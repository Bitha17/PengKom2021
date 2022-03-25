def kel(A, i, j):
    kel = 0
    if (i > 0 and A[i - 1][j]):
        kel+= 1
    if (j > 0 and A[i][j - 1]):
        kel+= 1
    if (i < B-1 and A[i + 1][j]):
        kel+= 1
    if (j < K-1 and A[i][j + 1]):
        kel+= 1
    return kel

B = int(input("Masukkan nilai brs: "))
K = int(input("Masukkan nilai klm: "))
# Deklarasi matriks grid
grid = [[0 for j in range(K)] for i in range(B)]
# Mengisi grid
for i in range(B):
    for j in range(K):
        grid[i][j] = int(input("Masukkan nilai petak baris "+str(i+1)+" kolom "+str(j+1)+": "))

keliling = 0
for i in range(B):
    for j in range(K):
        if grid[i][j] == 1:
            keliling += 4 - kel(grid, i, j)

print(keliling)