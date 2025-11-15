#Dinda Rahmadanty Alamsyah
#065002500028

def dapatkan_akhiran_ordinal(n):
    if n == 0:
        return 'th'
    if 10 <= (n % 100) <= 20:
        return 'th'
    
    digit_terakhir = n % 10
    
    if digit_terakhir == 1:
        return 'st'
    elif digit_terakhir == 2:
        return 'nd'
    elif digit_terakhir == 3:
        return 'rd'
    else:
        return 'th'

print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    try:
        angka = int(input("masukkan angka: "))
    except ValueError:
        print("Input harus berupa angka.")
        continue

    if angka == 0:
        print("terima kasih telah menggunakan program saya")
        break
    suffix = dapatkan_akhiran_ordinal(angka)
    print(f"({angka}, '{suffix}')")
    
1