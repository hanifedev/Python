giris="""
(1) Topla
(2) Çıkar
(3) Çarp
(4) Böl
(5) Karesini Hesapla
(6) karekök hesapla
"""
print(giris)
s1 = int(input("1. sayıyı giriniz"))
s2 = int(input("2. sayıyı giriniz"))
print("1. sayı:%s &&& 2. sayı: %s" % (s1, s2))
while True:
    islem=input("Yapmak istediğiniz işlemi seçiniz (Çıkmak için q' ya basınız)")
    if islem=="q":
        print("çıkılıyor..")
        break
    elif islem == "1":
        print("%s + %s = %s " %(s1,s2, s1+s2))
    elif islem == "2":
        print("%s - %s = %s" %(s1,s2,s1-s2))
    elif islem == "3":
        print("%s * %s = %s" %(s1,s2,s1*s2))
    elif islem == "4":
        print("%s / %s = %s" %(s1,s2,s1/s2))
    elif islem == "5":
        print("%s ^ %s = %s" %(s1,s2,s1**s2))
    elif islem =="6":
        s3=input("karekokunu almak istediginiz sayıyı giriniz")
        print("%s nin karekoku : " %(s3, s3**0.5))
    else:
        print("Yanlıs giris ")
