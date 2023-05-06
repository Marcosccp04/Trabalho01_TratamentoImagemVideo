import cv2
import numpy as np

def bic_descriptor(img):
    # Converter a imagem para escala de cinza
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar o algoritmo Canny para detecção de bordas
    canny_img = cv2.Canny(gray_img, 30, 100)

    # Criar uma máscara com os pixels de borda
    border_mask = np.zeros_like(img)
    border_mask[canny_img > 0] = img[canny_img > 0]

    # Inverter a máscara para obter os pixels de interior
    interior_mask = cv2.bitwise_not(border_mask)

    return border_mask, interior_mask

# Carregar a imagem
img = cv2.imread('bic.png')

# Chamar a função bic_descriptor para obter as imagens de borda e interior
border_img, interior_img = bic_descriptor(img)

# Exibir as imagens
cv2.imshow('Imagem de Borda', border_img)
cv2.imshow('Imagem de Interior', interior_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
