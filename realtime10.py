#Dinda Rahmadanty Alamsyah
#065002500028

data = [12, 5, 9, 24, 1, 7]
print("List sebelum sorting:", data)

data.sort()
print("List setelah sorting:", data)

def binary_search(data, x):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == x:
            return mid
        elif data[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

cari = int(input("Masukkan angka yang ingin dicari: "))
hasil = binary_search(data, cari)

if hasil != -1:
    print("Angka ditemukan di index:", hasil)
else:
    print("Angka tidak ditemukan")