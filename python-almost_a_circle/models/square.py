#!/usr/bin/python3
"""Model 10. And now, the Square!"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size=None, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """read size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Print Str format """
        st = "[Square] ({:d}) {:d}/{:d} - {:d}"
        st = st.format(self.id, self.x, self.y, self.width)
        return st

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
            else:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]
