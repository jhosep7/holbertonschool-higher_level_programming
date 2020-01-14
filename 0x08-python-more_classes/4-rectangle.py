#!/usr/bin/python3
"""class that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            Perimeter = 0
        else:
            Perimeter = (self.__width + self.__height) * 2
        return Perimeter

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        MyWidth = "#" * self.width
        rectangle = MyWidth
        for x in range(self.height - 1):
            rectangle += "\n" + MyWidth
        return (rectangle)

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))
