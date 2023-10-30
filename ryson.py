from PIL import Image, ImageDraw, ImageFont
from moduly.prostokat.prostokat import *
from moduly.linia.linia import *

rozmiar_tla = [400, 500]
tlo = Prostokat(rozmiar_tla)

linia = Linia(tlo)
linia.rysuj([10, 10], [100, 100])
linia.rysuj([100, 100], [100, 150])

tlo.zapisz("tlo.jpg")
