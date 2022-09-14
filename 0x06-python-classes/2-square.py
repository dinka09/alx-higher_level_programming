#!/usr/bin/python3
"""
This the class to define the square
"""


class Square:
    """
    The square class to define the square size
    """
    def __init__(self, size=0):
        """The __init__ method uses the keyword self to
        assign the values passed as
        arguments to the object attributes self."""
        if type(size) != int:
            """
            define the size if not equal to the given integers
            """
            raise TypeError("size must be an integer")
        elif size < 0:
            """
            When the given attributes is less than zero
            """
            raise ValueError("size must be >= 0")
        self.__size = size
