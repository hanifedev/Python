from datetime import *
before = datetime.now()
text = "Merhaba Dünya"
print("Text : {}".format(text))
if(text == input("Aynı metni giriniz : ")):
  after = datetime.now()
  speed = after - before
  seconds = speed.total_seconds()
  letter_per_second = round(len(text) / seconds , 1)
  print("Tebrikler!")
  print("Scor : {}".format(seconds))
  print("Letter per second : {}".format(letter_per_second))
else:
  print("Yanlış metin girdiniz")
