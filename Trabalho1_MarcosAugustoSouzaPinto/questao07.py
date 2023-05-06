import numpy as np
from PIL import Image
from utils import in_file, out_file

def sobel_filter(img):
    img_array = np.array(img)
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

if __name__ == "__main__":
    img = Image.open(in_file("img.jpg"))
    img = img.quantize(colors=32)
    filtered_img = sobel_filter(img)
    filtered_img.save(out_file("q7_sobel.png"))
    filtered_img.show()
    
