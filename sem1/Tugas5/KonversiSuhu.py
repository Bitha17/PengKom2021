# Program Konversi Suhu
# Spesifikasi Program : Program menerima input suhu dalam satuan kelvin, celcius, reamur, atau farenheit. Kemudian mengonversikan suhu tersebut ke kelvin, celcius, reamur, atau farenheit sesuai pilihan pengguna.

# KAMUS
# T!, T2, T: float
# S1, S2, S: string

# ALGORITMA
# Terima input besaran suhu dan satuan suhu
T1 = float(input("suhu: "))
S1 = str(input("huruf pertama satuan suhu: "))
S2 = str(input("suhu akan dikonversi ke satuan (huruf pertama): "))

# Suhu awal (T1) dikonversi ke angka tengah (T2)
if S1 == "k" or S1 == "K":
    T2 = (T1 - 273)/5
elif S1 == "c" or S1 == "C":
    T2 = T1/5
elif S1 == "r" or S1 == "R":
    T2 = T1/4
elif S1 == "f" or S1 == "F":
    T2 = (T1 - 22)/9
else:
    print("Satuan suhu tidak valid.")
    exit

# Angka tengah (T2) dikonversi ke satuan yang diinginkan
if S2 == "k" or S2 == "K":
    T = T2*5 + 273 
    S = "K"
elif S2 == "c" or S2 == "C":
    T = T2*5
    S = "C"
elif S2 == "r" or S2 == "R":
    T = T2*4
    S = "R"
elif S2 == "f" or S2 == "F":
    T = T2*9 + 22
    S = "F"
else:
    print("Satuan suhu tidak valid.")
    exit

print(f"suhu: {T} " + S)