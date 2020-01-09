#!/usr/bin/python3
class Square:
    """
        Square Class with a private instance
            size: the size of the square
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

    def area(self):
        return (self.__size * self.__size)
