# NIM/Nama  : 16521076/Tabitha Permalla
# Tanggal   : 06/10/2021
# Deskripsi : Program menerima input penghasilan Tuan Ric. Kemudian menghitung dan mencetak pajak yang harus dibayarkan Tuan Ric.

# KAMUS
# P : int (penghasilan)

# ALGORITMA
P = int(input("Masukkan penghasilan Tuan RIc: "))

if P < 50000000:
    print("Pajak yang harus dibayar Tuan Ric sebesar " + str(int(P*0.05)) + " rupiah.")
elif 50000000 <= P <= 249999999:
    print("Pajak yang harus dibayar Tuan Ric sebesar " + str(int(P*0.15)) + " rupiah.")
elif 250000000 <= P <= 499999999:
    print("Pajak yang harus dibayar Tuan Ric sebesar " + str(int(P*0.25)) + " rupiah.")
else:  # P > 499999999
    print("Pajak yang harus dibayar Tuan Ric sebesar " + str(int(P*0.3)) + " rupiah.")
