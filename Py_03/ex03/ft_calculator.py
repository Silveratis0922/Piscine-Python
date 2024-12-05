class calculator:
    """ Calculator class"""

    def __init__(self, object: list[float]):
        self.obj = object

    def __add__(self, object) -> None:
        # self.obj = [i + object for i in self.obj]
        for i in range(len(self.obj)):
            self.obj[i] += object
        print(self.obj)

    def __mul__(self, object) -> None:
        # self.obj = [i * object for i in self.obj]
        for i in range(len(self.obj)):
            self.obj[i] *= object
        print(self.obj)

    def __sub__(self, object) -> None:
        # self.obj = [i - object for i in self.obj]
        for i in range(len(self.obj)):
            self.obj[i] -= object
        print(self.obj)

    def __truediv__(self, object) -> None:
        try:
            # self.obj = [i // object for i in self.obj]
            for i in range(len(self.obj)):
                self.obj[i] //= object
            print(self.obj)
        except ZeroDivisionError:
            print("Error: You're trying to divide by zero.")


# Tuto list comprehension :

# new_list = [expression for item in iterable if condition]

# - expression : operation de transformation de la list
# - for item in... : l'iteration sur la sequence.
# - if confition : un filtre a un inclure (facultatif).***

# Difference entre for i in iterable et for i in range:

# for i in iterable :      | for i in range()/ for i in range(len(iterable)):
#                          |
# - i est un iterateble    | - i s'incremente de 1 a chaque boucle et permet
#                          |   l'utilisation d'index
