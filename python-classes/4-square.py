#!/usr/bin/python3
""" Defines a square """

class Square:
    """ Creates a private instance """
    
    def __init__(self, size=0):
        """ Initializes size """
            self.__size = size

    def area(self):
        square_area = self.__size ** 2
        return square_area

    @property
    def size(self):
        """ Method to eturns the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
