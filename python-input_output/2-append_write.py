#!/usr/bin/python3
""" Module 2. Append to a file"""


def append_write(filename="", text=""):
    """ Function that appends a string
    at the end of a text file (UTF8)"""
    with open(filename, "a", encoding="utf-8") as file:
        file.seek(0, 2)  # move the file pointer to the end of the file
        n_chars = file.write(text)
    return n_chars
