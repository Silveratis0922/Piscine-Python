import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError
        # aquarium_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
        iterable = sys.argv[1].split(" ")
        N = int(sys.argv[2])
        test = ft_filter(lambda word: len(word) > N, iterable)
        official = filter(lambda word: len(word) > N, iterable)
        print(list(test))
        print(list(official))
    except ValueError:
        print("AssertionError: the arguments are bad")
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    # print(filter.__doc__)
    # print(ft_filter.__doc__)
    main()
