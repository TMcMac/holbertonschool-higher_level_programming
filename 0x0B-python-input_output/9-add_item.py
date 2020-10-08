#!/usr/bin/python3
"""Saves Args to list and then to JSON File"""
import os
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    existing_file = "add_item.json"
    new_list = load_from_json_file(existing_file)
except:
    new_list = []

for i in range(len(argv)):
    """
    Cycles through args and adds them to list
    """
    if str(type(argv[i])) == "_io.TextIOWrapper":
        """
        if its a file we need to open it
        """
        new_item = load_from_json_file(argv[i])
        new_list.append(new_item)
    elif i > 0:
        new_list.append(argv[i])

save_to_json_file(new_list, "add_item.json")
