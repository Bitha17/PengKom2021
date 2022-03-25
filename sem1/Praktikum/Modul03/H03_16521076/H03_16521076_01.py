# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 01/11/2021
# Deskripsi : Program menerima N buah bilangan dan menuliskan kembali bilangan tersebut, namun terbalik

# KAMUS
# N : int
# A : array [0..N] integer

# ALGORITMA
# Minta pengguna memasukkan N
N = int(input("Masukkan N: "))
# Deklarasi array A
A = [0 for i in range(N)]
# Minta pengguna memasukkan N buah bilangan
for i in range(0, N):
    A[i] = int(input())
# Cetak bilangan dalam urutan terbalik
print("Hasil dibalik:")
for i in range(N-1, -1, -1):
    print(A[i])