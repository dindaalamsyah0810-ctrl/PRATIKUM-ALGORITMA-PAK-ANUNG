#Dinda Rahmadanty Alamsyah
#065002500028

print("---Program Perhitungan Diskon Pembelian USakTIF---")

nama = input("Masukkan Nama: ")
nim = input("Masukkan Nim: ")

total_belanja = -1
input_valid = False
while not input_valid:
    total_belanja_str = input("Masukkan Total Belanja anda: ")
    try:
        total_belanja = int(total_belanja_str)
        if total_belanja <= 0:
            print("Masukkan total belanja dengan benar!")
        else:
            input_valid = True
    except ValueError:
        if total_belanja_str.strip() == "":
            print("Total belanja tidak boleh kosong!")
        else:
            print("Masukkan total belanja berupa angka yang benar!")

persen_diskon = 0
potongan_harga = 0
kode_kupon_berlaku = "IKLB99"
gratis_ongkir = False
pesan_diskon = "--ANDA TIDAK MENDAPATKAN DISKON--"

kupon_diproses = False
while not kupon_diproses:
    bayar_kupon = input("Bayar pakai kupon? y/n: ").strip().lower()

    if bayar_kupon == 'y':
        kode_kupon_input = input("Masukkan kode kupon: ").strip()
        if kode_kupon_input == kode_kupon_berlaku:
            persen_diskon = 100
            pesan_diskon = "--SELAMAT ANDA MENDAPATKAN DISKON 100%--"
            gratis_ongkir = True
            kupon_diproses = True
        else:
            print("--Maaf kode yang anda pakai salah atau expired!--")
            kupon_diproses = True
    elif bayar_kupon == 'n':
        kupon_diproses = True
    else:
        print("Masukkan pilihan dengan benar!")

if persen_diskon != 100:
    if total_belanja >= 390000:
        persen_diskon = 80
        pesan_diskon = "--SELAMAT ANDA MENDAPATKAN DISKON 80%--"
    elif total_belanja >= 190000:
        persen_diskon = 60
        pesan_diskon = "--SELAMAT ANDA MENDAPATKAN DISKON 60%--"
    elif total_belanja >= 90000:
        persen_diskon = 40
        pesan_diskon = "--SELAMAT ANDA MENDAPATKAN DISKON 40%--"
    elif total_belanja >= 40000:
        persen_diskon = 20
        pesan_diskon = "--SELAMAT ANDA MENDAPATKAN DISKON 20%--"

if persen_diskon > 0:
    potongan_harga = total_belanja * (persen_diskon / 100)

total_pembayaran = total_belanja - potongan_harga

print(pesan_diskon)
print("---Rincian Belanja---")
print(f"Nama : {nama}")
print(f"Total Belanja anda : Rp. {total_belanja:.0f}".replace(",", "."))
print(f"Potongan harga : Rp. {potongan_harga:.0f}".replace(",", "."))

if gratis_ongkir:
    print("Total Pembayaran : GRATIS TIS")
else:
    print(f"Total Pembayaran : Rp. {total_pembayaran:.0f}".replace(",", "."))

print("\nTerimakasih sudah belanja :)")