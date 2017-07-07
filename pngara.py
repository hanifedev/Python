import os
import re
dirc = "C:/Users/User/Desktop/deneme"
sayac = 0
dizin = os.listdir(os.chdir(dirc))
for i in dizin:
   if re.match(".*png", i):
       print("PNG DOSYASI : {}".format(i))
       sayac+=1
   else:
       if not re.match(".*png", i):
           os.chdir(dirc + "/" + i)
           for i in os.listdir(os.getcwd()):
               if re.match(".*png", i):
                   print("PNG DOSYASI : {}".format(i))
                   sayac+=1
if sayac == 0:
    print("PNG uzantılı dosya yoktur..")
else:
    print("Listeleme işlemi tamamlandı...{} dosya bulundu".format(sayac))
