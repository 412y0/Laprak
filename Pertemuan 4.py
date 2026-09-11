## LATIHAN 
# Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia tersebut berdasarkan kriteria berikut:
# 0-12  tahun       : Anak-anak
# 13-17 tahun       : Remaja
# 18-59 tahun       : Dewasa
# 60 tahun ke atas  : Lansia
# JAWAB
nama = str(input("Nama: "))
umur = int(input("umur: "))
if umur >= 0 and umur <= 12:
    print("Kategori anda: Anak-anak")
elif umur >= 13 and umur <= 17:
    print("Kategori anda: Remaja")
elif umur >= 18 and umur <= 59:
    print("Kategori anda: Dewasa")
elif umur >= 60:
    print("Kategori anda: Lansia")
print(" ")
print("Sekian Terimakasih")