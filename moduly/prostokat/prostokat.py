from PIL import Image, ImageDraw, ImageFont

class Prostokat:

    def __init__(self, rozmiar):
        self.tlo = self.stworz(rozmiar)

    def stworz(self, rozmiar):
        grafika = Image.new("RGB", (rozmiar[0], rozmiar[1]), "white")
        return grafika

    def zwroc(self):
        return self.tlo

    def otworz(self, nazwa):
        self.tlo = Image.open(nazwa)

    def zapisz(self, nazwa):
        self.tlo.save(nazwa)

    def pokaz(self, nazwa):
        self.tlo.show(nazwa)

    def rysuj_piksel(self, pozycja):
        self.mapa_pikseli = self.tlo.load()
        self.mapa_pikseli = pozycja
