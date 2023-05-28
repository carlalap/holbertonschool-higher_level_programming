#!/usr/bin/python3
""" Module 8-Rectangle.py """
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


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
