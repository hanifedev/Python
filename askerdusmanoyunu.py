import random
class Asker():
    def __init__(self):
        self.guc = 100
        self.silah = 50
    def vurulma(self, deger):
        self.guc -= deger

    def canlı_mı(self, ):
        if self.guc > 0:
            return True
        else:
            return False

class Oyuncu(Asker):
    def __init__(self):
        self.guc = 1500
        self.silah = 70

class Dusman(Asker):
    def __init__(self):
        self.guc = random.randint(10,100)
        self.silah = random.randint(20,100)

kahraman = Oyuncu()

dusmanlar = []
for i in range(10):
    dusmanlar.append(Dusman())
print(dusmanlar)
while (kahraman.canlı_mı()) and (len(dusmanlar)>0):
    print("Kahramanımız hayatta, güç : {}".format(kahraman.guc))
    for sayi, adam in enumerate(dusmanlar):
        print(sayi+1, "- Gücü : {} - Silah Kapasitesi : {}".format(adam.guc,adam.silah))

    hedef = int(input("Vurmak istediğiniz dusmanın numarasını giriniz"))
    dusmanlar[hedef-1].vurulma(kahraman.silah)
    if(dusmanlar[hedef-1].guc < 0):
        del(dusmanlar[hedef-1])
    print("==============================================\n\n")
    for i in range(random.randint(1,len(dusmanlar))):
        ates_eden = random.choice(dusmanlar)
        kahraman.vurulma(ates_eden.silah)

print("Oyun bitti, kahraman öldü. Lütfen tekrar oynayın...")
