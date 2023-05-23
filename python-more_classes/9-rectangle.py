#!/usr/bin/python3
"""9. A square is a rectangle"""


class Rectangle:
    """Write a class rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Atributes of the rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

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
                result += str(self.print_symbol)
            result += "\n"
        result = result[:-1]
        return (result)

    def __repr__(self):
        """ return a string representation of the rectangle  """
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    def __del__(self):
        """prints a message when an instance is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method returns the biggest rectangle based on the area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        elif rect_1.area() < rect_2.area():
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Class method that returns a new Rectangle instance """
        return Rectangle(size, size)
