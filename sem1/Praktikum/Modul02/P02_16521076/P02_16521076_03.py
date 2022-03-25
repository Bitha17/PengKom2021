# NIM / Nama : 16521076 / Tabitha Permalla
# Tanggal : 27/10/2021
# Deskripsi : Program menerima bilangan bulat N yang lebih besar dari 1. 
#             Bilangan tersebut dibagi menjadi jumlah dari k bilangan bulat positif, dimana k >= 2.
#             Program kemudian menentukan nilai maksimal dari perkalian bilangan-bilangan tersebut.

# KAMUS

# ALGORITMA
# Minta pengguna memasukkan bilangan N
N = int(input("Masukkan bilangan N: "))
maks = 0  # Inisasi nilai maks ke 0
for i in range(2, N+1):
    n = N  # inisiasi nilai n sementara
    m = 1  # inisiasi nilai m ke 1
    x = n // i
    while n > 1:
        if n >= x:
            n -= x
            m *= x
        else:
            m *= n
    if m > maks:
        maks = m

print("Nilai maksimalnya adalah", maks)