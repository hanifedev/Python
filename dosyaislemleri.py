file=open("dosya.txt","w")
file.write("""Bilgisayar,kendisine işlediğimiz bilgileri istediğimizde saklayabilen,
istediğimizde geri verebilen cihaza denir.
İlk elektrikli bilgisayar ENIAC'tır.""")
file.close()
ac=open("dosya.txt")
print(ac.readline())
ac.seek(0)
print(ac.read())
ac.seek(0)
print(ac.readlines())
#Dosyayı otomatik kapatmak
try:
    dosya=open("dosya.txt","r")
except IOError:
    print("bir hata olustu")
finally:
    dosya.close()
print("-"*30)
#Dosyayı otomatik olarak kapatmak
with open("dosya.txt","r") as dosya:
    print(dosya.read())
print("-"*30)
