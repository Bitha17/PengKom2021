# Program KelulusanMahasiswa
# Deskripsi Program : Program menerima data nilai 50 mahasiswa dalam bentuk indeks huruf dan disimpan dalam array of character.
#                     Program kemudian menentukan jumlah mahasiswa yang lulus dan hasilnya dicetak ke layar.
#                     Program ditulis dengan asumsi pengguna hanya akan memasukan nilai 'A', 'B', 'C', 'D', atau 'E'.

# KAMUS
#   Nilai : array [0,49] character
#   i : int (indeks)
#   Lulus : int
#   CONTOH
#       Misalkan Nilai = [A, B, C, D, E, E, D, C, B, A, A, A, B, B, C, C, D, D, E, E, 
#                         A, A, A, B, B, B, C, C, C, D, D, D, E, E, E, A, A, A, A, B,
#                         B, B, B, C, C, C, C, D, D, D]

# ALGORITMA
# Deklarasi array Nilai
Nilai = ['a' for i in range(50)]

# Mengisi array dari pembacaan nilai dari keyboard
for i in range(0, 50):
    Nilai[i] = input("Nilai ke-["+str(i+1)+"] : ")
# Misalkan Nilai = [A, B, C, D, E, E, D, C, B, A, A, A, B, B, C, C, D, D, E, E, 
#                   A, A, A, B, B, B, C, C, C, D, D, D, E, E, E, A, A, A, A, B,
#                   B, B, B, C, C, C, C, D, D, D]

# Menentukan jumlah mahasiswa yang lulus
Lulus = 0
for (i) in range(0, 50):
    if Nilai[i] == 'A' or Nilai[i] == 'B' or Nilai[i] == 'C':
        Lulus = Lulus + 1

# Mencetak jumlah mahasiswa yang lulus
print("Jumlah mahasiwa yang lulus : " + str(Lulus))
# Jawaban yang diekspektasikan : "Jumlah mahasiswa yang lulus : 33"