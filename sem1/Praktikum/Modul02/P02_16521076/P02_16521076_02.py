# NIM / Nama : 16521076 / Tabitha Permalla
# Tanggal : 27/10/2021
# Deskripsi : Program menerima input volume x, y, dan z. Kemudian program menghitung berapa kali ember x dan ember y perlu diisi penuh untuk kemudian mengisi kolam z

# KAMUS
# x, y, z, m, n : int

# ALGORITMA
# Minta pengguna memasukkan volume x, y, dan z
x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))
z = int(input("Masukkan z: "))

m = 0 # jumlah ember x
n = 0 # jumlah ember y
while z % y != 0 and z >= x:  # kurangi z dengan x sampai ditemukan nilai z yang habis dibagi y
    z = z - x
    m += 1
while z >= y:  # kurangi z dengan y sampai bernilai 0
    z = z - y
    n += 1

if z == 0:
    print(m, "kali ember x,", n, "kali ember y")
else:  # jika z tidak bisa dikurangi hingga 0
    print("Tidak mungkin")