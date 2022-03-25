# Program LuasSegitiga
# Spesifikasi Program : Program ini menerima input berupa panjang alas dan tinggi segitiga, kemudian memberikan output berupa luas segitiga

# KAMUS
# alas, tinggi : int
# luas : float

# ALGORITMA
# Minta panjang alas segitiga
alas = int(input("panjang alas segitiga: "))
# Minta tinggi segitiga
tinggi = int(input("tinggi segitiga: "))
# Hitung luas segitiga
luas = 0.5*alas*tinggi
# Berikan luas segitiga
print(f"luas segitiga: {luas} satuan")