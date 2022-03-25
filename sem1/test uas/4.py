# Program digunakan untuk menuliskan ke layar hasil f(x) berdasarkan 
# masukan nilai a dan b (bilangan riil) dan n (bilangan bulat) dari pengguna dengan menggunakan deret di atas. 
# Nilai xi sebanyak n buah juga merupakan masukan dari pengguna. Diasumsikan: n > 0.

# KAMUS


# ALGORITMA
# Minta pengguna memasukkan a, b, dan n
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
n = int(input("Masukkan nilai n: "))

# Olah nilai f(x)
f = 0
for i in range(n):
    x = float(input("Masukkan nilai x(" +str(i+1)+ "): "))
    f = f + a*x + b

# Print nilai f(x)
print("Nilai f(x): " +str(f))
