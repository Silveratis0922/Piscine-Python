from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
    im = Image.open(path)
    test = np.array(im)
    
    print("The shape of image is:", np.shape(test))
    return(test)