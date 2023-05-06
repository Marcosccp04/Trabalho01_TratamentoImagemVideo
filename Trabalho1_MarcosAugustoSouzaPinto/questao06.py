from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from utils import in_file, out_file

def knn_filter(image, k, save=True, save_name=out_file('q6_k_vizinhos.jpg')):
    img = cv2.imread(image, 0)
    height, width = img.shape
    output = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            neighbors = []
            for m in range(i-k, i+k+1):
                for n in range(j-k, j+k+1):
                    if m >= 0 and n >= 0 and m < height and n < width:
                        neighbors.append(img[m, n])
            output[i, j] = np.mean(neighbors)

    cv2.imshow("Imagem original", img)
    cv2.imshow("Filtragem KNN", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if save:
        cv2.imwrite(save_name, output)

    return output


def media_filter(img, size):
    img = img.convert('L')
    img_array = np.array(img)
    kernel_size = (size, size)
    kernel = np.ones(kernel_size) / (size**2)
    filtered_array = np.zeros_like(img_array)
    height, width = img_array.shape
    for i in range(size//2, height-(size//2)):
        for j in range(size//2, width-(size//2)):
            filtered_array[i, j] = np.sum(kernel * img_array[i-(size//2):i+(size//2)+1, j-(size//2):j+(size//2)+1])
    filtered_img = Image.fromarray(filtered_array)
    filtered_img.save(out_file('q6_img_media.jpg'))
    return filtered_img

def moda_filter(img, k):
    img_array = np.array(img.convert('L')) 
    output = np.zeros_like(img_array)
    height, width = img_array.shape[:2]
    
    for i in range(height):
        for j in range(width):
            neighbors = []
            for m in range(i-k, i+k+1):
                for n in range(j-k, j+k+1):
                    if m >= 0 and n >= 0 and m < height and n < width:
                        neighbors.append(img_array[m, n])
            output[i, j] = np.bincount(neighbors).argmax()

    output_img = Image.fromarray(output)
    output_img.save(out_file('q6_img_moda.jpg'))
    return output_img


if __name__ == '__main__':
    img = Image.open((out_file("imgRuido.png")))
   #knn_filter(out_file("imgRuido.png"), 3)
    #filtered_img = moda_filter(img, 3)
    filtered_img = media_filter(img,3)
    filtered_img.show()

