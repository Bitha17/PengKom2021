# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 03/11/2021
# Deskripsi : Program menerima bilangan bulat positif N, kemudian string dengan panjang N.
#             Kemudian program menentukan berapa huruf vkal dan huruf konsonan dari string tersebut. 
#             Diasumsikan string yang dimasukkan hanya berisi alfabet daram huruf kecil dan spasi.

# KAMUS
# N, vokal, konsonan, i : int
# s : string / array of char

# ALGORITMA
# Minta pengguna memasukkan N
N = int(input("Masukkan N: "))
# Minta pengguna memasukkan string
s = input("Masukkan string: ")
# Hitung huruf vokal dan konsonan
# Inisiasi nilai vokal dan konsonan ke 0
vokal = 0
konsonan = 0
for i in range(N):
    # Menghitung huruf vokal
    if s[i] == 'a' or s[i] == 'i' or s[i] == 'u' or s[i] == 'e' or s[i] == 'o':
        vokal += 1
    elif s[i] == ' ':  # Skip perhitungan untuk spasi
        vokal = vokal
    # Menghitung huruf konsonan
    else:
        konsonan += 1
# Print hasil
print("Terdapat", vokal, "huruf vokal dan", konsonan, "huruf konsonan.")