#!/usr/bin/python3
"""Prints the text"""


def append_write(filename="", text=""):
    """The function appends the text to file and returns the number of the text"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
