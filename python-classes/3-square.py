#!/usr/bin/python3
"""This is a Class Square that defines a square (based on 2-square.py) """


class Square:
    """Define Class Square"
    """
    def __init__(self, size=0):
        """ Conditional atrribute for the Class that represents a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        """Return area of the Square"""
    def area(self):
        return (self.__size ** 2)
