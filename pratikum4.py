#Dinda Rahmdanty Alamsyah
#065002500028

bulan = int(input("masukan bulan (1-12): "))
while bulan < 1 or bulan > 12:
    print("bulan tidak valid coba lagi.")
    bulan = int(input("masukan bulan (1-12): "))

tahun = int(input("masukan tahun: "))

if bulan in (1, 3, 5, 7, 8, 10, 12):
    hari = 31
elif bulan in (4, 6, 9, 11):
    hari = 30
else:
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari = 29
    else:
        hari = 28
        
print(f"jumlah hari pada bulan {bulan} tahun {tahun} adalah {hari} hari: ")