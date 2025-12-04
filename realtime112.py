class Mahasiswa:
    total_mahasiswa = 0
    
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.total_mahasiswa += 1

    def tampilkan_biodata(self):
        print("\nHasil Data:")
        print(f"Nama:    {self.nama}")
        print(f"Nim:     {self.nim}")
        print(f"Angkatan: {self.angkatan}")

print("Masukkan Data Mahasiswa")

nama_input = input("Masukkan Namamu: ")
nim_input = input("Masukkan NIM kamu: ")
angkatan_input = input("Masukkan Tahun Angkatanmu: ")

mhs1 = Mahasiswa(nama_input, nim_input, angkatan_input)

mhs1.tampilkan_biodata()

print(f"\nTotal Mahasiswa {Mahasiswa.total_mahasiswa}")