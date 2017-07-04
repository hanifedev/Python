#!/bin/python3
import random
chars="abcdefghijklmnoprstuvwxyz1234567890ABCDEFGHIJKLMNOPRSTUVWXYZ,.*-+"
lenght2 = int(input("Kaç tane parola oluşturmak istiyorsunuz"))
lenght = int(input("Parolanız kaç karakter olsun"))
for p in range(lenght2):
  password=""
  for c in range(lenght):
    password += random.choice(chars)
  print("Parolanın uzunluğu = {} , Parola = {}".format(lenght,password))
print("{} tane parola oluşturuldu".format(lenght2))
