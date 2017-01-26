metin=input("Metin giriniz")
snc=""
sec=input("Şifrelemek için 1 ' e , şifreyi çözmek için 2'ye basınız çıkmak için q'ya basınız")
if sec=="1":
    for i in metin:
        snc+=chr((ord(i)+3)%255)
elif sec=="2":
    for i in metin:
        snc+=chr(abs(ord(i)-3)%255)
elif sec=="q":
    exit()
else:
    print("Yanlış seçim..")
print(snc)