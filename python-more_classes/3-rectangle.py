#!/usr/bin/python3
"""3. String representation"""


class Rectangle:
    """Write a class rectangle"""

    def __init__(self, width=0, height=0):
        """Atributes of the rectangle"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        return (self.__height)

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ __str__ method to print the Rectangle """
        result = ""
        if self.height == 0 or self.width == 0:
            return (result)
        for x in range(self.height):
            for y in range(self.width):
                result += "#"
            result += "\n"
        result = result[0:-1]
        return (result)
