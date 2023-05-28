#!/usr/bin/python3
""" Module 9. Full rectangle - that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class BaseGeometry:
    """ BaseGeomety Class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Define class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Atrributes for Rectangle

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of Rectangle"""
        self.__width * self.__height

    def __str__(self):
        """return string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
