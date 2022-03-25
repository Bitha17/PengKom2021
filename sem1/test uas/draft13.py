print("Ukuran Matriks")
n = int(input("Baris: "))
m = int(input("Kolom: "))

M = [[0 for i in range(m)] for j in range(n)]

# Mengisi matriks
print("Masukkan matriks")
for i in range(n):
    for j in range(m):
        M[i][j] = int(input("Elemen [" +str(i)+ "," +str(j)+ "] = "))

# Minta masukan b dan k
b = int(input("Indeks baris dihapus: "))
k = int(input("Indeks kolom dihapus: "))

# Nilai rata-rata matriks M
sum = 0
for i in range(n):
    for j in range(m):
        sum += M[i][j]
mean = sum/(n*m)
print("Nilai rata-rata elemen matriks = " +str(mean))

M1 = [[0 for i in range(m-1)] for j in range(n-1)]
for i in range(n-1):
    for j in range(m-1):
        if i < b and j < k:
            M1[i][j] = M[i][j]
        elif i >= b and j < k:
            M1[i][j] = M[i+1][j]
        elif i >= b and j >= k:
            M1[i][j] = M[i+1][j+1]
        elif i < b and j >= k:
            M1[i][j] = M[i][j+1]

print("Submatriks")
for i in range(n-1):
    for j in range(m-1):
        print(str(M1[i][j])+" ", end='')  # print tanpa enter
    print()

# Nilai rata-rata matriks M1
sum = 0
for i in range(n-1):
    for j in range(m-1):
        sum += M1[i][j]
mean = sum/((n-1)*(m-1))
print("Nilai rata-rata elemen submatriks = " +str(mean))