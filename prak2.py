#Dinda Rahmadanty Alamsyah
#065002500028

a = float(input("masukan panjang sisi a:"))
b = float(input("masukan panjang sisi b:"))
c = float(input("masukan panjang sisi c:"))

if a + b <= c or a + c <= b or b + c <= a:
    print("bukan segitiga")
    
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("segitiga siku-siku")
    
elif a == b == c:
    print("segitiga sama sisi")
    
elif a == b or a == c or b == c:
    print("segitiga sama kaki")
    
else:
    print("segitiga sembarang")