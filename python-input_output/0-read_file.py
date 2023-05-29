#!/usr/bin/python3
def read_file(filename=""):
    """Module function that reads a text file (UTF8)"""
    

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
