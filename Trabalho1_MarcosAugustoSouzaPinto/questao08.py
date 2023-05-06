import numpy as np
from PIL import Image
from utils import in_file, out_file

def sobel_filter(img):
    img_gray = img.convert("L")  # Converter para níveis de cinza
    img_array = np.array(img_gray)
    height, width = img_array.shape[:2]
    output = np.zeros_like(img_array, dtype=np.float32)
    kernel_x = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]], dtype=np.float32)
    kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)

    for i in range(1, height-1):
        for j in range(1, width-1):
            window = img_array[i-1:i+2, j-1:j+2]
            Gx = np.sum(kernel_x * window)
            Gy = np.sum(kernel_y * window)
            output[i, j] = np.sqrt(Gx**2 + Gy**2)

    output *= 255.0 / np.max(output)
    output = output.astype(np.uint8)
    return Image.fromarray(output)


def bic_descriptor(img):
    img_array = np.array(img)
    height, width = img_array.shape[:2]
    quantized_array = np.zeros_like(img_array)
    num_colors = 32
    step = 256 // num_colors

    for i in range(num_colors):
        lower_bound = i * step
        upper_bound = (i+1) * step
        quantized_array[(img_array >= lower_bound) & (img_array < upper_bound)] = lower_bound + step//2

    sobel = sobel_filter(Image.fromarray(quantized_array))
    hist_edge = np.zeros(num_colors)
    hist_interior = np.zeros(num_colors)

    for i in range(height):
        for j in range(width):
            if sobel.getpixel((j, i)) > 0:
                hist_edge[quantized_array[i, j] // step] += 1
            else:
                hist_interior[quantized_array[i, j] // step] += 1

    hist_edge /= np.sum(hist_edge)
    hist_interior /= np.sum(hist_interior)
    
    np.savetxt(out_file("q8_histograma_borda.csv"), hist_edge, delimiter=",")
    np.savetxt(out_file("q8_histograma_inteior.csv"), hist_interior, delimiter=",")
    
    border_img = img.copy()
    interior_img = img.copy()

    for i in range(height):
        for j in range(width):
            if sobel.getpixel((j, i)) > 0:
                interior_img.putpixel((j, i), (255, 255, 255))
            else:
                border_img.putpixel((j, i), (255, 255, 255))

    return border_img, interior_img

if __name__ == "__main__":
    img = Image.open(in_file("arvore.jpg")).convert("RGB")
    border_img, interior_img = bic_descriptor(img)
    border_img.save(out_file("q8_borda.png"))
    interior_img.save(out_file("q8_interior.png"))
