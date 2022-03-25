# NIM/Nama      : 16521076/Tabitha Permalla
# Tanggal       : 3 Oktober 2021
# Judul Program : Kalkulator
# Deskripsi     : Program kalkulator sederhana yang menerima 2 buah angka dan sebuah karakter operasi, dan menuliskan hasil perhitungannya. 
#                 Operator yang diterima adalah+(tambah), - (kurang), * (kali),/(bagi,dibulatkan ke bawah), % (sisa bagi).

# ALGORITMA
# Import library
import math

# Minta input dari pengguna
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
o = input("Masukkan operator: ")

# Jika pengguna memasukkan operator '+'
if o == '+':
    result = a + b
    print(a, "+", b, "=", result)
# Jika pengguna memasukkan operator '-'
elif o == '-':
    result = a - b
    print(a, "-", b, "=", result)
# Jika pengguna memasukkan operator '*'
elif o == '*':
    result = a * b
    print(a, "*", b, "=", result)
# Jika pengguna memasukkan operator '/'
elif o == '/':
    result = math.floor(a / b)
    print(a, "/", b, "=", result)
# Jika pengguna memasukkan operator '%' 
elif o == '%':
    result = a % b
    print(a, "%", b, "=", result)
else:
    print("Operator tidak dikenal")