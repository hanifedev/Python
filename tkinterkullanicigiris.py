from tkinter import *
import time

bilgiler = ("hanife", "123456")
denemeHakki = 3
zaman = 0
def girisYap():
    global denemeHakki, zaman
    if(denemeHakki <= 0):
        if time.time() - zaman >= 5:
            denemeHakki = 3
        else:
            sonuc.config(text = "5 sn. beklemeniz gerekir.. Kalan zaman : {}".format(int(5 - (time.time() - zaman))))
            return False
    kAdi = kutu.get()
    prl = kutu2.get()
    print(kAdi, " - ", prl)
    print("Bilgiler kontrol ediliyor...")
    if(kAdi == bilgiler[0]) and (prl == bilgiler[1]):
        print("Bilgiler doğru")
        sonuc.config(text = "Başarıyla giriş yapıldı..")
        ekraniTemizle()
    else:
        print("Bilgiler yanlış")
        denemeHakki -= 1
        if(denemeHakki == 0):
            zaman = time.time()
        sonuc.config(text = "Bilgiler yanlış! Kalan deneme hakkı: {}".format(denemeHakki))

def ekraniTemizle():
    yazi.config(text = "Sisteme hoşgeldiniz")
    isim.destroy()
    kutu.destroy()
    parola.destroy()
    kutu2.destroy()
    buton.destroy()

pencere = Tk()
pencere.title("Giriş Ekranı")
yazi = Label(pencere, text = "Hosgeldiniz, lütfen giriş yapınız")
yazi.pack()

isim = Label(pencere, text = "Kullanıcı Adı:")
isim.pack()

kutu = Entry(pencere)
kutu.pack()

parola = Label(pencere, text = "Parola:")
parola.pack()

kutu2 = Entry(pencere)
kutu2.pack()

buton = Button(pencere, text="Giriş Yap", command = girisYap)
buton.pack()

sonuc = Label(pencere, text="Henüz giriş yapılmadı")
sonuc.pack()

pencere.mainloop()
