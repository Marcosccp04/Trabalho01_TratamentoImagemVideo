from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from utils import in_file, out_file

def equalizar_histograma(img):
    img_cinza = img.convert('L')
    histograma, bins = np.histogram(img_cinza, bins=256, range=(0, 255))
    cdf = histograma.cumsum()
    cdf_norm = cdf / cdf.max()
    img_eq = np.interp(img_cinza, bins[:-1], cdf_norm)

    hist_eq, bins_eq = np.histogram(img_eq, bins=256, range=(0, 1))
    
    fig, axs = plt.subplots(1, 4, figsize=(20,5))
    axs[0].imshow(img, cmap='gray')
    axs[0].set_title('Imagem original')
    axs[1].bar(bins[:-1], histograma, width=1)
    axs[1].set_title('Histograma original')
    axs[2].imshow(img_eq, cmap='gray')
    axs[2].set_title('Imagem equalizada')
    axs[3].bar(bins_eq[:-1], hist_eq, width=1)
    axs[3].set_title('Histograma equalizado')
    plt.show()
    img_eq_pil = Image.fromarray((img_eq * 255).astype(np.uint8))
    img_eq_pil.save(out_file('q5_img_equalizada.jpg')) # salvar a imagem equalizada
    return img_eq

def realce_linear(imagem, a, b):
    img = cv2.imread(imagem)
    altura, largura, canais = img.shape

    # Aplicando a transformação radiométrica
    img_saida = np.zeros((altura, largura, canais), dtype=np.uint8)
    for i in range(altura):
        for j in range(largura):
            for k in range(canais):
                pixel = img[i, j, k]
                pixel_saida = a * pixel + b
                if pixel_saida < 0:
                    pixel_saida = 0
                elif pixel_saida > 255:
                    pixel_saida = 255
                img_saida[i, j, k] = pixel_saida
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Imagem de entrada')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img_saida, cv2.COLOR_BGR2RGB))
    plt.title('Imagem de saída')
    plt.axis('off')

    plt.show()
    cv2.imwrite(out_file('q5_img_realce.jpg'), img_saida)

def complemento_negativo(imagem):
    img = cv2.imread(imagem, cv2.IMREAD_GRAYSCALE)
    img_saida = 255 - img

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Imagem de entrada')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(img_saida, cmap='gray')
    plt.title('Imagem de saída')
    plt.axis('off')

    plt.show()
    cv2.imwrite(out_file('q5_img_negativo.jpg'), img_saida)

if __name__ == "__main__":
    img = Image.open((in_file("img.jpg")))
   # equalizar_histograma(img)
    #realce_linear((in_file("img.jpg")), 1.2, 80)
    complemento_negativo((in_file("img.jpg")))
   


