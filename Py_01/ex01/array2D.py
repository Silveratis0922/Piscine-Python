import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        family_array = np.array(family)
        print("My shape is:", family_array.shape)
        new_array = family_array[start:end]
        print("My new shape is :", new_array.shape)
        return new_array
    except ValueError:
        print("error")
