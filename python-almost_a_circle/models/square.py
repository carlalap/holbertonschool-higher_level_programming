#!/usr/bin/python3
"""Model 10. And now, the Square!"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
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
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                elif i == 3:
                    self.y = j
            else:
                if "id" in kwargs:
                    self.id = kwargs["id"]
                if "size" in kwargs:
                    self.size = kwargs["size"]
                if "x" in kwargs:
                    self.x = kwargs["x"]
                if "y" in kwargs:
                    self.y = kwargs["y"]
