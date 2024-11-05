from PIL import Image
import numpy as np

def load_image(path: str) -> np.array:
    im = Image.open(path)
    array = np.array(im)

    print("The shape of image is:", np.shape(array))
    return array[0]