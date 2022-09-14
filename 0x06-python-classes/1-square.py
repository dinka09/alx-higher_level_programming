#!/usr/bin/python3
"""
Args:
size: size of the object's are wich should be
considered as the private and setted as private attributes
"""


class Square:
    """
    Square class to define square
    """
    def __init__(self, size):
        """
        This methods will determine the size of the given objects
        """
        self.__size = size
