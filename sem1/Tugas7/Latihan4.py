# Program IndeksTerakhir
# Deskripsi Program : Program mencari indeks terakhir di mana X ditemukan di T.

# KAMUS
#   N : int
#   T : array [0..N-1] of integer
#   i : int (indeks)
#   X : int
#   found : bool; menentukan X sudah ditemukan/belum
#   CONTOH
#       Misalkan N = 5
#       Misalkan T = [3, -1, 3, 2, 5]
#       Misalkan X = 3


# ALGORITMA
# Assign N sebagai ukuran T
N = int(input("Ukuran array: "))
# Misalkan N = 5

# Deklarasi array T
T = ['0' for i in range(N)]
# Misalkan T = [3, -1, 3, 2, 5]

# Mengisi array dari pembacaan nilai dari keyboard
for i in range(0, N):
    T[i] = int(input("Angka ["+str(i)+"]: "))

# Membaca nilai yang dicari, yaitu X
X = int(input("Angka yang dicari: "))
# Misalkan X = 3

# Pencarian nilai X, dimulai dari belakang
i = N - 1
found = False  # found = False; X belum ditemukan
while (i >= 0 and found == False):
    if T[i] == X:
        found = True  # found = True; X sudah ditemukan
    else:
        i = i - 1   # hanya increment jika X belum ditemukan
# i < 0 atau found = True

# Cetak hasil
if (found == True):  # X ditemukan di T
    print(str(X) + " ditemukan di indeks ke-" + str(i))
else:  # found = False; X tidak ditemukan di T
    print(str(X) + " tidak ditemukan")
# Jawaban yang diekspektasikan : "3 ditemukan di indeks ke-2"