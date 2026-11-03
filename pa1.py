
import os
import json
import time
import random
import math
import msvcrt
from datetime import datetime
from prettytable import PrettyTable

FILE_DATA = "data.json"
BATAS_LOGIN = 3
METODE_PEMBAYARAN = ("E-Money",)
MENU_AWAL = []

DATA_AWAL = {
    "users": [
        {"username": "admin", "password": "admin123", "role": "admin", "saldo": 0}
    ],
    "menu": MENU_AWAL,
    "transaksi": []
}


def baca_input(pesan="", sembunyikan=False):
    print(pesan, end="", flush=True)
    karakter = []
    while True:
        try:
            tombol = msvcrt.getwch()
        except KeyboardInterrupt:
            continue
        if tombol in ("\x00", "\xe0"):
            msvcrt.getwch()
            continue
        if tombol in ("\x03", "\x1a"):
            continue
        if tombol in ("\r", "\n"):
            print()
            return "".join(karakter)
        if tombol == "\b":
            if karakter:
                karakter.pop()
                print("\b \b", end="", flush=True)
        elif tombol.isprintable():
            karakter.append(tombol)
            print("*" if sembunyikan else tombol, end="", flush=True)


def input(pesan=""):
    return baca_input(pesan)


def input_password(pesan="Password: "):
    return baca_input(pesan, sembunyikan=True)


def input_username(pesan):
    return baca_input(pesan).strip()


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def format_rupiah(angka):
    return "Rp" + f"{angka:,.0f}".replace(",", ".")


def muat_data():
    try:
        with open(FILE_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
        data.setdefault("users", [])
        data.setdefault("menu", [])
        data.setdefault("transaksi", [])
        return data
    except FileNotFoundError:
        simpan_data(DATA_AWAL)
        return json.loads(json.dumps(DATA_AWAL))
    except json.JSONDecodeError:
        print("Peringatan: data.json rusak/tidak valid. Menggunakan data awal.")
        simpan_data(DATA_AWAL)
        return json.loads(json.dumps(DATA_AWAL))
    except OSError as error:
        print(f"Gagal membaca file: {error}")
        return json.loads(json.dumps(DATA_AWAL))


def simpan_data(data):
    try:
        with open(FILE_DATA, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        print(f"Gagal menyimpan data: {error}")
        return False


def input_angka(pesan, minimum=0):
    while True:
        nilai = input(pesan).strip()
        if nilai.lower() == "b":
            return None
        try:
            angka = int(nilai)
            if angka < minimum:
                print(f"Nilai minimal adalah {minimum}.")
                continue
            return angka
        except ValueError:
            print("Input harus berupa angka bulat. Ketik 'b' untuk batal.")


def konfirmasi(pesan):
    while True:
        jawaban = input(pesan + " (y/n): ").strip().lower()
        if jawaban in ("y", "n"):
            return jawaban == "y"
        print("Masukkan y atau n.")


def cari_user(data, username):
    for user in data["users"]:
        if user["username"].lower() == username.lower():
            return user
    return None


def cari_menu(data, id_menu):
    for item in data["menu"]:
        if item["id"] == id_menu:
            return item
    return None


def tampilkan_menu(data):
    if not data["menu"]:
        print("Menu makanan masih kosong.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Kategori", "Harga", "Stok"]
    for item in data["menu"]:
        tabel.add_row([
            item["id"], item["nama"], item["kategori"],
            format_rupiah(item["harga"]), item["stok"]
        ])
    print(tabel)


def registrasi(data):
    print("\n=== REGISTRASI USER ===")
    while True:
        username = input_username("Buat username (min. 4 karakter): ")
        if len(username) < 4:
            print("Username minimal 4 karakter.")
        elif not username.replace("_", "").isalnum():
            print("Username hanya boleh berisi huruf, angka, dan underscore.")
        elif cari_user(data, username):
            print("Username sudah digunakan. Pilih username lain.")
        else:
            break

    while True:
        password = input_password("Buat password (min. 6 karakter): ")
        if len(password) < 6:
            print("Password minimal 6 karakter.")
        else:
            break

    data["users"].append({
        "username": username,
        "password": password,
        "role": "user",
        "saldo": 0
    })
    simpan_data(data)
    print("Registrasi berhasil. Silakan login.")


def login(data):
    print("\n=== LOGIN ===")
    for percobaan in range(BATAS_LOGIN):
        username = input_username("Username: ")
        password = input_password("Password: ")
        user = cari_user(data, username)

        if user and user["password"] == password:
            print(f"Login berhasil. Selamat datang, {user['username']}!")
            time.sleep(1)
            return user

        sisa = BATAS_LOGIN - percobaan - 1
        print(f"Username atau password salah. Sisa percobaan: {sisa}")
        if sisa > 0:
            time.sleep(1)

    print("Login gagal 3 kali. Kembali ke menu awal.")
    return None


def top_up(data, user):
    nominal = input_angka("Nominal top up (Rp, ketik b untuk batal): ", 1)
    if nominal is None:
        return
    user["saldo"] += nominal
    simpan_data(data)
    print(f"Top up berhasil. Saldo sekarang: {format_rupiah(user['saldo'])}")


def invoice(transaksi):
    print("\n" + "=" * 48)
    print("              INVOICE PEMESANAN")
    print("=" * 48)
    print(f"Kode transaksi : {transaksi['kode']}")
    print(f"Waktu          : {transaksi['waktu']}")
    print(f"Username       : {transaksi['username']}")
    print("-" * 48)
    for detail in transaksi["detail"]:
        print(f"{detail['nama']} x{detail['jumlah']} = {format_rupiah(detail['subtotal'])}")
    print("-" * 48)
    print(f"Total          : {format_rupiah(transaksi['total'])}")
    print(f"Pembayaran     : {transaksi['metode']}")
    print(f"Status         : {transaksi['status']}")
    print("=" * 48)


def pesan_makanan(data, user):
    if not data["menu"]:
        print("Belum ada menu yang dapat dipesan.")
        return

    keranjang = []
    while True:
        tampilkan_menu(data)
        pilihan = input_angka("Masukkan ID makanan (0 untuk checkout, b untuk batal): ", 0)
        if pilihan is None:
            print("Pemesanan dibatalkan.")
            return
        if pilihan == 0:
            break

        item = cari_menu(data, pilihan)
        if not item:
            print("ID menu tidak ditemukan.")
            continue
        if item["stok"] <= 0:
            print("Stok makanan habis.")
            continue

        jumlah = input_angka(f"Jumlah {item['nama']} (tersedia {item['stok']}): ", 1)
        if jumlah is None:
            continue

        jumlah_di_keranjang = sum(
            x["jumlah"] for x in keranjang if x["id"] == item["id"]
        )
        if jumlah + jumlah_di_keranjang > item["stok"]:
            print("Jumlah melebihi stok yang tersedia.")
            continue

        baris = next((x for x in keranjang if x["id"] == item["id"]), None)
        if baris:
            baris["jumlah"] += jumlah
            baris["subtotal"] = baris["jumlah"] * item["harga"]
        else:
            keranjang.append({
                "id": item["id"],
                "nama": item["nama"],
                "harga": item["harga"],
                "jumlah": jumlah,
                "subtotal": jumlah * item["harga"]
            })
        print("Item ditambahkan ke keranjang.")

    if not keranjang:
        print("Keranjang kosong.")
        return

    total = sum(item["subtotal"] for item in keranjang)
    print("\n=== RINGKASAN PESANAN ===")
    tabel = PrettyTable(["Nama", "Jumlah", "Harga", "Subtotal"])
    for item in keranjang:
        tabel.add_row([
            item["nama"], item["jumlah"],
            format_rupiah(item["harga"]), format_rupiah(item["subtotal"])
        ])
    print(tabel)
    print("Total:", format_rupiah(total))
    print("Saldo:", format_rupiah(user["saldo"]))

    if user["saldo"] < total:
        print("Saldo tidak cukup. Silakan top up terlebih dahulu.")
        return
    if not konfirmasi("Lanjutkan pembayaran dengan E-Money?"):
        print("Pembayaran dibatalkan.")
        return

    for baris in keranjang:
        item = cari_menu(data, baris["id"])
        if item is None or item["stok"] < baris["jumlah"]:
            print("Stok berubah atau tidak cukup. Pesanan dibatalkan.")
            return
    if user["saldo"] < total:
        print("Saldo tidak cukup.")
        return

    user["saldo"] -= total
    for baris in keranjang:
        item = cari_menu(data, baris["id"])
        item["stok"] -= baris["jumlah"]

    transaksi = {
        "kode": f"ORD-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}",
        "waktu": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "username": user["username"],
        "detail": keranjang,
        "total": total,
        "metode": METODE_PEMBAYARAN[0],
        "status": "Berhasil"
    }
    data["transaksi"].append(transaksi)
    simpan_data(data)
    invoice(transaksi)
    print(f"Saldo tersisa: {format_rupiah(user['saldo'])}")


def riwayat_transaksi(data, user=None):
    daftar = data["transaksi"] if user is None else [
        trx for trx in data["transaksi"] if trx["username"] == user["username"]
    ]
    if not daftar:
        print("Belum ada transaksi.")
        return

    tabel = PrettyTable(["Kode", "Waktu", "Username", "Total", "Status"])
    for trx in daftar:
        tabel.add_row([
            trx["kode"], trx["waktu"], trx["username"],
            format_rupiah(trx["total"]), trx["status"]
        ])
    print(tabel)

    if konfirmasi("Cetak invoice dari salah satu transaksi?"):
        kode = input("Masukkan kode transaksi: ").strip()
        transaksi = next((trx for trx in daftar if trx["kode"] == kode), None)
        if transaksi:
            invoice(transaksi)
        else:
            print("Transaksi tidak ditemukan atau tidak dapat diakses.")


def crud_menu(data):
    while True:
        print("\n=== KELOLA MENU (ADMIN) ===")
        print("1. Lihat menu\n2. Tambah menu\n3. Ubah menu\n4. Hapus menu\n0. Kembali")
        pilih = input("Pilih: ").strip()

        if pilih == "1":
            tampilkan_menu(data)

        elif pilih == "2":
            nama = input("Nama makanan: ").strip()
            if not nama:
                print("Nama tidak boleh kosong.")
                continue

            kategori = input("Kategori (Makanan/Minuman): ").strip().title()
            if kategori not in ("Makanan", "Minuman"):
                print("Kategori harus Makanan atau Minuman.")
                continue

            harga = input_angka("Harga (Rp): ", 1)
            stok = input_angka("Stok awal: ", 0)
            if harga is None or stok is None:
                print("Penambahan dibatalkan.")
                continue

            if any(x["nama"].lower() == nama.lower() for x in data["menu"]):
                print("Nama menu sudah ada.")
                continue

            id_baru = max((x["id"] for x in data["menu"]), default=0) + 1
            data["menu"].append({
                "id": id_baru, "nama": nama, "harga": harga,
                "stok": stok, "kategori": kategori
            })
            simpan_data(data)
            print("Menu berhasil ditambahkan.")

        elif pilih == "3":
            tampilkan_menu(data)
            id_menu = input_angka("ID menu yang diubah: ", 1)
            if id_menu is None:
                continue

            item = cari_menu(data, id_menu)
            if not item:
                print("Menu tidak ditemukan.")
                continue

            print("Kosongkan nama/kategori untuk mempertahankan nilai lama.")
            nama = input(f"Nama [{item['nama']}]: ").strip()
            kategori = input(f"Kategori [{item['kategori']}]: ").strip().title()

            if nama:
                if any(
                    x["id"] != id_menu and x["nama"].lower() == nama.lower()
                    for x in data["menu"]
                ):
                    print("Nama menu sudah dipakai menu lain.")
                    continue
                item["nama"] = nama

            if kategori:
                if kategori not in ("Makanan", "Minuman"):
                    print("Kategori harus Makanan atau Minuman.")
                    continue
                item["kategori"] = kategori

            harga = input(f"Harga [{item['harga']}] (kosong = tetap): ").strip()
            stok = input(f"Stok [{item['stok']}] (kosong = tetap): ").strip()

            try:
                if harga:
                    nilai_harga = int(harga)
                    if nilai_harga <= 0:
                        raise ValueError
                    item["harga"] = nilai_harga
                if stok:
                    nilai_stok = int(stok)
                    if nilai_stok < 0:
                        raise ValueError
                    item["stok"] = nilai_stok
            except ValueError:
                print("Harga harus lebih dari 0 dan stok tidak boleh negatif. Periksa kembali.")
                continue

            simpan_data(data)
            print("Menu berhasil diperbarui.")

        elif pilih == "4":
            tampilkan_menu(data)
            id_menu = input_angka("ID menu yang dihapus: ", 1)
            if id_menu is None:
                continue

            item = cari_menu(data, id_menu)
            if not item:
                print("Menu tidak ditemukan.")
                continue

            if konfirmasi(f"Yakin menghapus {item['nama']}?"):
                data["menu"].remove(item)
                simpan_data(data)
                print("Menu berhasil dihapus.")
            else:
                print("Penghapusan dibatalkan.")

        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid.")


def kelola_akun(data):
    tabel = PrettyTable(["Username", "Role", "Saldo"])
    for user in data["users"]:
        tabel.add_row([
            user["username"], user["role"], format_rupiah(user["saldo"])
        ])
    print(tabel)

    if not konfirmasi("Hapus akun user?"):
        return

    username = input("Username yang dihapus: ").strip()
    user = cari_user(data, username)
    if not user:
        print("Akun tidak ditemukan.")
    elif user["role"] == "admin":
        print("Akun admin awal tidak dapat dihapus.")
    elif konfirmasi(f"Yakin menghapus akun {username}?"):
        data["users"].remove(user)
        simpan_data(data)
        print("Akun berhasil dihapus.")


def laporan_admin(data):
    transaksi = data["transaksi"]
    pendapatan = sum(trx["total"] for trx in transaksi)
    jumlah_transaksi = len(transaksi)
    terjual = {}

    for trx in transaksi:
        for detail in trx["detail"]:
            terjual[detail["nama"]] = terjual.get(detail["nama"], 0) + detail["jumlah"]

    print("\n=== LAPORAN RINGKAS ADMIN ===")
    print("Total pendapatan :", format_rupiah(pendapatan))
    print("Jumlah transaksi :", jumlah_transaksi)
    print(
        "Rata-rata transaksi:",
        format_rupiah(math.floor(pendapatan / jumlah_transaksi))
        if jumlah_transaksi else format_rupiah(0)
    )

    if terjual:
        terbanyak = max(terjual.values())
        terlaris = [
            nama for nama, jumlah in terjual.items() if jumlah == terbanyak
        ]
        print(f"Produk terlaris   : {', '.join(terlaris)} ({terbanyak} item)")
    else:
        print("Produk terlaris   : Belum ada penjualan.")


def menu_admin(data, user):
    while True:
        print(f"\n=== MENU ADMIN: {user['username']} ===")
        print("1. Kelola menu makanan (CRUD)")
        print("2. Lihat seluruh akun")
        print("3. Riwayat seluruh transaksi")
        print("4. Laporan ringkas")
        print("5. Lihat menu makanan")
        print("0. Logout")

        pilih = input("Pilih: ").strip()
        if pilih == "1":
            crud_menu(data)
        elif pilih == "2":
            kelola_akun(data)
        elif pilih == "3":
            riwayat_transaksi(data)
        elif pilih == "4":
            laporan_admin(data)
        elif pilih == "5":
            tampilkan_menu(data)
        elif pilih == "0":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")


def menu_user(data, user):
    while True:
        print(f"\n=== MENU USER: {user['username']} ===")
        print(f"Saldo E-Money: {format_rupiah(user['saldo'])}")
        print("1. Lihat menu makanan")
        print("2. Pesan makanan")
        print("3. Top up E-Money")
        print("4. Riwayat transaksi saya")
        print("0. Logout")

        pilih = input("Pilih: ").strip()
        if pilih == "1":
            tampilkan_menu(data)
        elif pilih == "2":
            pesan_makanan(data, user)
        elif pilih == "3":
            top_up(data, user)
        elif pilih == "4":
            riwayat_transaksi(data, user)
        elif pilih == "0":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")


def main():
    data = muat_data()
    bersihkan_layar()

    while True:
        print("\n" + "=" * 42)
        print("   SISTEM PEMESANAN MAKANAN ONLINE")
        print("=" * 42)
        print("1. Registrasi")
        print("2. Login")
        print("3. Lihat menu makanan")
        print("0. Keluar")

        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            registrasi(data)
        elif pilih == "2":
            user = login(data)
            if user:
                if user["role"] == "admin":
                    menu_admin(data, user)
                else:
                    menu_user(data, user)
                data = muat_data()
        elif pilih == "3":
            tampilkan_menu(data)
        elif pilih == "0":
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
