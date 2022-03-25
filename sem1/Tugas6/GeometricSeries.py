# Program Geometric Series
# Spesifikasi Program : Program menerima input a, r, dan n.
# Kemudian program akaan memberikan output apakah G bernilai konvergen, nilai G itu sendiri, dan nilai E(error) apabila G konvergen.

# KAMUS
# a, r, g, G, E : float
# n, i : int

# ALGORITMA
# Minta pengguna untuk memasukan nilai a, r, dan n
a = float(input("nilai a : "))
r = float(input("nilai r : "))
n = int(input("nilai n : "))

# Inisialisasi nilai G
G = 0
# Hitung nilai G
for i in range(1, n+1):
    g = a*(r**i)
    G = G + g

# Identifikasi apakah |r| < 1 atau |r| >= 1
if abs(r) < 1:
    # Berikan output "Nilai G konvergen" dan nilai G
    print("Nilai G konvergen")
    print("Nilai G : ", G)
    # Hitung nilai E dan berikan output nilai G
    E = (a/(1-r))-G
    print("Nilai E(error) : ", E)
else:  # abs(r) >= 1
    # Berikan output "Nilai G divergen" dan nilai E
    print("Nilai G divergen")
    print("Nilai G: ", G)