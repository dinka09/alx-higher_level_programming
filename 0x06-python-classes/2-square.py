#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """The __init__ method uses the keyword self to
        assign the values passed as
        arguments to the object attributes self."""
        if type(siz) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
