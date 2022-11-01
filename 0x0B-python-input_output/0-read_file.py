#!/usr/bin/python3
"""Prints the text"""


def read_file(filename=""):
    """The function reads the text file as well as prints to stdout"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
