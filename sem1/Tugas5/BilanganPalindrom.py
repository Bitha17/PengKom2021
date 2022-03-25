# Program Bilangan Palindrom
# Spesifikasi Program : Program memeriksa apakah suatu bilangan bulat 8 digit yang diinputkan adalah bilangan palindrom atau bukan.

# KAMUS
# n: int

# ALGORITMA
n = 0
while n/10000000 < 1:
    n = int(input("Bilangan 8 digit: "))

if n % 10 == (n % 100000000 - n % 10000000)/10000000 and (n % 100 - n % 10)/10 == (n % 10000000 - n % 1000000)/1000000 and (n % 1000 - n % 100)/100 == (n % 1000000 - n % 100000)/100000 and (n % 10000 - n % 1000)/1000 == (n % 1000000 - n % 100000)/100000:
    print(f"Bilangan {n} adalah sebuah palindrom.")
else:
    print(f"Bilangan {n} bukanlah sebuah palindrom")