#!/usr/bin/python3
"""Module 9. Student to JSON"""


class Student:
    """class that defines a student by
    first_name, last_name, age)"""

    def __init__(self, first_name, last_name, age):
        """defining attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of a Student instance"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
            }
