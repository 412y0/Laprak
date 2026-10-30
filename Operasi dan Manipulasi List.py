##Kumpulan Data
data_string = ["Papa", "Mama", "Anak", "Kakek", "Nenek"]
print(data_string)
print(" ")
data_boolean = [True, False, True, False]
print(data_boolean)
print(" ")
data_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(data_integer)
print(" ")
data_campuran = ["Papa", 1, True, "Mama", 2, False]
print(data_campuran)
print(" ")

##Operassi List
data_range = range(1, 10)
print(data_range)
data_list = list(data_range)
print(data_list)
print(" ")

##Membuat list dengan for loop, list comprehension
list_for = [i **2 for i in range(0, 10)]
print(list_for)
print(" ")
##Membuat list dengan for dan if
list_for_if = [i **2 for i in range(0, 10) if i  != 5]
print(list_for_if)
print(" ")
list_for_if = [i **2 for i in range(0, 10) if i % 2 != 0]
print(list_for_if)
print(" ")

##Manipulasi List
data = ["Mak", "Pak", "Puding", "Kakak", "Adik"]
print(" ")
##Mengambil data list
print(data[0])
print(f"data pertama adalah {data[0]}")
print(" ")

##Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"jumlah data dalam list adalah {panjang_data}")
print(" ")

##Manipulasi data list
print(f"data sebelum ditambah = \n{data}")
data.insert(2, "Kucing")
print(f"data setelah diubah = \n{data}")
print(" ")

##Menambah list dengan list
data_baru = ["Ayam", "Ikan"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")
print(" ")

##Merubah data
data[1] = "Bapak"
print(f"data diubah = \n{data}")
print(" ")
##Menghapus Data
data.remove("Kucing")
print(f"data setelah dihapus = \n{data}")
print(" ")
##Menghapus data paling akhir
data.pop()
print(f"data akhir = \n{data}")
print(" ")

##Operasi List
data_angka = [1, 2, 3, 4, 5]
print(f"data angka = \n{data_angka}")
print(" ")

#count data
jumlah_data = data_angka.count(3)
print(f"jumlah data 3 = {jumlah_data}")
print(" ")

##Ambil posisi data
data = ["Spi", "Delman", 1, 5, 8]
index_delman = data.index("Delman")
print(f"posisi Delman = {index_delman}")
print(" ")

##Mengurutkan List
print(f"data sebelum diurutkan = \n{data_angka}")
data_angka.sort()
print(f"data setelah diurutkan = \n{data_angka}")
print(" ")

###Membalik urutan list
print(f"data sebelum dibalik = \n{data_angka}")
data_angka.reverse()
print(f"data setelah dibalik = \n{data_angka}")
print(" ")

##Menggabungkan List
data_angka2 = [6, 7, 8, 9, 10]
print(f"data angka 1 = \n{data_angka}")
print(f"data angka 2 = \n{data_angka2}")
data_angka.extend(data_angka2)
print(f"data gabungan = \n{data_angka}")
print(" ")


##LATIHAN
#1. Diberikan list berikut:
#   kendaraan = ["Motor", "Mobil", "Sepeda", "Bus"]
#   a. Tambahkan "Truk" ke dalam list kendaraan.
#   b. Sisipkan "Becak" pada index ke 1.
#   c. Hapus data yang berada paling belakang dari list tersebut.
#   d. Ubaha elemen 'sepeda' menjadi 'skuter'.
#   e. Tampilkan jumlah data dalam list kendaraan.
#   Jawaban:
kendaraan = ["Motor", "Mobil", "Sepeda", "Bus"]
print("a. Tambahkan 'Truk' ke dalam list kendaraan.")
kendaraan.append("Truk")
print(kendaraan)
print(" ")
print("b. Sisipkan 'Becak' pada index ke 1.")
kendaraan.insert(1, "Becak")
print(kendaraan)
print(" ")
print("c. Hapus data yang berada paling belakang dari list tersebut.")
kendaraan.pop()
print(kendaraan)
print(" ")
print("d. Ubah elemen 'Sepeda' menjadi 'Skuter'.")
kendaraan[2] = "Skuter"
print(kendaraan)
print(" ")
print("e. Tampilkan jumlah data dalam list kendaraan.")
print(f"Jumlah data dalam list kendaraan: {len(kendaraan)}")

#2. Diberikan list berikut:
#   angka = [75, 80, 90, 75, 85, 100, 65]
#   a. Cari tahu di indeks berapa skor 100 berada.
#   b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.
#   c. Urutkan list skor tersebut dari nilai terkecil hingga terbesar.
#   d. Balik urutan list yang sudah diurutkan tersebut sehingga menjadi dari nilai terbesar hingga terkecil.
#   Jawaban:
angka = [75, 80, 90, 75, 85, 100, 65]
print("a. Cari tahu di indeks berapa skor 100 berada.")
index_100 = angka.index(100)
print(f"Skor 100 berada di indeks: {index_100}")
print(" ")
print("b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.")
count_75 = angka.count(75)
print(f"Ada {count_75} siswa yang mendapatkan skor 75.")
print(" ")
print("c. Urutkan list skor tersebut dari nilai terkecil hingga terbesar.")
angka.sort()
print(f"List skor setelah diurutkan: {angka}")
print(" ")
print("d. Balik urutan list yang sudah diurutkan tersebut sehingga menjadi dari nilai terbesar hingga terkecil.")
angka.reverse()
print(f"List skor setelah dibalik: {angka}")
print(" ")

#3. menu_utama = ["Nasi Goreng", "Mie Ayam"]
#   menu_tambahan = ["Kerupuk", "Es Teh"]
#   Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut.
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
print("Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, kemudian tampilkan hasil dari data gabungan tersebut.")
menu_utama.extend(menu_tambahan)
print(f"Data gabungan menu: {menu_utama}")
print(" ")

#4. Diberikan data nested list berupa informasi nama barang dan harganya:
#   data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
#   a. Tampilkan harga dari "Pensil" (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik darilist tersebut.
#   b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: "Nama Barang: [nama barang], Harga: [harga barang]" untuk setiap elemen didalamnya
#   Jawaban:
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
print("a. Tampilkan harga dari 'Pensil' (yaitu 2000) dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.")
harga_pensil = data_barang[1][1]
print(f"  " f"Harga dari Pensil adalah: {harga_pensil}")
print(" ")
print("b. Gunakan perulangan untuk membaca data satu per satu, lalu tampilkan output dengan format: 'Nama Barang: [nama barang], Harga: [harga barang]' untuk setiap elemen didalamnya.")
for barang in data_barang:
    print(f"  " f"Nama Barang: {barang[0]}, Harga: {barang[1]}")
print(" ")