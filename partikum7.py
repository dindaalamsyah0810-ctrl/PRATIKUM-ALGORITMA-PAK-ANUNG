#Dinda Rahmadanty Alamsyah
#065002500028

def cek_prima(x):
    if x <= 1:
        return False
        
    if x == 2:
        return True
        
    for i in range(2, x):
       
        if x % i == 0:
            return False
            
    return True

def tampil_hasil_prima(angka, status_prima):
    if status_prima == True:
        print(f"{angka} adalah bilangan Prima")
    else:
        print(f"{angka} bukanlah bilangan Prima")
        
angka_input = int(input("Masukkan angka: "))
status = cek_prima(angka_input)
tampil_hasil_prima(angka_input, status)