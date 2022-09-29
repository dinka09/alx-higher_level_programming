#!/usr/bin/python3
"""Prints the text"""


def write_file(filename="", text=""):
    """The function reads the text file as well as prints to stdout"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
