def variance(iterable):
    size = len(iterable)
    mean = sum(iterable) / size
    return sum(pow(i - mean, 2) for i in iterable) / size


def standard_deviation(iterable):
    size = len(iterable)
    mean = sum(iterable) / size
    return (sum(pow(i - mean, 2) for i in iterable) / size) ** 0.5


def quartile(iterable):
    """ Return the 25e and 75e percentile."""
    iterable = sorted(iterable)
    size = len(iterable)
    first = (size - 1) // 4
    third = (size - 1) // 4 * 3

    if size % 4:
        return list((float(iterable[first]), float(iterable[third])))
    else:
        one = (iterable[first] + iterable[first + 1]) / 2
        two = (iterable[third] + iterable[third + 1] / 2)
        return list((float(one), float(two)))


def median(iterable):
    """ Return the median of iterable or 50e percentile."""
    iterable = sorted(iterable)
    size = len(iterable)
    index = (size - 1) // 2

    if size % 2:
        return iterable[index]
    else:
        return (iterable[index] + iterable[index + 1]) / 2


def ft_statistics(*args: any, **kwargs: any) -> None:
    if args:
        first = []
        for arg in args:
            first.append(arg)
        if kwargs:
            for value in kwargs.values():
                match value:
                    case "mean":
                        print("mean :", sum(first) / len(first))
                    case "median":
                        print("median:", median(first))
                    case "quartile":
                        print("quartile :", quartile(first))
                    case "std":
                        print("std :", standard_deviation(first))
                    case "var":
                        print("var :", variance(first))
                    case _:
                        pass
    elif not args:
        for kwarg in kwargs:
            print("ERROR")
