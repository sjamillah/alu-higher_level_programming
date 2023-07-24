#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Defines a square """

     def __init__(self, size=0, position=(0, 0)):
         """ Method to initialize the square object """
         self.__size = size
         self.__position = position

    def area(self):
        square_area = self.__size ** 2
        return square_area

    @property
    def size(self):
        """ Method to return the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Method to show position of the size """
            return self.__position

    @position.setter
    def position(self, value):
        """ Method to set position """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                    for l in range(self.__size):
                print("#" * self.__size)
