#!/usr/bin/python3
""" Module 9. Full rectangle - that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry:
    """ BaseGeomety Class """
    def area(self):
        raise NotImplementedError("Subclass must implement area() method")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be a positive integer")


class Rectangle(BaseGeometry):
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
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
