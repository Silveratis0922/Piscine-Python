import sys

def check_words(number):
    if number % 2 == 0:
    #if len(str) > int(sys.argv[2]):
        return True
    return False

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError
        iterable = sys.argv[1].split(" ")
        N = int(sys.argv[2])
        test = ft_filter(check_words, iterable)
        official = filter(check_words, iterable)
        print(test)
        print(official)
    except ValueError as e:
        print("AssertionError: the arguments are bad")
    except AssertionError:
        print("AssertionError: the arguments are bad 2")


if __name__ == "__main__":
    main()
