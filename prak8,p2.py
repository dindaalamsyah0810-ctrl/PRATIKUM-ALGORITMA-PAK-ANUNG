#Dinda Rahmadanty Alamsyah
#065002500028
#Pratikum Algoritma Part 2

def hitung_pangkat_positif(base, power):

    if power == 0:
        return 1
    
    if power == 1:
        return base
        
    else:
        return base * hitung_pangkat_positif(base, power - 1)

def pangkat_rekursif(base, power):

    if power >= 0:
        return hitung_pangkat_positif(base, power)
    else:

        pangkat_positif = hitung_pangkat_positif(base, -power)
        return 1 / pangkat_positif

print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")

while True:

    base_str = input("\nMasukkan Angka : ")
    if base_str == "":
        print("Program Selesai")
        break

    base = float(base_str)
    
    power_str = input("Masukkan Pangkatnya : ")
    if power_str == "":
        print("Program Selesai")
        break
        
    power = int(power_str)

    hasil = pangkat_rekursif(base, power)
    print(f"Hasilnya adalah: {hasil}")