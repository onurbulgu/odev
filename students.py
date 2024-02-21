class Ogrenci:
    def __init__(self, ad, numara, sinifi):
        self.ad = ad
        self.numara = numara
        self.sinifi = sinifi
        self.dersler = []

    def ders_ekle(self, ders):
        self.dersler.append(ders)

    def bilgileri_goster(self):
        print(f"Öğrenci Adi: {self.ad}")
        print(f"Numarasi: {self.numara}")
        print(f"Sinifi: {self.sinifi}")
        print("Aldiği Dersler:")
        for ders in self.dersler:
            print(f"- {ders}")
        print(" ")

