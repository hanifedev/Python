import numpy as np
import tensorflow as tf

girdiler = np.array([2,5])
agirliklar = np.array([-1,0.8])
agirlikli_toplam = girdiler * agirliklar
toplam = sum(agirlikli_toplam)
aktivasyon_fonksiyonu = (lambda x:1 if x > 0 else -1)
cikti = aktivasyon_fonksiyonu(toplam)
print(cikti)

print("******* tensorflow ile *********")
sess = tf.InteractiveSession()
girdi_1 = tf.constant(2.0)
girdi_2 = tf.constant(5.0)
agirlik_1 = tf.constant(-1.0)
agirlik_2 = tf.constant(0.8)

toplam_1 = tf.multiply(girdi_1, agirlik_1)
toplam_2 = tf.multiply(girdi_2, agirlik_2)
agirlikli_toplam = tf.add(toplam_1, toplam_2)
toplam = agirlikli_toplam.eval()
aktivasyon_fonksiyonu = (lambda x:1 if x>0 else -1)
cikti = aktivasyon_fonksiyonu(toplam)
print(cikti)
