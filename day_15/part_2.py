import re
from helper import parseFile


FILENAME = "input.txt"

PATTERN = r"^([^=-]+)(=|-)(\d+)?$"


boxes = {}


def determine_hash(item: str) -> int:
    current_value = 0

    for char in item:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value = current_value % 256

    return current_value


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    initialization_sequence = lines[0].split(",")

    for sequence in initialization_sequence:
        search_result = re.search(PATTERN, sequence)

        if (search_result) is not None:
            label = search_result.group(1)
            operation = search_result.group(2)
            power = search_result.group(3)

            box_number = determine_hash(label)

            if box_number not in boxes:
                boxes[box_number] = {}

            if operation == "=":
                if label not in boxes[box_number]:
                    boxes[box_number][label] = power

                boxes[box_number][label] = power

            elif operation == "-":
                if not (boxes[box_number].get(label, {}) == {}):
                    del boxes[box_number][label]

    sum_of_focusing_power = 0
    for box_number, lenses in boxes.items():
        if len(lenses) > 0:
            items = list(lenses.items())

            for slot_number, lens_info in enumerate(items):
                focal_length = lens_info[1]
                sum_of_focusing_power += (
                    (box_number + 1) * (slot_number + 1) * (int(focal_length))
                )

    print("The total focusing power is:", sum_of_focusing_power)
