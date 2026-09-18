##Perulangan (Loop)
angka = 1
print(angka)
angka = angka + 1
print(angka)
angka = angka + 1
print(angka)

# for kondisi
#     aksi

#dengan list
angka2 = [0, 1, 2, 3, 4]
print(angka2)

for i in angka2:
    print(f"i sekarang -> {i}")
    print("akhiri program")

print(' ')
#dengan range
angka3 = range (5)
for i in angka3:
    print(f"i sekarang -> {i}")
print("akhiri program")
angka4 = range(1,10)
for i in angka4:
    print(f"i sekarang -> {i}")
print(" ")
#menggunakan string
data_str = "saya ganteng abiezz"

for huruf in data_str:
    print(huruf)
print(" ")

# WHILE LOOP
angka = 10
while angka > 5:
    print("JATUH, JATUH, JATUH, UDE TOLONG AKU UDE!!!")
    break

angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    print("JATUH, JATUH, JATUH, UDE TOLONG AKU UDE!")

print("program berakhir, HAYOYO MAK UDE!!!!")
print(' ')
## CONTINUE, PASS< BREAK
#PASS
angka = 0
while angka < 5:
    angka = angka + 1

    if(angka == 3):
        pass
        print(angka)

#CONTINUE
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka = angka +1
    print(f"angka sekarang -> {angka}")

    if(angka ==3):
        print("nice")
        print("HALOOOO COYY!!!!!")
print("finish")
#BREAK
angka = 0
print(f"angka sekarang -> {angka}")

while angka < 5:
    angka = angka + 1
    print(f"angka sekarang -> {angka}")

    if(angka == 3):
        print("nice")
        break
    print("whassup")
    print(' ')

print("cukup masssssss!!!!!!!!!!!!")

## LATIHAN PERULANGAN
# *
# * *
# * * *
# * * * *
# * * * * *

#latihan membuat segitiga 

# 1. Menggunakan FOR
sisi = 4
count = 1

for i in range(sisi):
    print("*" * count)
    count += 1

# 2. Menggunakan While
sisi = 4
count = 1

while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break

## LATIHAN
# BUAT PROGRAM YG MENAMPILKAN BILANGAN GANJIL DAN GENAP DARI 1 SAMPAI 50 MENGGUNAKAN PERULANGAN!
# BUAT PROGRAM YANG MENAMPILKAN SEMUA BILANGAN PRIMA ANTARA 1 SAMPAI 100 MENGGUNAKAN PERULANGAN!
# JAWAB
print(' ')
print("LATIHAN")
print("BUAT PROGRAM YG MENAMPILKAN BILANGAN GANJIL DAN GENAP DARI 1 SAMPAI 50 MENGGUNAKAN PERULANGAN!")
for angka in range(1,51):
    if angka % 2 == 0:
        print(f"{angka} bilangan genap")
    else:
        print(f"{angka} bilangan ganjil")
print(' ')
print("BUAT PROGRAM YANG MENAMPILKAN SEMUA BILANGAN PRIMA ANTARA 1 SAMPAI 100 MENGGUNAKAN PERULANGAN!")
bilangan_prima = [angka for angka in range(2, 101) if all(angka % i != 0 for i in range(2, int(angka**0.5) + 1))]
print(bilangan_prima)