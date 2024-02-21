from students import Ogrenci
from teachers import Ogretmen

ogrenci_listesi = []
ogretmen_listesi = []

def ogrenci_ekle(ogrenci):
    ogrenci_listesi.append(ogrenci)

def ogretmen_ekle(ogretmen):
    ogretmen_listesi.append(ogretmen)

def bilgileri_goster():
    print("Öğrenci Bilgileri:")
    for ogrenci in ogrenci_listesi:
        ogrenci.bilgileri_goster()

    print("\nÖğretmen Bilgileri:")
    for ogretmen in ogretmen_listesi:
        ogretmen.bilgileri_goster()

# Test
ogrenci1 = Ogrenci("Ali", 12345, "Yazılım Geliştirme - A")
ogrenci1.ders_ekle("Java")
ogrenci1.ders_ekle("Python")

ogrenci2 = Ogrenci("Ayşe", 67890, "Yazılım Geliştirme - B")
ogrenci2.ders_ekle(".Net")
ogrenci2.ders_ekle("Java")

ogrenci3 =Ogrenci("Cafer", 12897, "Yazılım Geliştirme - C")
ogrenci3.ders_ekle(".Net")
ogrenci3.ders_ekle("Python")

ogretmen1 = Ogretmen("Ahmet", "Java")
ogretmen1.ogrenci_ekle(ogrenci1)
ogretmen1.ogrenci_ekle(ogrenci2)

ogretmen2 = Ogretmen("Veli", "Python")
ogretmen2.ogrenci_ekle(ogrenci1)
ogretmen2.ogrenci_ekle(ogrenci3)

ogretmen3 = Ogretmen("Halit", ".Net")
ogretmen3.ogrenci_ekle(ogrenci2)
ogretmen3.ogrenci_ekle(ogrenci3)

ogrenci_ekle(ogrenci1)
ogrenci_ekle(ogrenci2)
ogrenci_ekle(ogrenci3)
ogretmen_ekle(ogretmen1)
ogretmen_ekle(ogretmen2)
ogretmen_ekle(ogretmen3)

bilgileri_goster()

