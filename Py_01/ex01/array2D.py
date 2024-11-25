import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Return an array with slicing python method from start to end parameter.
    """
    try:
        if not isinstance(family, list):
            raise AssertionError("First argument have to be a list.")
        family_array = np.array(family)
        if not family_array.ndim == 2:
            raise AssertionError("Array have to be in 2 dimensions.")
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Start and End have to be an int.")
        print("My shape is:", family_array.shape)
        new_array = family_array[start:end]
        print("My new shape is :", new_array.shape)
        return new_array.tolist()
    except ValueError:
        print(f"{ValueError.__name__}: list dont have same the size.")
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
