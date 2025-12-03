#Dinda Rahmadanty Alamsyah
#065002500028

def tulis_biodata():
    nama = input("Masukkan Nama mu: ")
    umur = input("Masukkan Umur mu: ")
    alamat = input("Masukkan Alamatmu: ")
    email = input("Masukkan Emailmu: ")
    dosen = input("Masukkan Dosen Walimu: ")

    file = open("Biodata.txt", "w")
    file.write("Nama: " + nama + "\n")
    file.write("Umur: " + umur + "\n")
    file.write("Alamat: " + alamat + "\n")
    file.write("Email: " + email + "\n")
    file.write("Dosen Wali: " + dosen + "\n")
    file.close()

    print("\nData berhasil disimpan ke Biodata.txt!\n")
    return nama, umur, alamat, email, dosen

def baca_biodata():
    file = open("Biodata.txt", "r")
    isi = file.read()
    file.close()
    print("Isi file Biodata.txt:")
    print(isi)

nama, umur, alamat, email, dosen = tulis_biodata()

baca_biodata()