import sys

def check_words(str):
    print("ok")


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError
        S = sys.argv[1]
        #N = int(sys.argv[2])
        iterable = sys.argv[1].split(" ")
        print(S)
        print(iterable)
        #filtered_string = filter(check_words, S)
        #print(list(filtered_string))
    except ValueError as e:
        print("AssertionError: the arguments are bad")
    except AssertionError:
        print("AssertionError: the arguments are bad 2")


if __name__ == "__main__":
    main()
