import sqlite3 as sql
import os
vt = sql.connect("deneme.sqlite")
dosya_mevcut = os.path.exists("deneme.sqlite")
im = vt.cursor()
kisiler = [('Hanife', 'Kurnaz', 'Samsun'),
           ('Meltem', 'Tahta','Samsun'),
           ('Can', 'Akalın', 'Samsun'),
           ('Ayse', 'Kaplan', 'Samsun')]
im.execute("CREATE TABLE IF NOT EXISTS personel (isim,soyisim,memleket)")
if not dosya_mevcut:
    for kisi in kisiler:
        im.execute("INSERT INTO personel VALUES (?, ?, ?)", kisi)
im.execute("SELECT * FROM personel")
print(im.fetchone())
print(im.fetchmany(2))
print(im.fetchall())
im.execute("SELECT * FROM personel WHERE soyisim = 'Kaplan' ")
print(im.fetchall())
vt.commit()
vt.close()
