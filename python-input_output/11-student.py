#!/usr/bin/python3
"""Module 11. Student to disk and reload"""


class Student:
    """class Student that defines a student by:
    (based on 10-student.py)"""
    def __init__(self, first_name, last_name, age):
        """Defining attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of the Student.
        If attrs is a list of strings, represents only those
        attributes included in the list."""
        if attrs is None:
            return self.__dict__

        student_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                student_dict[attr] = getattr(self, attr)

        return student_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
