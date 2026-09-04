## LATIHAN
P = 12
L = 5
T = 8
print("Panjang = 12")
print("Lebar   = 5")
print("Luas    = 8")
print("a. Hitunglah luas, volume, dan keliling dari bangunan tersebut!")
print("b. Apakah luas bangunan tersebut lebih luas dari 50?")
print("c. Apakah volume tersebut bernilai 480?")
print(" ")
print("JAWABAN:")
#LUAS
print("a. Hitunglah luas, volume, dan keliling dari bangunan tersebut!")
print("LUAS DARI BANGUNAN TERSEBUT")
hasil = 2 * (12*5 + 12*8 + 5*8)
print(2, "*", (12*5 + 12*8 + 5*8), "=", hasil)
print(" ")
#VOLUME
print("VOLUME DARI BANGUNAN TERSEBUT")
hasil = 12 * 5 * 8
print(12, "*", 5, "*", 8, "=", hasil)
print(" ")
#KELILING
print("KELILING DARI BANGUNAN TERRSEBUT")
hasil = 4 * (12 + 5 + 8)
print(4, "*", "(",12,"+",5,"+",8,")","=", hasil)
print(" ")
#KOMPERASI
print("b. Apakah luas bangunan tersebut lebih luas dari 50?")
m = 2*(12*5 + 12*8 + 5*8)
n = 50
hasil = m > n 
print(m, ">", n, "=", hasil)
print(" ")
#VOLUME APAKAH BERNILAI 480?
print("c. Apakah volume tersebut bernilai 480?")
k = 480
j = 12*5*8
hasil = k == j 
print(k, '==', j, '=', hasil)