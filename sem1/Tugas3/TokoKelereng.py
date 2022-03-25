# Program TokoKelereng
# Spesifikasi Program : Program ini memberi informasi mengenai harga kelereng. Kemudian program ini menerima input berupa jumlah kelereng yang mau dibeli, dan memberikan output berupa harga dari total belanjaan.

# KAMUS
# merah, hijau, hitam, harga : int

# ALGORITMA
# Sambut pelanggan, dan berikan list harga
print("Selamat datang di Toko Kelereng.\nBerikut adalah daftar harga kelereng di toko kami:\n merah: 10 sen\n hijau: 15 sen\n hitam: 20 sen\n")
# Tanyakan pelanggan jumlah kelereng yang ingin dibeli
print("Berapa kelereng yang akan Anda beli?")
merah = int(input("Kelereng merah: "))
hijau = int(input("Kelereng hijau: "))
hitam = int(input("Kelereng hitam: "))
# Hitung harga total
harga = merah*10 + hijau*15 + hitam*20
# Berikan harga total
print(f"\nTotal belanjaan Anda hari ini senilai {harga} sen.\nTerima kasih telah berbelanja di toko kami.")