# Program Skala Gempa Bumi
# Spesifikasi Program : Program menerima bilangan skala richter dari sebuah gempa bumi dan mengeluarkan output kondisi yang sesuai dengan gempa bumi tersebut.

# KAMUS
# SR : float

# ALGORITMA
SR = float(input("Bilangan Skala Ricther: "))
if SR < 2.0:
    print("Micro")
elif 2.0 <= SR < 3.9:
    print("Minor")
elif 3.9 <= SR < 4.9:
    print("Light")
elif 4.9 <= SR < 5.9:
    print("Moderate")
elif 5.9 <= SR < 6.9:
    print("Strong")
elif 6.9 <= SR < 7.9:
    print("Major")
else:  # (SR > 7.9)
    print("Great")