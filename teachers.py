class Ogretmen:
    def __init__(self, ad, brans):
        self.ad = ad
        self.brans = brans
        self.ogrenciler = []

    def ogrenci_ekle(self, ogrenci):
        self.ogrenciler.append(ogrenci)

    def bilgileri_goster(self):
        print(f"Öğretmen Adı: {self.ad}")
        print(f"Branşı: {self.brans}")
        print("Öğrenciler:")
        for ogrenci in self.ogrenciler:
            print(f"- {ogrenci.ad}")
        print("  ")

