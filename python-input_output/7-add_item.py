#!/usr/bin/python3
"""Module 7. Load, add, save"""
import sys


if __name__ == "__main__":
    """ calling functions"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    # Add command-line arguments to the list
    items.extend(sys.argv[1:])
    # Save the updated list to the filei
    save_to_json_file(items, "add_item.json")
