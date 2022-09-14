#!/usr/bin/python3
"""
Square class to define the size of the given obejed
"""


class Square:
    """
    Square class to define the square size of the object
    """
    def __init__(self, size=0):
        """
        Args:
        size: attributes defined in integer
        """
        self.size = size

    @property
    def size(self):
        """
        instance to get object size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter for an object
        """
        if type(value) != int:
            """
            checks if the attribute is not an integer
            """
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        value of the area of the object
        """
        a = self.__size * self.__size
        return a
