#Dinda Rahmadanty Alamsyah
#065002500028

def is_leap(year):
    """Cek tahun kabisat."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days(month, year):
    """Hitung jumlah hari dalam bulan."""
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
            
    elif 1 <= month <= 12:
        return days[month]
        
    else:
        return 0

print("Program hitung hari (ketik 0 untuk berhenti)")
while True:
    try:
        month_input = input("Masukkan bulan (1-12): ")
        month = int(month_input)
        
        if month == 0:
            print("Sampai jumpa lagi!")
            break

        if 1 <= month <= 12:
            pass 
        else:
            print("Bulan harus di antara 1-12.")
            continue 

        year_input = input("Masukkan tahun (e.g., 2023): ")
        year = int(year_input)
        
        days = get_days(month, year)
        
        if days > 0:
            print(f"{days} hari dalam sebulan")
        else:
            print("Input bulan atau tahun tidak valid.")

    except ValueError:
        print("Input harus berupa angka.")