# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 17/11/2021
# Deskripsi : Program menerima input grid baris x kolom yang merepresentasikan peta dimana grid[i][j] = 1 menyatakan daratan, 
#             dan grid[i][j] = 0 menyatakan lautan. Program menentukan keliling dari pulau pada peta

# KAMUS
# B, K, i, j, keliling : int
# grid : matriks integer

# ALGORITMA
# Minta pengguna memasukkan nilai baris dan kolom
B = int(input("Masukkan nilai brs: "))
K = int(input("Masukkan nilai klm: "))
# Deklarasi matriks grid
grid = [[0 for j in range(K)] for i in range(B)]
# Mengisi grid
for i in range(B):
    for j in range(K):
        grid[i][j] = int(input("Masukkan nilai petak baris "+str(i+1)+" kolom "+str(j+1)+": "))

# Menghitung keliling pulau
keliling = 0
if B == 1 and K == 1:
    keliling = 4
elif B > 1 and K > 1:
    for i in range(1, B-1):
        for j in range(1, K-1):
            if grid[i][j] == 1:
                keliling += 4  
                if grid[i-1][j] == 1:
                    keliling -= 1
                if grid[i+1][j] == 1:
                    keliling -= 1
                if grid[i][j-1] == 1:
                    keliling -= 1
                if grid[i][j+1] == 1:
                    keliling -= 1
        if grid[i][0] == 1:
            keliling += 4  
            if grid[i-1][0] == 1:
                keliling -= 1
            if grid[i+1][0] == 1:
                keliling -= 1
            if grid[i][1] == 1:
                keliling -= 1
        if grid[i][K-1] == 1:
            keliling += 4  
            if grid[i-1][K-1] == 1:
                keliling -= 1
            if grid[i+1][K-1] == 1:
                keliling -= 1
            if grid[i][K-2] == 1:
                keliling -= 1
    for j in range(1, K-1):
        if grid[0][j] == 1:
            keliling += 4  
            if grid[1][j] == 1:
                keliling -= 1
            if grid[0][j-1] == 1:
                keliling -= 1
            if grid[0][j+1] == 1:
                keliling -= 1
        if grid[B-1][j] == 1:
            keliling += 4  
            if grid[B-2][j] == 1:
                keliling -= 1
            if grid[B-1][j-1] == 1:
                keliling -= 1
            if grid[B-1][j+1] == 1:
                keliling -= 1
    if grid[0][0] == 1:
        keliling += 4
        if grid[0][1] == 1:
            keliling -= 1
        if grid[1][0] == 1:
            keliling -= 1
    if grid[B-1][0] == 1:
        keliling += 4
        if grid[B-1][1] == 1:
            keliling -= 1
        if grid[B-2][0] == 1:
            keliling -= 1
    if grid[0][K-1] == 1:
        keliling += 4
        if grid[0][K-2] == 1:
            keliling -= 1
        if grid[1][K-1] == 1:
            keliling -= 1
    if grid[B-1][K-1] == 1:
        keliling += 4
        if grid[B-1][K-2] == 1:
            keliling -= 1
        if grid[B-2][K-1] == 1:
            keliling -= 1
# Print hasil
print("Keliling pulau tersebut adalah ", str(keliling))