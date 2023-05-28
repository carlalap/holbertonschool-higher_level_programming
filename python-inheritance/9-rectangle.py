#!/usr/bin/python3
""" Module 9. Full rectangle. """


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle (BaseGeometry):
    """Define class Rectangle that inherits from BaseGeometry"""


def __init__(self, width, height):
    """Initialize Atrributes for Rectangle

    Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
    """
    self.integer_validator = width
    self.integer_validator = height
    self.__width = width
    self.__height = height

    def area(self):
        """Returns area of Rectangle"""
        self.__width * self.__height

    def __str__(self):
        """Print string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
