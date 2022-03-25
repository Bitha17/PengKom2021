# NIM / Nama : 16521076 / Tabitha Permalla
# Tanggal : 27/10/2021
# Deskripsi : Program menerima input N dan menuliskan banyak langka untuk mengubah N menjadi 1

# KAMUS
# N, i : int

# ALGORITMA
# Minta pengguna memasukkan nilai N
N = int(input("Masukkan bilangan N: "))
# Inisiasi nilai langkah ke 0
langkah = 0
# Lakukan pengulangan sampai N menjadi 1
while N != 1:
    if N % 2 != 0: # Jika N ganjil, N dikurangi 1
        N = N - 1
        langkah += 1
    else:  # N % 2 == 0 (Jika N genap, N dibagi 2)
        N = N / 2
        langkah += 1
print("Banyak langkah yang diperlukan adalah", langkah)
