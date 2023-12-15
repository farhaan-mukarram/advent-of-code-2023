from helper import parseFile


FILENAME = "input.txt"


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

    sum_of_hashes = 0

    for item in initialization_sequence:
        item_hash = determine_hash(item)
        sum_of_hashes += item_hash

    print("The sum of all hashes is :", sum_of_hashes)
