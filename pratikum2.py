# Dinda Rahmadanty Alamsyah
# 065002500028

import math

print("silahkan isi lattitude dan longitude-nya untuk menetukan jarak antara 2 titik yang di cari:")

R = 6371

nama_titik1 = input("Masukkan Nama titik pertama permukaannya: ")
nama_titik2 = input("Masukkan Nama titik kedua permukaannya: ")
lat1 = float(input(f"Masukkan Lattitude 1 ({nama_titik1}) = "))
lon1 = float(input(f"Masukkan Longitude 1 ({nama_titik1}) = "))
lat2 = float(input(f"Masukkan Lattitude 2 ({nama_titik2}) = "))
lon2 = float(input(f"Masukkan Longitude 2 ({nama_titik2}) = "))

lat1_rad = math.radians(lat1)
lon1_rad = math.radians(lon1)
lat2_rad = math.radians(lat2)
lon2_rad = math.radians(lon2)

dlat = lat2_rad - lat1_rad
dlon = lon2_rad - lon1_rad

a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
jarak = R * c

print(f"Jarak antara {nama_titik1} dan {nama_titik2} adalah {jarak} kilometer")