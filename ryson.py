from PIL import Image, ImageDraw, ImageFont
from moduly.prostokat.prostokat import *
from moduly.linia.linia import *
from moduly.piksel.piksel import *
import math
from moduly.elipsa.elipsa import *
from moduly.elipsa.okrag import *

rozmiar_tla = [400, 500]
tlo = Prostokat(rozmiar_tla)

linia = Linia(tlo)
linia.rysuj([10, 10], [100, 100])
linia.rysuj([100, 100], [100, 150])

piksel = Piksel(tlo)
piksel.rysuj([50, 10], (0, 0, 255))

elipsa = Elipsa(tlo, [50, 50], [200, 120])
elipsa.rysuj()

okrag = Okrag(tlo, [70, 80], 130)
okrag.rysuj()

tlo.zapisz("tlo.jpg")
tlo.pokaz("tlo.jpg")
