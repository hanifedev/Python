sayi=input("binary sayi giriniz : ")
uzunluk=len(sayi)
toplam=0
for i in sayi:
    uzunluk-=1
    sonuc=int(i)*(2**uzunluk)
    toplam+=sonuc
print("decimal : " , toplam)

    
