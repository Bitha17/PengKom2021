NBrs = int(input("Jumlah baris matriks: "))
NKol = int(input("Jumlah kolom matriks: "))

# Deklarasi matriks M
M = [[0 for j in range(NKol)] for i in range(NBrs)]

# Mengisi matriks ukuran NBrsxNKol
for i in range(NBrs):
    for j in range(NKol):
        M[i][j] = int(input("Elemen ke-["+str(i)+","+str(j)+"] = "))

segitiga = True

if NBrs != NKol:
    segitiga = False
else:
    for i in range(NBrs):
        for j in range(i, NKol):
            if M[i][j] == 0:
                segitiga = False
    for k in range(1, NBrs):
        for l in range(k):
            if M[k][l] != 0:
                segitiga = False
print(segitiga)