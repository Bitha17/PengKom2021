# Program Menghitung Hari
# Spesifikasi Program : Program menghitung jumlah hari dalam rentang tanggal pada tahun yang sama.

# KAMUS
# y, d1, m1, d2, m2, D1, D2 : int
# M, M1 : list/array

# AlGORITMA
# Minta angka tahun
y = int(input("tahun: "))
# Minta rentang tanggal
d1 = int(input("tanggal_1: "))
m1 = int(input("bulan_1: "))
d2 = int(input("tanggal_2: "))
m2 = int(input("bulan_2: "))

# Buat list/array jumlah hari sampai bulan ke-n
M = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
M1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

# Lakukan perhitungan
if y % 4 != 0:
    D1 = int(M[m1 - 1]) + d1
    D2 = int(M[m2 - 1]) + d2
else:
    D1 = int(M1[m1 - 1]) + d1
    D2 = int(M1[m2 - 1]) + d2
# Berikan output
print(f"Jumlah hari: {D2-D1}")