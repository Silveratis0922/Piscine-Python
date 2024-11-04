from load_image import load_image
from PIL import Image
import numpy as np

def zoom(img, x, y, zoom) -> np.array:
    img = Image.open(img)
    img = img.convert('L')
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2,
                    x + w / zoom2, y + h / zoom2))
    test = np.array(img)
    print("New shape after slicing:", np.shape(np.expand_dims(test, axis=-1)), "or", np.shape(test))
    return img.show(img.resize((x, y), Image.LANCZOS))

def main():
    img = "animal.jpeg"
    print(load_image(img))
    zoom(img, 400, 400, 2)


if __name__ == "__main__":
    main()
