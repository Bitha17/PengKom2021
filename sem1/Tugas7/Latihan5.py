# Program PenjumlahanVektor
# Deskripsi Program : Program menerima input 2 buah vektor, masing-masing terdiri dari 5 elemen.
#                     Kemudian Program menjumlahkan kedua vektor tersebut dan mencetaknya ke layar.

# KAMUS
#   U, V, W : array [0..4] of integer
#   i : int (indeks)
#   CONTOH
#       Misalkan U = [1, 2, 3, 4, 5]
#       Misalkan V = [6, 7, 8, 9, 10]

# ALGORITMA
# Deklarasi array U, V, dan W
U = [0 for i in range(5)]
V = [0 for i in range(5)]
W = [0 for i in range(5)]

# Mengisi array U dan V dari pembacaan nilai di keyboard
for i in range(0, 5):
    U[i] = int(input("U [" + str(i)+"]: "))
#   Misalkan U = [1, 2, 3, 4, 5]
for i in range(0, 5):
    V[i] = int(input("V [" + str(i)+"]: "))
#   Misalkan V = [6, 7, 8, 9, 10]

# Melakukan penjumlahan elemen-elemen array
for i in range(0, 5):
    W[i] = U[i] + V[i]

# Mencetak hasil
print(W)
# Hasil yang diekspektasikan : [7, 9, 11, 13, 15]