# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 15/11/2021
# Deskripsi : Program menerima N dan M, lalu membaca matriks A berukuran N×M, 
#             dan menulsikan berapa banyak bilangan positif di dalam matriks 
#             beserta menuliskan isi matriks itu sendiri

# KAMUS
# N, M, positif, i, j: int
# A : matriks integer

# ALGORITMA
# Input ukuran matriks
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))
# Deklarasi matriks A
A = [[0 for j in range(M)] for i in range(N)]
# Mengisi matriks ukuran NxM, dan menghitung jumlah elemen positif
positif = 0
for i in range(N):
    for j in range(M):
        A[i][j] = int(input(f"Masukkan nilai A[{i+1}][{j+1}]: "))
        if A[i][j] > 0:
            positif += 1
# Menuliskan jumlah elemen positif
print(f"Ada {positif} bilangan positif di matriks.")
# Mencetak matriks ke layar
for i in range(N):
    for j in range(M):
        print(str(A[i][j])+" ", end='')  # print tanpa enter
    print()  # print enter