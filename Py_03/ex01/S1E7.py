from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Docstring Method from Baratheon"""
        self.is_alive = False

    def __str__(self):
        return f"({self.family_name}, {self.eyes}, {self.hairs})"

class Lannister(Character):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Docstring Method from Lannister."""
        self.is_alive = False

    def __str__(self):
        return f"({self.family_name}, {self.eyes}, {self.hairs})"

    #decorator
    #def create_lannester():