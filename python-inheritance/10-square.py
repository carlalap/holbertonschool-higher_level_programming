#!/usr/bin/python3
""" Module 10-square.py- BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """super Square class, inherits from rectangle """
    def __init__(self, size):
        """Initialize new square"""

        self.integer_validator("size", size)
        super().__init__(size.size)
        self.__size = size
    
    def area(self):
        """ Calculator area """
        return super().area()
