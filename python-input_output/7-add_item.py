#!/usr/bin/python3
'''script that adds all args to a python list and saves them to a file'''


import sys
from json import load as load_from_json_file, dump as save_to_json_file


if __name__ == "__main__":
    try:
        loadFile = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadFile = []

        loadFile.append(sys.argv[1:])
    save_to_json_file(loadFile, open("add_item.json", 'w'))
