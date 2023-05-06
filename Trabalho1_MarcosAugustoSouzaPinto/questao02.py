from PIL import Image
from utils import in_file, out_file

# 2. Imagem negativa (inversão de cores)

def imagem_negativa(img):
    largura, altura = img.size
    questao2_output = Image.new('RGB',(largura, altura))
    for w in range(largura):
        for h in range(altura):
            pixel = (w,h)
            r,g,b = img.getpixel(pixel)
            r = 255 - r
            g = 255 - g
            b = 255 - b

            questao2_output.putpixel(pixel,(r,g,b))
    questao2_output.save(out_file("q2_output.jpg"))
    questao2_output.show()        



if __name__ == "__main__":
    img = Image.open((in_file("arvore.jpg")))
    imagem_negativa(img)