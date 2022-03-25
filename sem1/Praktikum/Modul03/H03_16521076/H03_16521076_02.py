# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 01/11/2021
# Deskripsi : Program memeriksa apakah array B merupakan anagram dari array A. 
#             Diasumsikan elemen pada array A dan B maksimal 10. (Berkisar dari angka 1 sampai 10)

# KAMUS
# NA, NB, i, j : int
# A, countA, B, countB : array of integer
# anagram : boolean

# ALGORITMA
# Minta pengguna memasukkan banyak elemen A
NA = int(input("Masukkan banyaknya elemen A: "))
# Deklarasi array A
A = [0 for i in range(NA)]
# Buat tabel frekuensi untuk array A
countA = [0 for i in range(10)]
# Minta pengguna memasukkan elemen-elemen A
for i in range(0, NA):
    A[i] = int(input("Masukkan elemen A ke-"+str(i+1)+": "))
    for j in range(10):
        if A[i] == j + 1:
            countA[j] += 1
# Minta pengguna memasukkan banyak elemen B
NB = int(input("Masukkan banyaknya elemen B: "))
# Deklarasi array B
B = [0 for i in range(NB)]
# Buat tabel frekuensi untuk array B
countB = [0 for i in range(10)]
# Minta pengguna memasukkan elemen-elemen B
for i in range(0, NB):
    B[i] = int(input("Masukkan elemen B ke-"+str(i+1)+": "))
    for j in range(10):
        if B[i] == j + 1:
            countB[j] += 1
# Periksa apakah array B merupakan anagram dari array A
anagram = True
for i in range(10):
    if countA[i] < countB[i]:
        anagram = False
# Print pernyataan apakah B merupakan anagram dari A atau bukan
if anagram:
    print("B adalah anagram dari A")
else:
    print("B bukan anagram dari A")


