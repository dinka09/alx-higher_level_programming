#!/usr/bin/python3
"""
Square class to define size of the object
"""


class Square:
    """
    class of the squaare to be determine the size
    """
    def __init__(self, size=0):
        """
        Args:

        size (attributes of the object given in integer)
        """
        self.self = size

        @property
        def size(self):
            """
            calling the methods to get the size value
            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            setter to value
            """
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """
            value of the object area
            """
            a = self.__size * self.__size
            return a

        def my_print(self):
            """
            To print the value
            """
            if self.__size == 0:
                print("")
            for i in range(0, self.__size):
                print("#", end="")
            print()
