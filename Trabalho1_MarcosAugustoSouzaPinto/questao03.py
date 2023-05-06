from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from utils import in_file,out_file

def histograma_global(img):
    largura, altura = img.size
    histograma = np.zeros(256, dtype=int)
    for x in range(largura):
        for y in range(altura):
            r, g, b = img.getpixel((x,y))
            intensidade = int((r + g + b) / 3)
            histograma[intensidade] += 1
    np.savetxt(out_file('q3_vetor_caracteristicas.csv'), histograma, delimiter=',')

if __name__ == "__main__":
    img = Image.open((in_file("img.jpg")))
    histograma_global(img)
