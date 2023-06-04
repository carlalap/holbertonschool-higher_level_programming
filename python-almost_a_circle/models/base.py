#!/usr/bin/python3
"module Base class"

import json

class Base:
    """ this class is the -base- of all
    other classes in this project. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
