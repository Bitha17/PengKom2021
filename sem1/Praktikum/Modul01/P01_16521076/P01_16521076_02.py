# NIM/Nama  : 16521076/Tabitha Permalla
# Tanggal   : 06/10/2021
# Deskripsi : Program menentukan kelas dan harga kursi pesawat yang dipilih pengguna.

# KAMUS
# N : string (Nomor Kursi)
# P : string (Posisi Kursi)

# ALGORITMA
N = input("Tentukan Nomor Kursi: ")
P = input("Tentukan Posisi Kursi: ")

if 0 < int(N) < 21 or 50 < int(N) < 61:
    if P == 'A' or P == 'F':
        print("Tuan Kil memilih kursi Hot Seat dengan harga 1600000.") 
    elif P == 'B' or P == 'E':
        print("Tuan Kil memilih kursi Hot Seat dengan harga 1550000.")
    elif P == 'C' or P == 'D':
        print("Tuan Kil memilih kursi Hot Seat dengan harga 1500000.")
    else:
        print("Tidak ada kursi yang sesuai.")
elif 20 < int(N) < 51 or 60 < int(N) < 101:
    if P == 'A' or P == 'F':
        print("Tuan Kil memilih kursi Reguler dengan harga 1000000.") 
    elif P == 'B' or P == 'E':
        print("Tuan Kil memilih kursi Reguler dengan harga 950000.")
    elif P == 'C' or P == 'D':
        print("Tuan Kil memilih kursi Reguler dengan harga 900000.")
    else:
        print("Tidak ada kursi yang sesuai.")
else:
    print("Tidak ada kursi yang sesuai.")