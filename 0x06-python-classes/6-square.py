#!/usr/bin/python3
class Square:
    """Square Class with a private instance
    """
    def __init__(self, size=0, position=(0, 0)):
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

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int and type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    """GET - SIZE
    """
    @property
    def size(self):
        return (self.__size)
    """SET - SIZE
    """
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """GET - POSITION
    """
    @property
    def position(self):
        return (self.__position)
    """SET - POSITION
    """
    @position.setter
    def position(self, value):
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int and type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    """METHOD
    """
    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
