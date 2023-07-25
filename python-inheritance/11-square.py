#!/usr/bin/python3
'''creates a new subclass from rectangle'''


BaseGeometry = __import__('7-geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class that defines a Square from Rectangle Class'''

    def __init__(self, size):
        '''initialize variables'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''Method to return the area'''
        return super().area()

    def __str__(self):
        '''special method that returns a printable string'''
        return f("[Square] {self.__size}/{self.__size}")
