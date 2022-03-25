# Program RataRataSuhu
# Deskripsi Program : Program menerima data suhu harian Bandung (dalam derajat Celcius) selama bulan September 2018.
#                     Program kemudian menuliskan rata-rata suhu, nilai suhu terndah, tanggal-tanggal saat suhu >= 30 derajat Celcius, 
#                     dan tanggal pertama kali suhu di bawah 15 derajat Celcius.

# KAMUS
#   S : array [0..29] of integer
#   i : int (index)
#   sum, min, avg: int
#   found : boolean
#   CONTOH
#      Misalkan S = [25, 27, 26, 20, 23, 29, 30, 24, 20, 32, 
#                    34, 22, 15, 28, 25, 27, 26, 31, 23, 21,
#                    32, 26, 22, 27, 33, 14, 24, 21, 19, 32] 

# ALGORITMA
# Deklarasi array S
S = [0 for i in range(30)]

# Mengisi array S dari pembacaan nilai dari keyboard
for i in range(0, 30):
    S[i] = int(input("Suhu " + str(i+1) + " September 2018: "))
# Misalkan S = [25, 27, 26, 20, 23, 29, 30, 24, 20, 32, 
#               34, 22, 15, 28, 25, 27, 26, 31, 23, 21,
#               32, 26, 22, 27, 33, 14, 24, 21, 19, 32]

# Menghitung dan mencetak rata-rata suhu
sum = 0
for i in range(0, 30):
    sum = sum + S[i]
avg = sum//30
print("Rata-rata suhu kota Bandung di bulan Sept. 2018 adalah " + str(avg) + " derajat Celcius")

# Mencetak suhu terendah
min = S[0]
for i in range(1, 30):
    if S[i] < min:
        min = S[i]
print("Suhu terendah di bulan Sept 2018 adalah " + str(min) + " derajat Celcius")

# Mencetak tanggal saat suhu harian >= 30
for i in range(1, 30):
    if S[i] >= 30:
        print("Suhu di tanggal " + str(i+1) + " lebih besar dari 30 derajat Celcius")

# Mencetak tanggal pertama suhu < 15 
i = 0
found = False 
while (i >= 0 and found == False):
    if S[i] < 15:
        found = True
    else:
        i = i + 1   # hanya increment jika X belum ditemukan
# i < 0 atau found = True

# Cetak hasil
if (found == True):  # X ditemukan di T
    print("Kota Bandung pertama kali mengalami suhu dibawah 15 derajat Celcius di bulan Spetember 2018 pada tanggal " + str(i+1))
else:  # found = False; X tidak ditemukan di T
    print("Suhu tidak pernah di	bawah 15 derajat Celcius")

# Jawaban yang diekspektasikan : 
#   Rata-rata suhu kota Bandung di bulan Sept. 2018 adalah 25 derajat Celcius
#   Suhu terendah di bulan Sept 2018 adalah 14 derajat Celcius
#   Suhu di tanggal 7 lebih besar dari 30 derajat Celcius
#   Suhu di tanggal 10 lebih besar dari 30 derajat Celcius
#   Suhu di tanggal 11 lebih besar dari 30 derajat Celcius
#   Suhu di tanggal 18 lebih besar dari 30 derajat Celcius
#   Suhu di tanggal 21 lebih besar dari 30 derajat Celcius
#   Suhu di tanggal 25 lebih besar dari 30 derajat Celcius
#   Suhu di tanggal 30 lebih besar dari 30 derajat Celcius
#   Kota Bandung pertama kali mengalami suhu dibawah 15 derajat Celcius di bulan Spetember 2018 pada tanggal 26