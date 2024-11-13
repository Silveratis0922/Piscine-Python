from load_image import load_image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def rotate(array, size) -> np.array:
    """
    Translation of an array without the np.translate function.
    """
    t_array = np.empty([400, 400], dtype=int)
    for y in range(size):
        for x in range(size):
            t_array[y][x] = array[x][y]
    return t_array


def zoom(img, size, zoom) -> np.array:
    """
    Zooms in on an image at a specified size.
    """
    try:
        img = Image.open(img).convert('L')
        w, h = img.size
        zoom2 = zoom * 2
        left = max(0, (w - size) // zoom2) + 300
        top = max(0, (h - size) // zoom2)
        right = left + size
        bottom = top + size
        img = img.crop((left, top, right, bottom))
        array = np.array(img)
        t_array = rotate(array, size)
        print("New shape after Transpose:", np.shape(array))
        plt.imshow(t_array, cmap='grey')
        plt.show()
        return t_array
    except FileNotFoundError:
        print("Error: File not found")
    except Image.UnidentifiedImageError:
        print("Error: File is not an image.")
    except ValueError:
        print("Error: Size can't be negative.")
    except ZeroDivisionError:
        print("Error: Zoom can't be zero.")


def main():
    img = 'animal.jpeg'
    print(load_image(img))
    print(zoom(img, 400, 2))


if __name__ == "__main__":
    main()
