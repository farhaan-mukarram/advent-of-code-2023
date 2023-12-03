import re
from helper import parseFile

FILENAME = "input.txt"

SPECIAL_CHAR_REGEX = r"[^\.\d\s]"

DIRECTIONS = {
    "NORTH": {"line_index": -1, "character_index": 0},
    "SOUTH": {"line_index": 1, "character_index": 0},
    "WEST": {"line_index": 0, "character_index": -1},
    "EAST": {"line_index": 0, "character_index": 1},
    "NORTHEAST": {"line_index": -1, "character_index": 1},
    "NORTHWEST": {"line_index": -1, "character_index": -1},
    "SOUTHEAST": {"line_index": 1, "character_index": 1},
    "SOUTHWEST": {"line_index": 1, "character_index": -1},
}


def get_search_directions(
    line_index: int, character_index: int, total_number_of_lines: int, line_length
):
    search_directions = None

    # first line
    if line_index == 0:
        # first character
        if character_index == 0:
            search_directions = [
                DIRECTIONS["EAST"],
                DIRECTIONS["SOUTH"],
                DIRECTIONS["SOUTHEAST"],
            ]

        # last character
        elif character_index == line_length - 1:
            search_directions = [
                DIRECTIONS["WEST"],
                DIRECTIONS["SOUTH"],
                DIRECTIONS["SOUTHWEST"],
            ]

        else:
            search_directions = [
                DIRECTIONS["WEST"],
                DIRECTIONS["EAST"],
                DIRECTIONS["SOUTH"],
                DIRECTIONS["SOUTHEAST"],
                DIRECTIONS["SOUTHWEST"],
            ]

    # last line
    elif line_index == total_number_of_lines - 1:
        # first character
        if character_index == 0:
            search_directions = [
                DIRECTIONS["NORTH"],
                DIRECTIONS["EAST"],
                DIRECTIONS["NORTHEAST"],
            ]

        # last character
        elif character_index == line_length - 1:
            search_directions = [
                DIRECTIONS["NORTH"],
                DIRECTIONS["WEST"],
                DIRECTIONS["NORTHWEST"],
            ]

        else:
            search_directions = [
                DIRECTIONS["NORTH"],
                DIRECTIONS["WEST"],
                DIRECTIONS["EAST"],
                DIRECTIONS["NORTHEAST"],
                DIRECTIONS["NORTHWEST"],
            ]

    else:
        # first character
        if character_index == 0:
            search_directions = [
                DIRECTIONS["NORTH"],
                DIRECTIONS["SOUTH"],
                DIRECTIONS["EAST"],
                DIRECTIONS["NORTHEAST"],
                DIRECTIONS["SOUTHEAST"],
            ]

        # last character
        elif character_index == line_length - 1:
            search_directions = [
                DIRECTIONS["NORTH"],
                DIRECTIONS["SOUTH"],
                DIRECTIONS["WEST"],
                DIRECTIONS["NORTHWEST"],
                DIRECTIONS["SOUTHWEST"],
            ]

        else:
            search_directions = [value for value in DIRECTIONS.values()]

    return search_directions


def search_for_special_chars(lines: list[str], line_index: int, character_index: int):
    special_char_flag_array = []

    search_directions = get_search_directions(
        line_index=line_index,
        character_index=character_index,
        total_number_of_lines=len(lines),
        line_length=len(lines[0]),
    )

    for direction in search_directions:
        relative_line_index, relative_character_index = (
            direction["line_index"],
            direction["character_index"],
        )

        item = lines[relative_line_index + line_index][
            relative_character_index + character_index
        ]
        search_result = re.search(SPECIAL_CHAR_REGEX, item)

        if search_result is not None:
            special_char_flag_array.append(True)
        else:
            special_char_flag_array.append(False)

    return True in special_char_flag_array


if __name__ == "__main__":
    sum_of_part_numbers = 0
    lines = parseFile(FILENAME)
    part_numbers = []

    for line_idx, line in enumerate(lines):
        buffer = ""
        is_part_number_array = []

        for char_idx, char in enumerate(line):
            if char.isdigit():
                buffer += char

                is_part_number = search_for_special_chars(
                    lines=lines, line_index=line_idx, character_index=char_idx
                )

                is_part_number_array.append(is_part_number)

                if (
                    char_idx == len(line) - 1
                    and len(buffer) > 0
                    and True in is_part_number_array
                ):
                    part_numbers.append(int(buffer))

            else:
                if len(buffer) > 0 and True in is_part_number_array:
                    part_numbers.append(int(buffer))

                buffer = ""
                is_part_number_array = []

    for number in part_numbers:
        sum_of_part_numbers += number

    print("The sum of part numbers is:", sum_of_part_numbers)
