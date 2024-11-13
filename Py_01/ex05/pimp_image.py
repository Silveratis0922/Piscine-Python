import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    """
    Invert the colors of an image by returning an array
    with the modified colors
    """
    try:
        if not isinstance(array, np.ndarray):
            raise AssertionError("Need numpy array.")
        if not array.ndim == 3:
            raise AssertionError("Need 3D array.")
        copy = np.copy(array)
        x, y, c = np.shape(copy)
        invert_array = np.empty([x, y, c], dtype=np.uint8)
        for a in range(x):
            for b in range(y):
                for d in range(c):
                    invert_array[a][b][d] = 255 - copy[a][b][d]
        plt.imshow(invert_array)
        plt.show()
        return invert_array
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


def ft_red(array) -> np.array:
    """
    Applies a red filter to an image, suppressing the green and blue channels.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise AssertionError("Need numpy array.")
        if not array.ndim == 3:
            raise AssertionError("Need 3D array.")
        red_array = np.copy(array)
        red_array[:, :, 1] = 0
        red_array[:, :, 2] = 0
        plt.imshow(red_array)
        plt.show()
        return red_array
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


def ft_green(array) -> np.array:
    """
    Applies a green filter to an image, suppressing the red and blue channels.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise AssertionError("Need numpy array.")
        if not array.ndim == 3:
            raise AssertionError("Need 3D array.")
        green_array = np.copy(array)
        green_array[:, :, 0] = 0
        green_array[:, :, 2] = 0
        plt.imshow(green_array)
        plt.show()
        return green_array
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


def ft_blue(array) -> np.array:
    """
    Applies a blue filter to an image, suppressing the green and red channels.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise AssertionError("Need numpy array.")
        if not array.ndim == 3:
            raise AssertionError("Need 3D array.")
        blue_array = np.copy(array)
        blue_array[:, :, 0] = 0
        blue_array[:, :, 1] = 0
        plt.imshow(blue_array)
        plt.show()
        return blue_array
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


def ft_grey(array) -> np.array:
    """
    Converts an image to grayscale using the average of the color channels.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise AssertionError("Need numpy array.")
        if not array.ndim == 3:
            raise AssertionError("Need 3D array.")
        copy = np.copy(array)
        x, y, z = np.shape(copy)
        grey_array = np.empty([x, y], dtype=np.uint8)
        for a in range(x):
            for b in range(y):
                grey_array[a][b] = np.mean(copy[a][b])
        plt.imshow(grey_array, cmap='grey')
        plt.show()
        return grey_array
    except AssertionError as e:
        print(f"{AssertionError.__main__}: {e}")
