import sys


if len(sys.argv) > 1:
    try:
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")
        arg = float(sys.argv[1])

        if arg % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")
