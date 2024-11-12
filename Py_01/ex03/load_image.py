from PIL import Image
import numpy as np


def load_image(path: str) -> np.array:
    """
    Basic fonction for load an image with pillow and return a numpy array.
    """
    try:  
        im = Image.open(path)
        array = np.array(im)
        print("The shape of image is:", np.shape(array))
        return array[0]
    except FileNotFoundError:
        print("Error: File not found.")
    except Image.UnidentifiedImageError:
        print("Error: File is not an image.")