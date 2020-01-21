#!/usr/bin/python3
"""class BaseGeometry.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""class Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
