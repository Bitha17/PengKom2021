# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 15/11/2021
# Deskripsi : Program menerima masukan N 
#             dan menuliskan matriks segitiga pascal berukuran NxN

# KAMUS
# N, i, j, a, b: int
# A : matriks integer

# ALGORITMA
# Minta pengguna memasukkan N
N = int(input("Masukkan N: "))
# Deklarasi matriks A
A = [[0 for i in range(N)] for j in range(N)]
# Buat matriks segitiga paskal
for a in range(N):
    for b in range(N):
        # Semua nilai baris pertama dan nilai kolom pertma bernilai 1
        if a == 0 or b == 0:
            A[a][b] = 1
        # ELemen lainnya dari matriks adalah jumlah bilangan di atas dan kirinya
        else:
            A[a][b] = A[a-1][b] + A[a][b-1]
# Mencetak matriks ke layar
for i in range(N):
    for j in range(N):
        print(str(A[i][j])+" ", end='')  # print tanpa enter
    print()  # print enter