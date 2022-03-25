# NIM/Nama  : 16521076/Tabitha Permalla
# Tanggal   : 06/10/2021
# Deskripsi : Program menentukan apakah data Tuan Dip mungkin benar atau tidak mungkin benar.

# KAMUS
# K, O, A: int

# ALGORITMA
K = int(input("Banyak kaki yang menginjak lantai: "))
O = int(input("Banyak orang tua: "))
A = int(input("Banyak anak: "))

if K % 2 == 0:  # Jika K genap
    if K > (A + O) * 2:  # Jika jumlah kaki lebih banyak dari dua kali jumlah orang yang ada
        print("Data Tuan Dip tidak mungkin benar.")
    elif A <= O * 2:  # Jika jumlah anak lebih sedikit dari atau sama dengan 2 kali jumlah orang tua
        if K >= O * 2:
            print("Data Tuan Dip mungkin benar.")
        else:  # K < O * 2 
            print("Data Tuan Dip tidak mungkin benar.")
    else:  # A > O * 2 (Jika jumlah anak lebih banyak dari 2 kali jumlah orang tua)
        if K >= (O * 2 + (A - 2 * O) * 2):
            print("Data Tuan Dip mungkin benar.")
        else:  # K < (O * 2 + (A - 2 * O) * 2)
            print("Data Tuan Dip tidak mungkin benar.")
else:  # K % 2 != 0 (Jika K ganjil)
    print("Data Tuan Dip tidak mungkin benar.")