#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Defines a square """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
       
    @property
    def size(self):
        """ Method to return the size value """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        square_area = self.__size ** 2
        return square_area

    def my_print(self):
        if size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(self.__size):
            print("#", end="")
