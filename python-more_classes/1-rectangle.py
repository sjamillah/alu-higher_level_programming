#!/usr/bin/python3
""" Defines a rectangle """


class Rectangle:
    """ Defines a rectangle """
    
    def __init__(self, width=0, height=0):
        """Initialize the variables"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to get the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width value"""
        if not isinstance(value=0, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method to get the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height value"""
        if not isinstance(value=0, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
