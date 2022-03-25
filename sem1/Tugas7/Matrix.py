# Program MatriksXKonstanta
# Deskripsi Program : Program membaca sebuah matriks M dengan elemen integer.
#                     Program kemudian menerima input sebuah nilai integer X.
#                     Program mengalikan setiap elemen matriks M dengan X, lalu menuliskannya di layar.

# KAMUS
#   M : matriks integer
#   NBrs, NKol : int (ukuran baris & kolom)
#   i, j : int (indeks)
#   X : int (faktor elemen)

# ALGORITMA
# Input ukuran matriks M
NBrs = int(input("Jumlah baris matriks: "))
NKol = int(input("Jumlah kolom matriks: "))

# Deklarasi matriks M
M = [[0 for j in range(NKol)] for i in range(NBrs)]

# Mengisi matriks ukuran NBrsxNKol
for i in range(NBrs):
    for j in range(NKol):
        M[i][j] = int(input("Elemen ke-["+str(i)+","+str(j)+"] = "))
print(M)
# Input X
X = int(input("Faktor pengali = "))

# Mengalikan elemen M
for i in range(NBrs):
    for j in range(NKol):
        M[i][j] = M[i][j] * X

# Mencetak matriks baru ke layar
for i in range(NBrs):
    for j in range(NKol):
        print(str(M[i][j])+" ", end='')  # print tanpa enter
    print()  # print enter