#!/usr/bin/python3


class Square:
    """ A class that defines a square by its size """

    def __str__(self):

        if self.size == 0:
            return ("")

        rtn = "\n"* self.position[1]
        for i in range(0, self.size):
                rtn += " " * self.position[0]
                rtn += "#" * self.size
            if i is not (self.size - 1):
                rtn += "\n"

        return rtn

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the variables """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Method to returns the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        square_area = self.__size ** 2
        return square_area

    @property
    def position(self):
        """ Method that returns the position value """
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
        """ Method that prints a # square according to the size value """
        if self.size == 0:
            print("")
            return

            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
