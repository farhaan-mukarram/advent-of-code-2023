import re
from helper import parseFile


FILENAME = "input.txt"

directions_map = {}


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    instructions = lines[:1][0]
    directions = lines[1:]

    starting_node = "AAA"
    ending_node = "ZZZ"

    for line in directions:
        matches = re.findall(r"[A-Z]+", line)

        if len(matches) > 0:
            node, left_element, right_element = matches

            directions_map[node] = {"L": left_element, "R": right_element}

    current_node = starting_node
    number_of_steps = 0

    while current_node != "ZZZ":
        for instruction in instructions:
            next_node = directions_map[current_node][instruction]

            current_node = directions_map[current_node][instruction]
            number_of_steps += 1

    print("Steps required to reach ZZZ:", number_of_steps)
