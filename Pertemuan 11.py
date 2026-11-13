##MULTI KEYS & NESTING DICTIONARY
import datetime
mahasiswa1 = {
    "nama": "Budi",
    "nim": "123456789",
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2000,10,10)
}

mahasiswa2 = {
    "nama": "Siti",
    "nim": "987654321",
    'sks_lulus': 120,
    'beasiswa': True,
    'lahir': datetime.datetime(2001,5,15)
}

mahasiswa3 = {
    "nama": "Andi",
    "nim": "456789123",
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(1999,12,20)
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3
}

print(f"{'KEY': <6} {'SKS': <3} {'NAMA': <6} {'Beasiswa': <9} {'Lahir': <10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
    key = mahasiswa
    sks = data_mahasiswa[mahasiswa]['sks_lulus']
    nama = data_mahasiswa[mahasiswa]['nama']
    beasiswa = data_mahasiswa[mahasiswa]['beasiswa']
    lahir = data_mahasiswa[mahasiswa]['lahir'].strftime("%d-%m-%Y")
    
    print(f"{key: <6} {sks: <3} {nama: <6} {beasiswa: <9} {lahir: <10}")
    print("\n")

##LATIHAN DICTIONARY BAGIAN 1
import datetime

mahasiswa_template = {
    "nama": "",
    "nim": "",
    'sks_lulus': 0,
    'beasiswa': False,
    'lahir': datetime.datetime(2000,1,1)
}

data_mahasiswa = {}
print(f"{'SELAMAT DATANG': ^20}")
print(f"{'DATA MAHASISWA': ^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input("Masukkan nama mahasiswa: ")
mahasiswa['nim'] = input("Masukkan NIM mahasiswa: ")
TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan Lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31):"))
mahasiswa['Lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print(mahasiswa)
print("\n")

##LATIHAN DICTIONARY BAGIAN 2
import datetime
import os
import string
import random

# Template dict mahasiswa
mahasiswa_template = {
    "nama": "",
    "nim": "",
    'sks_lulus': 0,
    'beasiswa': False,
    'lahir': datetime.datetime(2000,1,1)
}

data_mahasiswa = {}
while True: 
    #os.system('cls') #untuk membersihkan layar
    os.system("clear")
    print(f"{'SELAMAT DATANG': ^20}")
    print(f"{'DATA MAHASISWA': ^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama mahasiswa: ")
    mahasiswa['nim'] = input("NIM mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31):"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_mahasiswa.update ({KEY: mahasiswa})

# dari program sebelumnya, hilangkan beasiswa
    print(f"\n{KEY: <6}  {'Nama': <17}  {'NIM': <8}  {'SKS Lulus': <10}  {'Tanggal Lahir': <10}")
    print("\n")
    is_done = input("Mau tambaha lagi bro (y/n)?")
    if is_done == "n":
        break

print("\nAkhir dari program, terimakasih")
print("\n")

## TUGAS
print("Buatlah program sistem manajemen perpustakaan sederhana (menambahkan dan menampilkan buku baru ke dalam sistem")
print("menggunakan konsep multi-keys dan nesting dictionary dengan format:")
print("-KEYS")
print("-JUDUL BUKU")
print("-PENULIS")
print("-TAHUN TERBIT")
print("-TANGGAL TERAKHIR PINJAM")
print("-STATUS (TERSEDIA/TIDAK)")

print("Jawab")
import datetime
import string
import random
import os

book_template = {
    'Judul': "",
    'Penulis': "",
    'Tahun Terbit': "",
    'Tanggal Terakhir Pinjam': "",

}

data_book = {}

while True: 
    print(f"{'SELAMAT DATANG DI PERPUSTAKAAN': ^20}")
    print("-"*20)

    book = dict.fromkeys(book_template.keys())
    book['Judul'] = input("Judul Buku: ")
    book['Penulis'] = input("Penulisnya: ")
    book['Tahun Terbit'] = input("Tahun Terbit: ")
    book['Tanggal Terakhir Pinjam'] = input("Tanggal Terakhir Pinjam: ")

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (6)))
    data_book.update({KEY:book})

    print(f"{'KEY':<6} {'Judul':<6} {'Penulis':<6} {'Tahun Terbit':^6} {'Tanggal Terakhir Pinjam':^6}")
    print("-"*60)

    for book in data_book:
        KEY = book

        JUDUL = data_book[KEY] ['Judul']
        PENULIS = data_book[KEY] ['Penulis']
        TAHUN_TERBIT = data_book[KEY] ['Tahun Terbit']
        TANGGAL_TERAKHIR_PINJAM = data_book[KEY] ['Tanggal Terakhir Pinjam']

        print(f"{KEY:<6} {JUDUL:<6} {PENULIS:<6} {TAHUN_TERBIT:^6} {TANGGAL_TERAKHIR_PINJAM:^6}")
    print("\n")
    status = input("Status dari buku tersebut:")
    if status == "Tersedia":
        break
    
    print("\nSelamat Menikmati Hari-mu:D")
