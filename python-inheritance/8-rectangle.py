#!/usr/bin/python3
# Write a class Rectangle inherits from (7-base_geometry.py)
""" Module 8.
    BaseGeometry = __import__('7-base_geometry.py').BaseGeometry
    Rectangle Class rectangle. """


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry
""" Importing function base geometry 7 """


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry """

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
