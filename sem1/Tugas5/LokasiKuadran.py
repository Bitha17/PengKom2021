# Program Lokasi Kuadran
# Spesifikasi Program : Program menerima sebuah titik lokasi, kemudia mengidentifikasi kuadran lokasi titik tersebut.

# KAMUS
# x, y : int

# ALGORTIMA
x = int(input("koordinat x: "))
y = int(input("koordinat y: "))

if x == 0:
    if y == 0:
        print("Titik terdapat di titik origin (O)")
    elif y > 0:
        print("Titik terdapat di sumbu y positif")
    else:
        print("Titik terdapat di sumbu y negatif")
elif x > 0:
    if y == 0:
        print("Titik terdapat di sumbu x positif")
    elif y > 0:
        print("Titik terdapat di kuadran I")
    else: 
        print("Titik terdapat di kuadran IV")
else: 
    if y == 0:
        print("Titik terdapat di sumbu x negatif")
    elif y > 0:
        print("Titik terdapat di kuadran II")
    else: 
        print("Titik terdapat di kuadran III")