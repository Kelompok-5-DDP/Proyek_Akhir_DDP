# Proyek_Akhir_DDP

Sistem Pemesanan Makanan Online

Anggota & Peran:
- Rafik Anugrah Yana (Konsep, Coding)
1. Referensi konsep program
2. Coding
3. Menjelaskan program di Laporan
4. Mencari bug dan error
- Wahyu Farras Zaky (Laporan)
1. Perancangan Laporan
2. Menjelaskan program di Laporan
3. Finishing Laporan
- Septiya Maharani (Konsep flowchart login admin dan registrasi)
1. Perancangan Laporan
2. Menjelaskan program di Laporan
3. Finishing Laporan
- Nila Amelia Nabilla (Konsep flowchart login user dan menu utama)
1. Pengembangan alur flowchart
2. Membuat Flowchart User dan menu utama
3. Mengecek alur flowchart


Deskripsi:

Perkembangan teknologi informasi dan perubahan gaya hidup masyarakat membuat kebutuhan akan layanan pemesanan makanan yang cepat, praktis, dan terorganisir terus meningkat. Konsumen kini terbiasa mengakses informasi menu, harga, dan ketersediaan makanan dengan mudah. Mereka juga mengharapkan proses pemesanan dan pembayaran yang efisien. Namun, tidak semua pelaku usaha kuliner, terutama usaha skala kecil dan menengah seperti warung makan, kantin, dan kedai, bisa mengikuti perkembangan tersebut. Sebagian besar masih mengelola proses pemesanan secara manual melalui buku catatan, nota kertas, atau ingatan pegawai. Cara kerja seperti ini menimbulkan berbagai permasalahan, baik bagi pelaku usaha maupun pelanggan.
Permasalahan tersebut meliputi: Pencatatan pesanan yang mudah terjadi kesalahan, menghitung total pembayaran yang membutuhkan waktu lama dan sering terjadi kesalahan hitung, pengelolaan stok yang tidak dipantau secara langsung, pengelolaan data menu dan harga yang kurang teratur, tidak adanya pencatatan riwayat transaksi yang rapi, rekapitulasi penjualan yang manual dan sering tidak tepat, sistem pembayaran tidak praktis dan sulit dicatat. Kurangnya kontrol atas hak akses dan keamanan data.

Berdasarkan permasalahan itu, dibutuhkan sistem pemesanan makanan yang bisa mengotomatisasi semua alur transaksi. Proses ini meliputi pendaftaran dan verifikasi pengguna, penampilan menu, pemesanan dengan pengecekan stok dan saldo, pembayaran, pencetakan bukti transaksi, serta pembuatan laporan penjualan. Sistem ini juga harus membedakan hak akses antara admin sebagai pengelola dan pengguna sebagai pelanggan.

Untuk memenuhi kebutuhan ini, penelitian ini membuat program Sistem Pemesanan Makanan Online dengan bahasa pemrograman Python yang berjalan di terminal. Program ini punya fitur registrasi dan login dengan batas percobaan. Pengguna bisa mengelola menu secara penuh, seperti menambah, melihat, mengubah, dan menghapus menu. Ada juga fitur pemesanan dengan keranjang belanja. Pembayaran memakai saldo E-Money. Program bisa mencetak invoice, menampilkan riwayat transaksi, dan membuat laporan ringkas penjualan. Semua data disimpan secara permanen dalam file JSON. Program ini dibuat sebagai prototipe dasar yang menunjukkan konsep sistem pemesanan makanan online dan bisa dikembangkan lagi menjadi aplikasi berbasis web atau mobile dengan basis data dan layanan pembayaran yang sesungguhnya.

Tujuan:

1.	Membuat program pemesanan makanan berbasis Python dengan pemisahan hak akses admin dan user.
2.	Menyediakan sistem registrasi dan login yang aman dengan validasi data dan batas percobaan.
3.	Memudahkan pelanggan melihat menu, memesan makanan, dan membayar menggunakan E-Money dengan validasi stok dan saldo otomatis.
4.	Membantu admin mengelola menu, akun pengguna, riwayat transaksi, dan laporan penjualan.
5.	Menghasilkan bukti transaksi berupa invoice dan riwayat pemesanan yang tercatat otomatis.
6.	Menerapkan konsep dasar pemrograman Python seperti percabangan, perulangan, fungsi, tuple, list, dictionary, penanganan error, dan pengelolaan file JSON.

FLOWCHART

Berikut ini merupakan flowchart dari sistem pemesanan makanan online yang menggambarkan alur proses kerja sistem, mulai dari proses awal hingga proses akhir. Flowchart ini dibuat untuk mempermudah pemahaman terhadap tahapan dan alur kerja sistem yang dikembangkan.

| NAMA FLOWCHART | GAMBAR FLOWCHART | PENJELASAN |
| :----: | :----: | :---- |
| 1. Menu Utama |<img width="753" height="631" alt="Menu Utama (1) jpg" src="https://github.com/user-attachments/assets/ebd05c95-bc0c-4a45-aa83-60b957060699" /> | <p>berikut ini adalah penjelasan alur flowchart dari menu utama.</p><p><b>1. Program dimulai dari simbol terminal Mulai</b> yang kemudian mencetak tampilan menu utama ke layar dengan pilihan:<br>&nbsp;&nbsp;&nbsp;&nbsp;1. Registrasi<br>&nbsp;&nbsp;&nbsp;&nbsp;2. Login<br>&nbsp;&nbsp;&nbsp;&nbsp;3. Lihat Menu Makanan, dan<br>&nbsp;&nbsp;&nbsp;&nbsp;0. Keluar</p><p><b>2. Sistem akan meminta pengguna</b> memasukkan pilihan angka melalui proses input.</p><p><b>3. Selanjutnya, terdapat proses validasi</b> menggunakan struktur keputusan (decision). Jika input yang dimasukkan di luar pilihan menu, sistem akan menampilkan pesan "Pilihan Tidak Valid" dan meminta input ulang.</p><p><b>4. Jika input valid</b>, sistem akan mencocokkan pilihan pengguna:<br>• Pilihan 1: Masuk ke Menu Registrasi.<br>• Pilihan 2: Masuk ke Menu Login.<br>• Pilihan 3: Menampilkan Daftar Menu Makanan, kemudian sistem akan kembali ke Menu Utama.<br>• Pilihan 0 (keluar): Menampilkan pesan "Terima kasih Telah Menggunakan Aplikasi" dan program berhenti (Selesai).</p> |
| 2. Menu Resgistrasi | <img width="304" height="1072" alt="Salinan dari pa ddp-Registrasi drawio" src="https://github.com/user-attachments/assets/fcfb929c-3449-4332-a08e-a1b649530cc4" /> | <p>berikut ini adalah penjelasan alur flowchart dari menu registrasi:</p><p><b>1. Input dan Validasi Username</b><br>Pengguna diminta memasukkan username dengan ketentuan minimal 4 karakter. Sistem kemudian melakukan pengecekan kondisi (decision):<br>• Jika Tidak memenuhi syarat (&lt; 4 karakter), sistem menampilkan pesan "Username minimal 4 karakter" lalu mengarahkan pengguna untuk menginput ulang username.<br>• Jika Ya (valid), alur dilanjutkan ke tahap berikutnya.</p><p><b>2. Input dan Validasi Password</b><br>Pengguna diminta memasukkan password dengan ketentuan minimal 6 karakter. Sistem kembali melakukan validasi:<br>• Jika Tidak memenuhi syarat (&lt; 6 karakter), sistem menampilkan pesan "Password minimal 6 karakter" lalu meminta pengguna menginput ulang password.<br>• Jika Ya (valid), proses berlanjut ke penyimpanan.</p><p><b>3. Penyimpanan Data dan Output</b><br>• Sistem memproses data akun baru dan menyimpannya secara permanen ke dalam file penyimpanan database (data.json).<br>• Sistem mencetak pesan sukses "Registrasi berhasil. Silakan login." ke layar.</p><p><b>4. Jika registrasi telah perhasil</b>,program akan mengarahkan untuk kembali ke Menu Utama agar user bisa melakukan login dengan akun yang baru dibuat.</p> |
| 3. Menu Login Sebagai Admin | <img width="2132" height="4062" alt="Menu Utama" src="https://github.com/user-attachments/assets/e355827b-53fc-4b9f-8114-a4473eb11f0d" /> | <p>berikut ini adalah penjelasan alur flowchart dari menu login admin.</p><p><b>1. Proses Masuk (Login) dan Validasi Percobaan</b><br>Saat pengguna memasukkan username dan password admin, Sistem memeriksa kecocokan data melalui database (data.json). Jika data yang dimasukkan salah, sistem akan menghitung atau mengecek batas percobaan (maksimal 3 kali). Jika belum 3 kali, admin diminta memasukkan ulang username dan passwordnya. Jika kesalahan mencapai batas maksimal 3 kali, alur program akan menolak akses dan mengembalikan pengguna ke Menu Utama. Jika data yang dimasukkan benar, alur dilanjutkan masuk ke halaman Menu Admin dan menampilkan menu utama admin.</p><p><b>2. Tampilan Menu Utama Admin (Pilihan 0 - 5)</b><br>Setelah berhasil masuk, sistem menampilkan menu admin dan meminta input angka (0 sampai 5), jika menginput selain 0-5 akan menampilkan "Pilihan tidak valid":<br><br>• <b>Pilihan 1 (Kelola Menu Makanan):</b><br>Jika memilih (1.Kelola Menu Makanan), alur masuk ke sub-menu pengelolaan dengan pilihan angka 0 sampai 4:<br>&nbsp;&nbsp;- <i>Pilihan 1 (Tambah Menu):</i> Menginput nama dan kategori makanan, memvalidasi input (misal cek apakah kosong atau format angka harga valid), memasukkan harga, lalu sistem memperbarui dan menyimpan data permanen ke database (data.json) sebelum kembali ke menu kelola makanan.<br>&nbsp;&nbsp;- <i>Pilihan 2 (Ubah Menu):</i> Menampilkan daftar menu, memilih menu yang mau diubah, lalu memperbarui data dan menyimpannya kembali ke data.json.<br>&nbsp;&nbsp;- <i>Pilihan 3 (Hapus Menu):</i> Menampilkan daftar menu, memilih menu yang ingin dihapus, lalu menghapus data tersebut dari data.json.<br>&nbsp;&nbsp;- <i>Pilihan 4 (Lihat Menu):</i> Membaca database dan menampilkan daftar menu makanan.<br>&nbsp;&nbsp;- <i>Pilihan 0 (Keluar / Kembali):</i> Mengembalikan alur kembali ke Menu Utama Admin.<br><br>• <b>Pilihan 2 (Lihat Seluruh User):</b><br>Sistem membaca file data.json untuk menampilkan daftar akun pengguna (user) yang terdaftar di sistem, lalu kembali ke menu utama admin.<br><br>• <b>Pilihan 3 (Riwayat Seluruh Transaksi):</b><br>Sistem membaca data transaksi dari database (data.json), menampilkan seluruh catatan transaksi global, serta menyediakan opsi pencarian atau cetak invoice berdasarkan kode transaksi.<br><br>• <b>Pilihan 4 (Laporan Keuangan):</b><br>Sistem membaca dan memproses data riwayat transaksi dari data.json untuk menampilkan ringkasan laporan keuangan aplikasi.<br><br>• <b>Pilihan 5 (Lihat Menu Makanan):</b><br>Sistem membaca database (data.json) dan langsung menampilkan daftar menu makanan ke layar.<br><br>• <b>Pilihan 0 (Logout):</b><br>Mengakhiri sesi admin dan mengembalikan alur program keluar ke Menu Utama.</p> |
| 4. Menu Login Sebagai User | <img width="2407" height="3662" alt="Menu User (1) jpg" src="https://github.com/user-attachments/assets/72bc1a40-2378-4495-9fe9-00051ec99fe2" /> | <p>berikut ini adalah penjelasan alur flowchart dari menu login User.</p><p><b>1. Proses Masuk (Login) dan Validasi Percobaan</b><br>Saat pengguna memasukkan username dan password admin, Sistem memeriksa kecocokan data melalui database (data.json). Jika data yang dimasukkan salah, sistem akan menghitung atau mengecek batas percobaan (maksimal 3 kali). Jika belum 3 kali, admin diminta memasukkan ulang username dan passwordnya. Jika kesalahan mencapai batas maksimal 3 kali, alur program akan menolak akses dan mengembalikan pengguna ke Menu Utama. Jika data yang dimasukkan benar, alur dilanjutkan masuk ke halaman Menu User dan menampilkan menu utama user.</p><p><b>2. Tampilan Menu Utama User (Pilihan 0 - 4)</b><br>Setelah berhasil masuk, sistem menampilkan menu admin dan meminta input angka (0 sampai 4):<br><br>• <b>Pilihan 1 (Lihat Menu Makanan):</b> Sistem membaca data dari database (data.json) dan menampilkan daftar menu makanan yang tersedia beserta harganya kepada user.<br>• <b>Pilihan 2 (Pesan Makanan):</b> Alur masuk ke proses pemesanan, di mana user memilih menu, memasukkan jumlah pesanan, melakukan pengecekan saldo e-money, memproses transaksi pembelian, hingga sistem memperbarui saldo dan menyimpan catatan riwayat transaksi secara permanen ke dalam database (data.json).<br>• <b>Pilihan 3 (Top-Up E-Money):</b> Alur bagi user untuk menambah saldo digital (e-money). Sistem memproses nominal top-up, lalu memperbarui saldo akun user tersebut dan menyimpannya kembali ke database (data.json).<br>• <b>Pilihan 4 (Riwayat Transaksi Saya):</b> Sistem membaca data transaksi dari database (data.json) khusus untuk menampilkan catatan riwayat pembelian atau transaksi yang pernah dilakukan oleh user yang bersangkutan.<br>• <b>Pilihan 0 (Logout):</b> Keluar dari menu user dan mengembalikan alur program keluar ke Menu Utama.</p> |

HASIL OUTPUT PROGRAM

| NAMA OUTPUT | GAMBAR OUTPUT |
| :----: | :----: |
| Menu Utama | <img width="507" height="234" alt="image" src="https://github.com/user-attachments/assets/f9591384-5962-429e-93c1-aecd8a2a146c" /> |
| Menu Utama Apabila pilihan menu tidak valid | <img width="536" height="506" alt="image" src="https://github.com/user-attachments/assets/bd7b20d6-5e95-43df-adc5-b81266ed6c4e" /> |
| Tampilan Input 3 Lihat Menu Makanan | <img width="575" height="720" alt="image" src="https://github.com/user-attachments/assets/de48e422-0532-4975-9bd3-60c54e2fa059" /> |
| Tampilan Input 0 Keluar | <img width="508" height="236" alt="image" src="https://github.com/user-attachments/assets/d343d597-1a5a-4cfc-80fd-f35cd3e07879" /> | 
| Registrasi | <img width="317" height="380" alt="registrasi berhasil" src="https://github.com/user-attachments/assets/d712025a-d762-410a-b32c-d2dd7196cca8" /> |
| Menu Login Admin Gagagl | <img width="302" height="404" alt="Login admin gagal" src="https://github.com/user-attachments/assets/cf6b2af2-4f72-4dd2-9776-1bb69dbc0936" /> |
| Menu Login Admin Berhasil | <img width="275" height="314" alt="login admin berhasil" src="https://github.com/user-attachments/assets/8f99e310-2377-4bc7-8ec8-8aaf60d84df1" /> |
| Tampilan Menu Pilihan 1. Kelola menu makanan (CRUD) | <img width="233" height="296" alt="Tampilan pilihan 1 " src="https://github.com/user-attachments/assets/26c313e9-d8bc-43fa-b380-e71e69264b5d" /> |
| Tampilan 1. Lihat Menu | <img width="347" height="353" alt="1 Lihat Menu" src="https://github.com/user-attachments/assets/2e7957f2-fe1d-4b70-9986-0ec5a2a6c42d" /> |
| Tampilan 2. Tambah Menu( nama tidak boleh kosong) | <img width="226" height="257" alt="Tambah menu (Nama tidak boleh kosong)" src="https://github.com/user-attachments/assets/915be5dd-e493-46ab-a481-0eb23d08cd6d" /> |
| Tampilan 2. Tambah Menu (Katagori Salah) | <img width="281" height="263" alt="Tambah menu (Katagori salah)" src="https://github.com/user-attachments/assets/6c83edba-0f09-46d7-8de5-f2b34cfdbc03" /> |
| Tampilan 2. Tambah Menu (Menu Dibatalkan) | <img width="347" height="201" alt="Tambah menu (menu dibatalkan)" src="https://github.com/user-attachments/assets/c147a733-23fc-46df-b81b-fe68fb908b17" /> |
Tampilan 2. Tambah Menu (Menu Berhasil Ditambahkan) | <img width="330" height="305" alt="Tambah menu (menu berhasil ditambahkan" src="https://github.com/user-attachments/assets/3c13c5ed-8004-4830-8145-fae930da5440" /> |
| Tampilan 3. Ubah Menu ( ID Tidak Ditemukan ) | <img width="326" height="387" alt="Ubah menu (id tidak ditemukan" src="https://github.com/user-attachments/assets/7ba67fc3-b318-4d24-9af6-638d398df98b" /> | 
| Tampilan 3. Ubah Menu ( Ubah Gagal ) |<img width="426" height="419" alt="Ubah menu (ubah gagal)" src="https://github.com/user-attachments/assets/d64e8eeb-8165-4807-b18f-53816b2afab7" />
| Tampilan 3. Ubah Menu ( Menu Berhasil Diubah ) | <img width="362" height="423" alt="Ubah menu (menu berhasil di ubah" src="https://github.com/user-attachments/assets/4e8b57f4-e0da-40fb-b081-b44134044dd4" /> | 
| Tampilan 4. Hapus Menu ( ID Menu Tidak Ditemukan ) | <img width="309" height="387" alt="Hapus menu (Id tidak ditemukan)" src="https://github.com/user-attachments/assets/6e9f1d1c-8874-4fdb-92d4-e03d0dae4a0a" /> |
| Tampilan 4. Hapus Menu ( Hapus Menu Batal) | <img width="307" height="403" alt="Hapus menu (hapus batal)" src="https://github.com/user-attachments/assets/27869293-c6e7-4271-878c-da00ba1b4f82" /> |
| Tampilan 4. Hapus Menu ( Hapus Menu Berhasil ) | <img width="320" height="405" alt="Hapus menu (hapus berhasil)" src="https://github.com/user-attachments/assets/cefe4080-fdbc-4baf-b816-8274ecd2178f" /> |
| Tampilan 0. Kembali (Keluar dari Menu kelola menu) | <img width="215" height="236" alt="0 kembali menu utama admin" src="https://github.com/user-attachments/assets/fb36a887-fa68-409e-8c1d-c1c9db3751b7" /> |
| Gagal Keluar dari Kelola Menu | <img width="212" height="230" alt="Kelola menu tidak valid" src="https://github.com/user-attachments/assets/309da6fe-e4c2-4344-95dd-7e4274598bb0" /> | 
| Tampilan Menu Utama Admin 2. Lihat Seluruh Akun | <img width="221" height="300" alt="Menu admin 2 Lihat Seluruh akun" src="https://github.com/user-attachments/assets/80bb27e8-85b6-4155-96b1-84f97fe7cadb" /> | 
| Tampilan Menu Utama Admin 2. Lihat Seluruh Akun ( Tidak Hapus Akun User ) | <img width="222" height="416" alt="Menu admin 2 Lihat seluruh akun tidak hapus" src="https://github.com/user-attachments/assets/0c7385a8-6d26-4bac-90ce-d563da8c01e9" /> 
| Tampilan Menu Utama Admin 2. Lihat Seluruh Akun ( Berhasil Hapus Akun User ) | <img width="229" height="419" alt="2  Lihat akun (hapus berhasil)" src="https://github.com/user-attachments/assets/809e3236-b667-4f39-afd8-9609839ada81" /> |
| Tampilan 3. Riwayat seluruh akun ( Tidak cetak invois ) | <img width="486" height="342" alt="3  riwayat seluruh transaksi (tidak cetak invois" src="https://github.com/user-attachments/assets/ea1ae908-fed7-405b-a218-e55ff4c5fdf7" /> |
|  Tampilan 3. Riwayat seluruh akun ( cetak invois berhasil ) | <img width="502" height="426" alt="invois berhasil di cetak" src="https://github.com/user-attachments/assets/455d449c-ebf2-4494-9502-57595b4666f2" /> |
| Tampilan 4. Laporan Ringkas | <img width="237" height="319" alt="4  Laporan ringkas" src="https://github.com/user-attachments/assets/33ad71b6-c5ca-481e-a9bf-07014320e596" /> |
| Tampilan 5. Lihat Menu Makanan | <img width="320" height="377" alt="5 Lihat menu makanan" src="https://github.com/user-attachments/assets/9c5282a5-bc2e-41b7-a159-46937fbe8550" /> | 
| Tampilan Jika Gagal Keluar Dari menu utama Admin | <img width="186" height="247" alt="Gagal Keluar menu utama admin" src="https://github.com/user-attachments/assets/99e22348-5192-4314-92e8-df64b1608a3c" /> |
| Tampilan Berhasil Keluar Menu Utama Admin | <img width="278" height="252" alt="0 Logout menu utama admin" src="https://github.com/user-attachments/assets/da2a8a0a-d5f9-4f84-bbdb-245af781097d" /> |
| Menu Login User | <img width="261" height="177" alt="login menu user" src="https://github.com/user-attachments/assets/bc425cc7-b273-4db6-8966-434154c369ca" /> |
| Login User Gagal |
| Input User Tidak Valid | <img width="190" height="376" alt="user tdk valid" src="https://github.com/user-attachments/assets/0e34e64a-1014-4103-b998-3a79bbdf74c1" /> |
| Tampilan Menu 1 Lihat Menu Makanan | <img width="298" height="364" alt="user input 1" src="https://github.com/user-attachments/assets/ab7b586a-79f4-4aa1-be7e-7cf8a8323073" /> | 
| Tampilan id Makanan Tidak Valid | <img width="337" height="404" alt="input id makanan tidak valid" src="https://github.com/user-attachments/assets/2b266390-c036-4f7f-980b-a3fda4e9b651" /> |
| Tampilan Menu 2 Pesan Makanan | <img width="333" height="253" alt="user input 2" src="https://github.com/user-attachments/assets/d5f37479-c0f8-4595-9d59-23a7195ce6fd" /> |
| Tampilan Apabila id tidak ditemukan | <img width="675" height="755" alt="image" src="https://github.com/user-attachments/assets/0f6ee601-c795-4e12-be44-d6a0ba4028ed" /> |
| Tampilan Apabila id bukan angka bulat | <img width="713" height="314" alt="image" src="https://github.com/user-attachments/assets/5fbd5105-7b1b-4e2d-8221-83e2ca48972b" /> |
| Tampilan Apabila input Pesanan Melebihi Batas | <img width="597" height="313" alt="image" src="https://github.com/user-attachments/assets/19746188-b924-4e14-ad6c-8c686541566c" /> |
| Item di tambahkan ke keranjang | <img width="660" height="335" alt="image" src="https://github.com/user-attachments/assets/cdfa2a80-c303-40ac-a16e-8d508e4b8308" /> |
| Tampilan Apabila id tidak 0/b | <img width="652" height="348" alt="image" src="https://github.com/user-attachments/assets/5ea141ab-f51f-4d9d-a83c-4d61d4a2e4d5" /> |
| Tampilan Apabila Input b (batal) | <img width="650" height="377" alt="image" src="https://github.com/user-attachments/assets/d8672bc8-69b6-4657-b79a-856b9ca3d7cc" /> |
| Tampilan Apabila Input 0 (chekout) | <img width="663" height="546" alt="image" src="https://github.com/user-attachments/assets/9429dbb9-7533-4515-8c12-b78f6c542a17" /> |
| Tampilan Apabila Saldo Tidak Terisi | <img width="655" height="792" alt="image" src="https://github.com/user-attachments/assets/4154368f-97af-4db7-9303-457fc9e3e4d1" /> |
| Tampilan Pembayaran Dibatalkan | <img width="655" height="589" alt="image" src="https://github.com/user-attachments/assets/dfb70795-ae77-4503-826a-6e83a7130414" /> |
| Tampilan Apabila Terbayar | <img width="685" height="750" alt="image" src="https://github.com/user-attachments/assets/376bdc7c-83e9-42bb-85c6-5987764205ed" /> |
| Tampilan Menu 3 Top-Up E-Money | <img width="541" height="261" alt="image" src="https://github.com/user-attachments/assets/d7eb9c17-2253-4b1d-b6fc-46d7766cf591" /> |
| Tampilan Apabila Input b (batal) | <img width="520" height="482" alt="image" src="https://github.com/user-attachments/assets/34da15e6-813f-496e-9ee4-e1497f6cf021" /> |
| Tampilan Apabila Nominal Tidak Berupa Angka | <img width="626" height="304" alt="image" src="https://github.com/user-attachments/assets/4b5c9d90-6475-46a6-8625-da8c68e93abb" /> |
| Tampilan Apabila Berhasil Top-Up | <img width="541" height="289" alt="image" src="https://github.com/user-attachments/assets/ddcd087f-8c10-43ac-badc-beef2fee9bc0" /> |
| Tampilan Menu 4 Riwayat Transaksi Saya | <img width="965" height="338" alt="image" src="https://github.com/user-attachments/assets/a6d7011a-1ab3-4f22-97f1-931521133405" /> |
| Tampilan jika input n ( tidak cetak invoice) | <img width="983" height="401" alt="image" src="https://github.com/user-attachments/assets/8273cf18-8aa2-43a4-a457-866ec1a0a8e8" /> |
| Tampilan Jika Input y ( Cetak Input ) | <img width="970" height="818" alt="image" src="https://github.com/user-attachments/assets/053eea70-8128-4602-8948-ad8fdbe93502" /> |
| Tampilan Jika kode transaksi tidak valid | <img width="957" height="223" alt="image" src="https://github.com/user-attachments/assets/c4e7dddc-56b2-40de-adfc-3d254f03f2aa" /> |
| Tampilan Menu 0 Logout | <img width="534" height="514" alt="image" src="https://github.com/user-attachments/assets/90a1b96e-78c2-4399-8a41-2972d74c6d0e" /> |






