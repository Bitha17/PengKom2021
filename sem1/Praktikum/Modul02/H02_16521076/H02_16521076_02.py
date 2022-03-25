# NIM / Nama : 16521076 / Tabitha Permalla
# Tanggal    : 22 Oktober 2021
# Deskripsi  : Program menerima bilangan N dan menuliskan bilangan 10^x terkecil yang lebih dari N

# KAMUS
# N, x : int

# ALGORITMA
# Minta pengguna memasukkan nilai N
N = int(input("Masukkan N: "))

x = 0  # Inisasi x = 0
while 10**x <= N:  # Pengecekan kondisi apabila 10^x <= N
    x += 1  # Perbaharui nilai x

# Print bilangan 10^x terkecil yang lebih besar dari N
print(10**x)