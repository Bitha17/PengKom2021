# NIM / Nama : 16521076 / Tabitha Permalla
# Tanggal    : 22 Oktober 2021
# Deskripsi  : Program menerima bilangan N dan menuliskan 1 sampai N dalam satu baris.

# KAMUS
# N : int

# ALGORITMA
# Minta pengguna memasukkan nilai N
N = int(input("Masukkan N: "))
for i in range(N):  # Lakukan pengulangan sebanyak N kali
    # Print angka 1 sampai N tanpa garis baru
    print(i+1, " ", end="") 