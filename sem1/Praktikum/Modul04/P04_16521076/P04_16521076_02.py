# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 17/11/2021
# Deskripsi : Program menerima input panjang string dan string itu sendiri.
#             Kemudian program memberi output jumlah kata berbeda yang dapat dibentuk. 
#             Diasumsikan string yang dimasukkan adalah huruf kecil a-z

# KAMUS
# fak : fungsi (input: int, output: int)
# n, i , a : int
# kata : float
# A : array

# ALGORITMA
# Fungsi faktorial
def fak(a):
    b = 1
    if a >= 1:
        for i in range(a):
            b *= (i+1)
    return b

# Minta pengguna memasukkan panjang string dan string
n = int(input("Masukkan panjang string: "))
S = input("Masukkan string: ")
# Deklarasi array untuk jumlah huruf a-z
A = [0 for i in range(26)]
# Hitung jumlah huruf yang sama dalam string
for i in range(n):
    a = ord(S[i]) - ord('a')
    A[a] += 1
# Hitung jumlah kata yang dapat dibentuk
kata = fak(n)
for i in range(26):
    kata /= fak(A[i])
# Print output
print("String tersebut dapat membentuk", str(int(kata)), "kata berbeda.")