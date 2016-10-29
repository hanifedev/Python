list=[]
snc=""
son=""
sayi=input("Dönüştürmek istediğiniz sayıyı giriniz")
while sayi!=0:
    kalan=int(sayi)%2
    sayi=int(sayi)/2
    snc+=str(kalan)
    list.append(snc)
for i in snc[::-1]:
    son+=str(i)
print(son)
    

