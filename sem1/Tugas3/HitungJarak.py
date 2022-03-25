# Program HitungJarak
# Spesifikasi Program : Program ini menerima input berupa kecepatan dan waktu, lalu memberikan output berupa jarak tempuh

# KAMUS
# kecepatan, waktu, jarak : int

# ALGORITMA
# Menerima input besar kecepatan
kecepatan = int(input("Kecepatan(m/s): "))
# Minta input waktu
waktu = int(input("Waktu(s): "))
# Hitung jarak tempuh
jarak = kecepatan*waktu
# Berikan jarak tempuh
print(f"Jarak(m): {jarak}")