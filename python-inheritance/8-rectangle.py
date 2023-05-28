#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry
""" Module:8. Rectangle
    Write a class Rectangle BaseGeometry (based on 7-base_geometry.py)."""


class Rectangle(BaseGeometry):
    """Type class Rectangle inherits from BaseGeometry """

    def __init__(self, width, height):
        """Declaring attributes.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
