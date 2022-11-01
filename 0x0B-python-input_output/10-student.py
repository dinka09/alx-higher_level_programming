#!/usr/bin/python3
"""method for student creation"""


class Student:
    """Student obj, interesting how you don't have to directly
    test for strings in a loop"""

    def __init__(self, first_name, last_name, age):
        """Class attribute instatiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To json"""
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary