# Program membaca input 2 buah bilangan riil, yaitu  s0 (jarak awal) dan t (waktu tempuh). 
# Nilai a (akselerasi) ditentukan (konstanta), yaitu a = 10-2, demikian pula nilai  v (kecepatan), yaitu v = 10. 
# Selanjutnya program menuliskan ke layar hasil perhitungan jarak tempuh st. Diasumsikan: s0 >= 0 dan t >= 0.

# KAMUS
# a, v : int
# s0, t : float
# st : prosedur

# ALGORITMA
# Tetapkan nilai a dan v
a = 0.01
v = 10
# Buat fungsi untuk mencari st
def st(s0, t):
    print("Jarak tempuh (st): " + str(0.5*a*t**2 + v*t + s0))
# Minta pengguna memasukkan nilai s0 dan t
s0 = float(input("Masukkan jarak awal (s0): "))
t = float(input("Masukkan waktu tempuh (t): "))
# print hasil
st(s0, t)