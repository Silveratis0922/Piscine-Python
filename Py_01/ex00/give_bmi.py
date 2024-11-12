def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculates and returns the BMI for each height-weight pair supplied.
    BMI formula is: Weigh / Height²
    """
    try:
        res = []
        if len(height) != len(weight):
            raise AssertionError()
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or \
               not isinstance(w, (int, float)):
                raise ValueError()
        for h, w in zip(height, weight):
            res.append(w / pow(h, 2))
        return res
    except AssertionError:
        print("Assertion Error: "
              "Height list and weight list does not have the same size.")
    except ValueError:
        print("Value Error: Type in list must be int or float.")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Return a list of Boolean. True if above the limit.
    """
    res = []
    for i in bmi:
        if i > limit:
            res.append(True)
        else:
            res.append(False)
    return res
