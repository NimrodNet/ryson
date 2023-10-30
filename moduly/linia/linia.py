from PIL import Image, ImageDraw, ImageFont

class Linia:

    def __init__(self, tlo):
        self.inicjuj(tlo)

    def inicjuj(self, tlo):
        grafika = tlo.zwroc()
        self.linia = ImageDraw.Draw(grafika)

    def rysuj(self, poczatek, koniec):
        self.linia.line(((poczatek[0], poczatek[1]), 
        (koniec[0], koniec[1])), "black")
