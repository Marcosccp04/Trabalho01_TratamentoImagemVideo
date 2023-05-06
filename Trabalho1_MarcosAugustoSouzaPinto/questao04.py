from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from utils import in_file, out_file

def calcular_histograma(imagem):
    largura, altura = imagem.size
    num_particoes = 3
    altura_particao = altura // num_particoes
    histograma = np.zeros((num_particoes, 256), dtype=int)

    for x in range(largura):
        for y in range(altura):
            r, g, b = imagem.getpixel((x,y))
            intensidade = int((r + g + b) / 3)
            particao = min(num_particoes-1, y // altura_particao)
            histograma[particao][intensidade] += 1

    return histograma

def salvar_histograma_csv(histograma):
    histograma_concatenado = np.concatenate(histograma)
    np.savetxt(out_file("q4_histograma_local.csv"), histograma_concatenado, delimiter=",")


def histograma_local(img):
    histograma = calcular_histograma(img)
    salvar_histograma_csv(histograma)

if __name__ == "__main__":
    img = Image.open((in_file("img.jpg")))
    histograma_local(img)