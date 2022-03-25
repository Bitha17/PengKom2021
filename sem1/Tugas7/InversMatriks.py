# Program InversMatriks
# Deskripsi Program : Program menginvers matriks dengan menggunakan Eliminasi Gauss-Jordan

# KAMUS
#   A, I : matriks integer
#   AI, A1 : matriks float
#   i, j, NKol, NBrs, k, l : integer
#   a : float
#   b : array [0..NBrs-1] float

# ALGORITMA
# Inisiasi ukuran matriks A (jumlah baris = jumlah kolom)
NKol = NBrs = int(input("Jumlah baris/kolom matriks: "))

# Deklarasi matriks A
A = [[0 for j in range(NKol)] for i in range(NBrs)]

# Mengisi matriks ukuran NBrsxNKol
for i in range(NBrs):
    for j in range(NKol):
        A[i][j] = int(input("Elemen ke-["+str(i)+","+str(j)+"] = "))
# Misal A = [[3, 4, 5]
#            [1, 3, 7]
#            [2, 4, 7]]

# Deklarasi matriks I
I = [[0 for j in range(NKol)] for i in range(NBrs)]
for i in range(NBrs):
    for j in range(NKol):
        if i == j:
            I[i][j] = 1
        else:
            I[i][j] = 0

# Definisikan matriks AI
AI = [[0 for j in range(2 * NKol)] for i in range(NBrs)]
for i in range(NBrs):
    for j in range(2 * NKol):
        if j < NKol:
            AI[i][j] = A[i][j]
        elif NKol <= j < 2 * NKol:
            AI[i][j] = I[i][j - NKol]

# Inisiasi array b untuk digunakan dalam pengolahan matriks
b = [0 for k in range(NBrs)]

# Melakukan eliminasi Gauss-Jordan
for i in range(NBrs):
    a = AI[i][i]
    # Normalisasi baris yang akan menjadi pivot
    for j in range(2 * NKol):
        AI[i][j] = AI[i][j] / a
    # Eliminasi baris-baris lainnya dengan menggunakan pivot
    for k in range(NBrs):
        if k != i:
            b[k] = float(AI[k][i])
            for l in range(2 * NKol):
                AI[k][l] = AI[k][l] - b[k] * AI[i][l]

# Definisikan matriks invers (A1)
A1 = [[0 for j in range(NKol)] for i in range(NBrs)]
for i in range(NBrs):
    for j in range(NKol):
        A1[i][j] = AI[i][j + NKol]

# Mencetak matriks baru ke layar
for i in range(NBrs):
    for j in range(NKol):
        print(str(A1[i][j])+" ", end='')  # print tanpa enter
    print()  # print enter

# Jawaban yang diekspektasikan :
#   2.333333333333332 2.666666666666665 -4.333333333333331 
#   -2.333333333333333 -3.6666666666666656 5.333333333333332
#   0.6666666666666665 1.3333333333333333 -1.6666666666666665