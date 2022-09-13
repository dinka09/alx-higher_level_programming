#!/usr/bin/python3
"""
Args:
size: size of the object's are wich should be considered as the private and setted as private attributes
"""
class Square:
    def __init__(self, size):
        self.__size = size
