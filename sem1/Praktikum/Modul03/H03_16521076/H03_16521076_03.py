# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 01/11/2021
# Deskripsi : Program menerima sebuah string dan menuliskan apakah string tersebut palindrom. 
#             Diasumsikan string hanya berisi huruf kecil (a-z)

# KAMUS
# n, i : int
# A : string / array pf char
# palindrom : boolean

# ALGORITMA
# Minta pengguna memasukkan panjang string dan string
n = int(input("Masukkan panjang string: "))
A = input("Masukkan string: ")
# Cek apakah string merupakan palindrom
palindrom = True
for i in range(0, n//2):
    if A[i] != A[n-1-i]:
        palindrom = False
# Print apakah string merupakan palindrom atau bukan
if palindrom:
    print(A, "adalah palindrom")
else:
    print(A, "bukan palindrom")