# Dinda Rahmadanty Alamsyah
# 065002500028

print("Hitung Luas Ruangan")
panjang_str = input("Masukkan Panjang Ruangan (Meter): ")
lebar_str = input("Masukkan Lebar Ruangan (Meter): ")

panjang_meter = float(panjang_str)
lebar_meter = float(lebar_str)

luas_meter = panjang_meter * lebar_meter

print(f"Luas ruangan dengan panjang {panjang_meter:.1f} dan lebar {lebar_meter:.1f} adalah {luas_meter:.1f} Meter")

konstanta_konversi = 39.3701
luas_inci = luas_meter * konstanta_konversi * konstanta_konversi

print(f"Luas ruangan dalam Inci adalah {luas_inci:.1f} Inci")