##MEMBUAT FUNGSi
def hello_world () :
    print("hello world")
    print("Kepada Budi")
    print("Dan juga kepada Handoko")

hello_world()
print("\n")

##FUNGSI DENGAN ARGUMEN
print("FUNGSI DENGAN ARGUMEN")
def hello_world(nama):
    print(f"Selamat datang di Dunia, {nama}")

hello_world("Janitra")
print(" ")

def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(4, 5)

def say_hi (list_peserta) :
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Selamat datang {peserta}")

    kumpulan_mahasiswa = ["Beni", "Tono", "Joko"]

    say_hi (kumpulan_mahasiswa)
print("\n")

##FUNGSI DENGAN RETURN
print("FUNGSI DENGAN RETURN")

def kuadrat(input_angka):
    output_kuadrat = input_angka ** 2
    return output_kuadrat

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

def fungsi_tambah(angka_1, angka_2):
    return angka_1 + angka_2

a = fungsi_tambah(10, 8)
print(a)

def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2   
    kali = angka_1 * angka_2   
    bagi = angka_1 / angka_2 

    return tambah,kurang,kali,bagi
k,l,m,n = operasi_matematika(9,5) 

print(f"Hasil tambah = {k}") 
print(f"Hasil kurang = {l}") 
print(f"Hasil kali = {m}") 
print(f"Hasil bagi = {n}")
print("\n")

##DEFAULT ARGUMEN FUNGSI
print("DEFAULT ARGUMEN FUNGSI")
print("Contoh 1")
def say_hello(nama = "Ojul"):
    print(f"Hello {nama}")

say_hello("Ucup")
say_hello()
print(" ")

print("Contoh 2")
def sapa_dia(nama, pesan = "Apa kabar?"):
    print(f"hai {nama}, {pesan}")

sapa_dia("Nanda", "Selamat pagi")
sapa_dia("Budi")
print(" ")

print("Contoh 3")
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2, 4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)
print(" ")

print("Contoh 4")
def faktorial(input_1=1,input_2=2,input_3=3,input_4=4):  
    hasil = input_1 * input_2 * input_3 * input_4   
    return hasil  

print(faktorial()) 
print(faktorial(input_3 = 10))
print("\n")

##LATIHAN
print("LATIHAN")
print("Buatlah program dengan input dan fungsi untuk menghitung: ")
print(" a. Luas persegi panjang")
print(" b. Volume persegi panjang")
print(" c. Luas lingkaran")
print(" d. Volume bola")
print("JAWAB:")
print("\n")
print(" a. Luas persegi panjang")
def luaspersegipanjang (panjang, lebar):
    luas = panjang * lebar
    print(f"Luasnya: {luas}")
    return luas
    
panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))

luaspersegipanjang(panjang, lebar)
print(" ")

print(" b. Volume persegi panjang")
def volumepersegipanjang(panjang, lebar, tinggi):
    volume = panjang*lebar*tinggi
    print(f"Volumenya adalah: {volume}")

panjang = float(input("panjang: "))
lebar = float(input("lebar: "))
tinggi = float(input("tinggi: "))

volumepersegipanjang(panjang, lebar, tinggi)
print(" ")

print(" c. Luas lingkaran")
def luaslingkaran(phi, jari):
    luasling = phi * jari**2
    print(f"Luas lingkarannya: {luasling}")

phi = 22/7
jari = float(input("Jari-jarinya: "))

luaslingkaran(phi, jari)
print(" ")

print(" d. Volume Bola")
def volumebola(v, phi, jari):
    volume = v*phi*jari**3
    print(f"Volume dari bola adalah: {volume}")

v = 4/3
phi = 22/7
jari = float(input("Jari-jarinya: "))

volumebola(v, phi, jari)