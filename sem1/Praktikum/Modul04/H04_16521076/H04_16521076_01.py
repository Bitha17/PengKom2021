# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 15/11/2021
# Deskripsi : Program menerima input A dan B kemudian menuliskan semua nilai f(A) sampai f(B)
#             Diasumsikan nilai B selalu lebih besar dari A

# KAMUS
# f(x) : function
# A, B, x, f, i : int

# ALGORITMA
# Definisikan fungsi f(x)
def f(x):
    f = x**2 - 2*x + 5
    return f

# Main Program
# Minta pengguna memasukkan A dan B
A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))
for i in range(A, B+1):
    print(f"f({i}) = {f(i)}")
