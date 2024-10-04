import sys



# if len(sys.argv) > 1:
#     try:
#         try:
#             test = int(sys.argv[1])
#         except ValueError as error:
#             raise AssertionError("argument is not an integer")
#         if len(sys.argv) != 2:
#             raise AssertionError("more then one argument is provided")
#         if test % 2 == 0:
#             print("I'm Even.")
#         else:
#             print("I'm Odd.")
#     except AssertionError as e:
#          print(f"AssertionError: {e}")

if len(sys.argv) > 1: 
    try:
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")
        arg = int(sys.argv[1])

        if arg % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError as error:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {e}")