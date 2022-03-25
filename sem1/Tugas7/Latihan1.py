# Program PengalianElemenArray
# Deskripsi Program : Program mengalikan elemen-elemen array T dengan sebuah integer X

# KAMUS
#   T : array [0..19] integer
#   X : int (faktor elemen)
#   i : int (index)
#   CONTOH
#       Misalkan T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#       Misalkan X = 2

# ALGORITMA
# Deklarasi array T
T = [0 for i in range(20)]

# Mengisi array dari pembacaan nilai dari keyboard
for i in range(0, 20):
    T[i] = int(input("Angka ke-["+str(i+1)+"] : "))
# Misalkan T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Input faktor pengali (X)
X = int(input("X = "))
# Misalkan X = 2

# Mengalikan semua elemen array T dengan faktor X
for i in range(0, 20):
    T[i] = T[i] * X

# Mencetak array baru ke layar
print(T)
# Jawaban yang diekspektasikan : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]