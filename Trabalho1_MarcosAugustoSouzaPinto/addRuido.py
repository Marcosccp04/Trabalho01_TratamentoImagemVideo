import numpy as np
from PIL import Image
from utils import in_file, out_file

def add_ruido(img, prob):
    img_array = np.array(img)
    random_matrix = np.random.rand(*img_array.shape)
    salt_and_pepper = random_matrix < prob/2
    pepper = random_matrix < prob
    img_array[salt_and_pepper] = 255
    img_array[pepper] = 0
    noisy_img = Image.fromarray(img_array)

    noisy_img.save(out_file("imgRuido.png"))

if __name__ == "__main__":
    img = Image.open((in_file("filtragem.png")))
    add_ruido(img, prob=0.1)