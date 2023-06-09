#!/usr/bin/python3
"""This is a Class Square that defines a square (based on 2-square.py) """


class Square:
    """Define Class Square"
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Conditional atrribute for the Class that represents a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the current size of the square """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the current position of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """Return area of the Square"""
    def area(self):
        return (self.__size ** 2)

    """Public instance Prints in stdout the square #"""
    def my_print(self):
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
