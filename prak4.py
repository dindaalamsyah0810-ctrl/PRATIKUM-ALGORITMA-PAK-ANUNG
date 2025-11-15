#Dinda Rahmdanty Alamsyah
#065002500028

while True:
    try:
        bulan = int(input("masukan bulan (1-12): "))
        if 1 <= bulan <= 12:
            break
        else:
            print("bulan tidak valid coba lagi.")
    except ValueError:
        print("Input bulan tidak valid. Masukkan angka antara 1 dan 12.")
try:
    tahun = int(input("masukan tahun: "))
except ValueError:
    print("Input tahun tidak valid. Menggunakan tahun default 2025.")
    tahun = 2025 
hari = 0
if bulan in (1, 3, 5, 7, 8, 10, 12):
    hari = 31
elif bulan in (4, 6, 9, 11):
    hari = 30
else:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari = 29 
    else:
        hari = 28 
print(f"jumlah hari pada bulan {bulan} tahun {tahun} adalah {hari} hari.")