##TUPLE
#Tuple
#menggunakan kurung biasa
data_tuple = (10, 2, 4, 3, 2)
print(data_tuple)
print(data_tuple[1])

#Sets (himpunan)
data_sets = {10, 2, 4, 3}
print(data_sets)

# Sets are unordered, so indexing is not possible
# print(data_sets[1])  # This will raise a TypeError

##DICTIONARY
data_list = ['ucup', 'rendi', 'salsa']
print(data_list[1])
data_dict = {'key' : 'value',
             'cp' : 'ucup',
             'rd' : 'rendi',
             'sl' : 'salsa',
             'nmbr' : 123,
             'list' : data_list}

print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'][1])

##OPERASI DICTIONARY
data_dict = {"cup" : "ucup surucup",
             "rd" : "rendi sururendi",
             "sl" : "salsa surusalsa",
             }

#Panjang dictionary
lendict = len(data_dict)
print(f"panjang dictionary = {lendict}")
print(" ")
#mengecek key exist atau tidak
key = "cup"
checkkey = key in data_dict
print(f"apakah key {key} ada di dictionary? = {checkkey}")
print(" ")
#Mengakses value dengan get
print(f"mengakses value dengan get")
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan")) #mengecek key dengan message
print(" ")
#Mengupdate data
print("mengupdate data")
data_dict["cup"] = "ucup cihuy"
print(data_dict["cup"])
data_dict["de"] = "dede cihuy" #menambahkan data baru
print(data_dict["de"])

data_dict.update({"de" : "dede surudede"}) #mengupdate data
print(data_dict["de"])
print(" ")

#Menghapus data
print("menghapus data")
del data_dict["de"] #menghapus data
print(data_dict)
print(" ")

##LOOPING DICTIONARY
print("looping dictionary")
teman_teman = {
    "cup": "ucup surucup",
    "rd": "rendi sururendi",
    "sl": "salsa surusalsa",
    "well": "well suruwell"
    }
#Looping first try (yang keluar hanya key)
print("looping ffirst try (yang keluar hanya key)")
for teman in teman_teman:
    print(teman)
    print(" ")
#Operator mengambil item
print("operator mengambil item")
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
    print(" ")

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
    print(" ")

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)
    print(" ")

for key, value in teman_teman.items():
    print(f"key = {key} dan value = {value}")
    print(" ")

##LATIHAN / TUGAS
print("LATIHAN / TUGAS")
# 1. Tuple
#       a. Buatlah sebuah tuple bernama mahasiswa yang berisi 3 data dari anda (nama, nim, prodi)
#       b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya
#       c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi
#       d. Buatlah sebuah set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar
#          dan jelaskan apa yang terjadi pada angka 10 dan 4.
#   Jawab:
print("Soal 1  ")
print("a. Buatlah sebuah tuple bernama mahasiswa yang berisi 3 data dari anda (nama, nim, prodi)")
mahasiswa = ("Aryo Kusumo P", "2605060059", "Teknologi Informasi")
print(mahasiswa)
print("b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya")
print(f"NIM = {mahasiswa[1]}")
print(f"Prodi = {mahasiswa[2]}")
print("c. Coba jalankan kode mahasiswa[2] = 'Teknologi Informasi'. Amati pesan error yang muncul, lalu jelaskan mengapa hal tersebut terjadi")
# mahasiswa[2] = "Teknologi Informasi" # ini akan menghasilkan error karena tuple bersifat immutable (tidak bisa diubah setelah dibuat)
print("d. Buatlah sebuah set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4.")
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)
print("Angka 10 dan 4 hanya muncul sekali karena set tidak mengizinkan elemen duplikat")
print("\n")
# 2. Manipulasi Dictionary
#       a. Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut:
#          "nama" : "Aryo Kusumo P"
#          "nim" : "2605060059" 
#          "prodi" : "Teknologi Informasi"
#       b. Ubah nilai "prodi" menjadi "Sastra Mesin" sekaligus menambahkan key baru "angkatan" dengan nilai 2026
#       c. Hapus data "nim", lalu tampilkan hasil dictionary ke layar
#   Jawab:
print("Soal 2  ")
print("a. Buatlah sebuah dictionary bernama data_mahasiswa dengan pasangan key-value berikut:" \
"          'nama' : 'Aryo Kusumo P'" \
"          'nim' : '2605060059'" \
"          'prodi' : 'Teknologi Informasi'" \
")")
data_mahasiswa = {
    "nama": "Aryo Kusumo P",
    "nim": "2605060059",
    "prodi": "Teknologi Informasi"
}
print(data_mahasiswa)
print("b. Ubah nilai 'prodi' menjadi 'Sastra Mesin' sekaligus menambahkan key baru 'angkatan' dengan nilai 2026")
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026
print(data_mahasiswa)
print("c. Hapus data 'nim', lalu tampilkan hasil dictionary ke layar")
del data_mahasiswa["nim"]
print(data_mahasiswa)
print("\n")
# 3. Perulangan Dictionary
#       a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: ("apel" : 5000, "pisang" : 3000, "jeruk" : 7000, "Anggur" : 15000)
#       b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000"
#       c. Tampilkan total belanja
#   Jawab:
print("Soal 3  ")
print("a. Buatlah dictionary bernama keranjang dengan data harga buah berikut: ('apel' : 5000, 'pisang' : 3000, 'jeruk' : 7000, 'Anggur' : 15000)")
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
print(keranjang)
print("b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: 'Harga apel: Rp 5000'")
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
print("c. Tampilkan total belanja")
total_belanja = sum(keranjang.values())
print(f"Total belanja: Rp {total_belanja}")