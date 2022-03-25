# NIM / Nama : 16521076 / Tabitha Permalla
# Tanggal    : 22 Oktober 2021
# Deskripsi  : Program menerima bilangan X dan menentukan apakah X adalah bilangan prima

# KAMUS
# X : int

# ALGORITMA
# Minta pengguna memasukkan nilai X
X = int(input("Masukkan X: "))

if X > 1:  # Bilangan prima pasti diatas 1
    for i in range(2,X):
        if X % i == 0:  # Bilangan yang habis dibagi bilangan selain 1 dan dirinya sendiri bukan bilangan prima
            print(X, "bukan bilangan prima")
            break
    else:  # Bilangan tidak habis dibagi dengan bilangan lain, sehingga adalah bilangan prima
        print(X, "adalah bilangan prima")
else:  # Bilangan yang <= 1 bukan bilangan prima
    print(X, "bukan bilangan prima")