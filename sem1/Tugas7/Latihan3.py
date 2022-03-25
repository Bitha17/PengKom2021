# Program NilaiTerkecil
# Deskripsi Program : Program mencari nilai terkecil dari array T.

# KAMUS
#   N : int
#   T : array [0..N-1] of integer
#   i : int (index)
#   min : int
#   CONTOH
#       Misalkan N = 5
#       Misalkan T = [0, 2, -1, 2, 4]

# ALGORITMA
# Assign N sebagai ukuran T
N = int(input("Ukuran array: "))
# Misalkan N = 5

# Deklarasi array T
T = ['0' for i in range(N)]

# Mengisi array dari pembacaan nilai dari keyboard
for i in range(0, N):
    T[i] = int(input("Angka ke-["+str(i+1)+"]: "))
# Misalkan T = [0, 2, -1, 2, 4]

# Mencari nilai minimum
min = T[0]  # inisiasi min dengan elemen pertama
# Pencarian dimulai dari elemen ke-2
for i in range(1, N):
    # jika ada elemen < min, ganti nilai min
    if T[i] < min:
        min = T[i]

# Cetak nilai terkecil
print("Nilai terkecil = " + str(min))
# Jawaban yang diekspektasikan : "Nilai terkecil = -1"