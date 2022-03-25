# NIM/Nama      : 16521076/Tabitha Permalla
# Tanggal       : 3 Oktober 2021
# Judul Program : Bilangan
# Deskripsi     : Program menentukan apakah sebuah bilangan adalah bilangan positif, negatif, atau nol. 
#                 Khusus untuk bilangan positif, dituliskan juga apakah ganjil atau genap.

# ALGORITMA
# Minta pengguna memasukkan angka
x = int(input("Masukkan X: "))

# Jika bilangan positif
if x > 0:
    if x % 2 == 0:
        print("X adalah bilangan positif genap")
    else:  # x % 2 != 0
        print("X adalah bilangan positif ganjil")
# Jika bilangan negatif
elif x < 0:
    print("X adalah bilangan negatif")
# Jika bilangan nol
else:  # x = 0
    print("X adalah bilangan nol")