from PIL import Image, ImageDraw, ImageFont


class Prostokat:

    def __init__(self, rozmiar):
        self.tlo = self.stworz(rozmiar)

    def stworz(self, rozmiar):
        grafika = Image.new("RGB", (rozmiar[0], rozmiar[1]), "white")
        return grafika

    def zwroc(self):
        return self.tlo

    def zapisz(self, nazwa):
        self.tlo.save(nazwa)
