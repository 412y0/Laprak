# PENUGASAN

## Mendeklarasikan Program
# tipe data: string
data_string = "Aryo Kusumo Priambodo"
print("Nama : ", data_string)
print(type(data_string))

# tipe data: integer
data_integer = "18 tahun"
print("Umur : ", data_integer)
print(type(data_integer))

#tipe data: float
data_float = "115.55 kg"
print("Berat Badan : ", data_float)
print(type(data_float))

print(" ")

## MENGKONVERSI TIPE DATA
# INTEGER ke FLOAT DAN STRING
print("INTEGER KE FLOAT DAN STRING")
data_int = 89
data_float = float(data_int)
data_str = str(data_int)
print(float(data_int))
print(str(data_int))

print(" ")

# FLOAT KE INTEGER
print("FLOAT KE INTEGER")
data_float = 45.67
data_int = int(data_float)
print(int(data_float))

print(" ")

# STRING KE INTEGER
print("STRING KE INTEGER")
data_str = "123"
data_integer = int(data_str)
print(int(data_str))

print(" ")

## MENGINPUT DATA USER
print("MENGINPUT DATA USER")
data1 = str(input("Nama: "))
data2 = int(input("Umur: "))
data3 = float(input("TB: "))

print("Nama saya: ", data1, type(data1))
print("Umur saya: ", data2, type(data2))
print("Tb saya: ", data3, type(data3))