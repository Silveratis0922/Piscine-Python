import sys


def read_arg(arg) -> None:
    """
    Documentation
    """
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punct = 0
    print("The text contains", len(arg), "characters:")
    for i in arg:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isdigit():
            digit += 1
        elif i.isspace():
            space += 1
        else:
            punct += 1
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    try:
        if len(sys.argv) == 1:
            print("What is the text to count ?")
            text = sys.stdin.readline()
            read_arg(text)
        elif len(sys.argv) == 2:
            read_arg(sys.argv[1])
        else:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
