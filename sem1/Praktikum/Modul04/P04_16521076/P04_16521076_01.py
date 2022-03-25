# NIM/Nama  : 16521076 / Tabitha Permalla
# Tanggal   : 17/11/2021
# Deskripsi : Program menerima input panjang sisi kubus dan tinggi limas, 
#             serta memberi output volume rumah tersebut.
#             Diasumsikan input yang dimasukkan adalah bilangan bulat positif, dan satuan panjang dalam meter.

# KAMUS
# vol1, vol2 : fungsi (input: int, output: float)
# s, t: int

# ALGORITMA
# Definisikan fungsi volume kubus dan volume limas
def vol1(s):
    return s**3
def vol2(s, t):
    return (s**2) * t / 3

# Minta pengguna memasukkan panjang sisi kubusdan tinggi limas
s = int(input("Masukkan panjang sisi kubus: "))
t = int(input("Masukkan tinggi limas: "))
# Print hasil
print("Volume rumah yang terbentuk adalah " + str(vol1(s) + vol2(s,t)) + " meter kubik.")