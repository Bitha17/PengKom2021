n = int("Masukkan nilai n: ")
if n <= 0:
    print("Tidak ada data yang tersedia.")
else:
    T0 = [0 for i in range(n)]
    T1 = [0 for i in range(n)]
    for i in range(n):
        T0[i] = float(input("Masukkan data teramati ke-" +str(i+1)+ ": "))
    for i in range(n):
        T1[i] = float(input("Masukkan data hasil estimasi model komputasi ke-" +str(i+1)+ ": "))
    m = 0
    for i in range(n):
        m += (T0[i] - T1[i])**2
    MSE = m/n
    print("MSE: ", str(MSE))