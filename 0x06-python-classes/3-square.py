#!/usr/bin/python3
"""
Square class to define thhe size of the given object
"""


class Square:
    """
    The square class to define the size of the object
    """
    def __init__(self, size=0):
        """
        size: attributes that define the size of the object with integer value
        """
        if type(size) != int:
            """
            check if the given attribute
            in not required integer
            """
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        to get the value of the size of the object
        """
        ar = self.__size * self.__size
        return ar
