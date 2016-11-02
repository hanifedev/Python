sayi=input("binary sayı giriniz: ")
lst=[]
tum=""
snc=""
for i in sayi:
    if(i=="1"):
        tum+="0"
        lst.append(tum)
    else:
        tum+="1"
        lst.append(tum)
for i in tum:
    snc+=str(i)
print("1 e tümlenmiş hali :" ,snc)
            

