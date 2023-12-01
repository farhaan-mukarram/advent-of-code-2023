import sys


def parseFile(filename):
    filepath = sys.path[0] + "/" + filename

    with open(filepath, "r") as file:
        lines = file.read().splitlines()

    return lines
