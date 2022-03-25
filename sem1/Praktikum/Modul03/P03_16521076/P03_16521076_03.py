# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 03/11/2021
# Deskripsi : Program menghitung banyak kemunculan sebuah string sebagai sebuah substring pada string lain. 
#             Diasumsikan string yang dimasukkan hanya terdiri dari huruf kecil (a-z), dan string 1 tidak lebih panjang dari string 2.

# KAMUS
# L1, L2, x, i : int
# S1, S2: string / array of char

# ALGORITMA
# Minta penngguna memasukkan panjang string 1 dan string 1
L1 = int(input("Masukkan panjang string 1: "))
S1 = input("Masukkan string 1: ")
# Minta pengguna memasukkan panjjang string 2 dan string 2
L2 = int(input("Masukkan panjang string 2: "))
S2 = input("Masukkan string 2: ")
# Cek jumlah string 1 di dalam string 2
x = 0
for i in range(L2 - L1 + 1):
    if S2[i:i+L1] == S1:
        x += 1
print("String 1 muncul sebanyak", x, "kali") 