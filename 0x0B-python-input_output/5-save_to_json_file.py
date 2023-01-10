#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)https://github.com/NwabuezeFranklin/alx-higher_level_programming/blob/master/0x0B-python-input_output/6-load_from_json_file.py
