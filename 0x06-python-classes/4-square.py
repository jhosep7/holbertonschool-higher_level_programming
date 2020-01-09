#!/usr/bin/python3
class Square:
    """Square Class with a private instance
    """
    def __init__(self, size=0):
        """
        Arguments:
            size: the size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """GET
    """
    @property
    def size(self):
        return (self.__size)
    """SET
    """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size ** 2)
