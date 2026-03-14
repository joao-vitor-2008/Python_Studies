from PIL import Image
import numpy as numpy

img = Image.open("/home/joao-vitor/Imagens/-2026-03-08_13-10-55.png")
matrix = numpy.array(img)

print(matrix)
