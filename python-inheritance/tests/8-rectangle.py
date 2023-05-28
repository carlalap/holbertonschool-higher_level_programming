#!/usr/bin/python3

"""Class rectangle """

BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


Class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """Declaring attributes """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
