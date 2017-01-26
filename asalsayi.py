sayi=int(input("bir sayı giriniz"))
sayac=0
for i in range(2,sayi):
    if sayi%i==0:
        sayac+=1
if sayac>=2:
    print("sayı asal değildir")
else:
    print("sayı asaldır")