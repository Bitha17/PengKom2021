# Program TinggiRataRata
# Spesifikasi Program : Program ini menerima 5 input data "tinggi" dan memberikan output berupa rata-rata dari input

# KAMUS
# i, a : int
# array : list/array
# rerata : float

# ALGORITMA
# Minta pengguna memasukan 5 data
array = []
for i in range(1, 6):
    a = int(input(f"tinggi {i}: "))
    array.insert(i-1, a)
# Hitung rata-rata
rerata = sum(array)/5.0
# Berikan rata-rata dari data
print(f"tinggi rata-rata: {rerata}")