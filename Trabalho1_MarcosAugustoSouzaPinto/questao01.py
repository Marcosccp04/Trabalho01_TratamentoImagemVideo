from PIL import Image
from utils import in_file, out_file

# 1. Alteração de brilho (um valor deve ser lido e passado por parâmetro para o procedimento de alteração de brilho da imagem)
def pixel_atualizado(r,g,b, shine):
    r = r + shine
    g = g + shine
    b = b + shine

    if r > 255:
        r = 255
    elif r < 0:
        r = 0

    if g > 255:
        g = 255
    elif g < 0:
        g = 0

    if b > 255:
        b = 255
    elif b < 0:
        b = 0
    return r,g,b
    
def aumentar_brilho(img, shine):
    largura, altura = img.size
    questao1_output = Image.new('RGB',(largura, altura))

    for w in range(largura):
        for h in range(altura):
            pixel = (w,h)
            r,g,b = img.getpixel(pixel)

            questao1_output.putpixel(pixel, pixel_atualizado(r,g,b,shine))
    questao1_output.save(out_file("q1_output.jpg"))
    questao1_output.show()


if __name__ == "__main__":
    img = Image.open((in_file("arvore.jpg")))
    aumentar_brilho(img,100)