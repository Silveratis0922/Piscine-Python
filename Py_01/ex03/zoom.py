from load_image import load_image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


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
        print("New shape after slicing:",
              np.shape(np.expand_dims(array, axis=-1)), "or", np.shape(array))
        plt.imshow(array, cmap='grey')
        plt.show()
        return np.expand_dims(array, axis=-1)
    except FileNotFoundError:
        print("Error: File not found.")
    except Image.UnidentifiedImageError:
        print("Error: File is not an image.")
    except ValueError:
        print("Error: Size can't be negative.")
    except ZeroDivisionError:
        print("Error: Zoom can't be zero.")


def main():
    img = "animal.jpeg"
    print(load_image(img))
    print(zoom(img, 400, 2))


if __name__ == "__main__":
    main()
