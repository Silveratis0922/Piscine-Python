from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class Character"""
    def __init__(self, first_name, is_alive=True):
        "Your docstring for Parent Constructor"
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Abstract method that must be in the child class"""
        pass


class Stark(Character):
    """Your docstring for Class Stark"""
    def __init__(self, first_name, is_alive=True) -> None:
        """Your doctstring for Stark Constructor"""
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """Your docstring for Method"""
        self.is_alive = False
