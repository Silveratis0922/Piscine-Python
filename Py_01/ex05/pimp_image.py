import numpy as np
from PIL import Image


def ft_invert(array) -> np.array:
    copy = np.copy(array)
    x, y, c = np.shape(copy)
    invert_array = np.empty([x, y, c], dtype=np.uint8)
    for a in range(x):
        for b in range(y):
            for d in range(c):
                invert_array[a][b][d] = 255 - copy[a][b][d]
    im = Image.fromarray(invert_array)
    im.show()
    return invert_array


def ft_red(array) -> np.array:
    red_array = np.copy(array)
    red_array[:, :, 1] = 0
    red_array[:, :, 2] = 0
    im = Image.fromarray(red_array)
    im.show()
    return red_array


def ft_green(array) -> np.array:
    green_array = np.copy(array)
    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0
    im = Image.fromarray(green_array)
    im.show()
    return green_array


def ft_blue(array) -> np.array:
    blue_array = np.copy(array)
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    im = Image.fromarray(array)
    im.show()
    return blue_array


def ft_grey(array) -> np.array:
    copy = np.copy(array)
    x, y, z = np.shape(copy)
    grey_array = np.empty([x, y], dtype=np.uint8)
    for a in range(x):
        for b in range(y):
            grey_array[a][b] = np.mean(copy[a][b])
    im = Image.fromarray(grey_array)
    im.show()
    return grey_array
