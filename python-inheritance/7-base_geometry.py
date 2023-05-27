#!/usr/bin/python3
""" Module:7. Integer validator
    Write a class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """Attribute area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
