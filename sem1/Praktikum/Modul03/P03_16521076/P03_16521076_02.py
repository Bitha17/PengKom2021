# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 03/11/2021
# Deskripsi : Program menerima banyak lampu, berapa kali Tuan Kil menekan tombol, dan tombol yang ditekan setiap kali. 
#             Kemudian program menuliskan keadaan akhir lampu

# KAMUS
# N, x, i, j, y: int
# L : array of integer

# ALGORITMA
# Minta pengguna memasukkan banyak lampu
N = int(input("Masukkan banyak lampu: "))
# Minta pengguna memasukkan berapa kali Tuan Kil menekan tombol
x = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))
# Buat array untuk kondisi awal lampu
L = [0 for i in range(N)]
# Minta pengguna memasukkan tombol yang ditekan, kemudian update kondisi lampu
for i in range(x):
    y = int(input("Tombol yang ditekan ke " +str(i+1)+ ": "))
    if y > 1 and y < N:
        for j in range(y - 2, y + 1):
            if L[j] == 0:
                L[j] = 1
            else:
                L[j] = 0
    elif y == 1:  # Jika tombol 1 ditekan
        for j in range(0, y + 1):
            if L[j] == 0:
                L[j] = 1
            else:
                L[j] = 0
    elif y == N:  # Jika tombol terakhir ditekan
        for j in range(y - 2, y):
            if L[j] == 0:
                L[j] = 1
            else:
                L[j] = 0
# Print hasil
print("Keadaan akhir rangkaian lampu adalah", end = ' ')
for i in range(N):
    print(L[i], end = '')