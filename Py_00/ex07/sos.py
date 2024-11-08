import sys


morse = {" ": "/ ",
         "A": ".- ",
         "B": "-... ",
         "C": "-.-. ",
         "D": "-.. ",
         "E": ". ",
         "F": "..-. ",
         "G": "--. ",
         "H": ".... ",
         "I": ".. ",
         "J": ".--- ",
         "K": "-.- ",
         "L": ".-.. ",
         "M": "-- ",
         "N": "-. ",
         "O": "--- ",
         "P": ".--. ",
         "Q": "--.- ",
         "R": ".-. ",
         "S": "... ",
         "T": "- ",
         "U": "..- ",
         "V": "...- ",
         "W": ".-- ",
         "X": "-..- ",
         "Y": "-.-- ",
         "Z": "--.. ",
         "1": ".---- ",
         "2": "..--- ",
         "3": "...-- ",
         "4": "....- ",
         "5": "..... ",
         "6": "-.... ",
         "7": "--... ",
         "8": "---.. ",
         "9": "----. ",
         "0": "----- "}


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError
        res = ""
        for i in sys.argv[1]:
            res = res + morse[i.upper()]
        res = res.rstrip()
        print(res)
    except KeyError:
        print("Assertion Error: the arguments are bad")
    except AssertionError:
        print("Assertion Error: the arguments are bad")


if __name__ == "__main__":
    main()
