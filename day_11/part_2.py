from helper import parseFile


FILENAME = "input.txt"


def is_empty_row(row: str):
    for char in row:
        if char != ".":
            return False

    return True


def is_empty_col(lines, col_idx: int):
    i = 0

    while i < len(lines):
        if lines[i][col_idx] != ".":
            return False
        i += 1

    return True


def determine_distance_between_galaxies(
    galaxy_1: tuple[int, int], galaxy_2: tuple[int, int], lines, debug=False
):
    current_line_idx, current_char_idx = galaxy_1
    other_line_idx, other_char_idx = galaxy_2
    delta_x = abs(current_line_idx - other_line_idx)
    delta_y = abs(current_char_idx - other_char_idx)

    col_start = min(current_char_idx, other_char_idx)
    col_end = max(current_char_idx, other_char_idx)

    # add empty cols to delta_x
    while col_start <= col_end:
        if col_start in empty_cols.keys():
            delta_x += 1000000 - 1
        col_start += 1

    row_start = min(current_line_idx, other_line_idx)
    row_end = max(current_line_idx, other_line_idx)

    # add empty rows to delta_y
    while row_start <= row_end:
        if row_start in empty_rows.keys():
            delta_y += 1000000 - 1
        row_start += 1

    return delta_x + delta_y


galaxy_locations = []
galaxy_distances = {}

empty_rows = {}
empty_cols = {}


if __name__ == "__main__":
    lines = parseFile(FILENAME)

    # populate galaxies_locations
    for line_idx, line in enumerate(lines):
        if is_empty_row(line):
            empty_rows[line_idx] = line_idx

        for char_idx, char in enumerate(line):
            if is_empty_col(lines, col_idx=char_idx):
                empty_cols[char_idx] = char_idx

            if char == "#":
                galaxy_locations.append((line_idx, char_idx))

    i = 0

    # Loop through all locations
    while i < len(galaxy_locations):
        current_galaxy = galaxy_locations[i]
        j = 0

        # Find distances between current and other galaxies
        while j < len(galaxy_locations):
            if i != j:
                other_galaxy = galaxy_locations[j]
                distance = determine_distance_between_galaxies(
                    current_galaxy, other_galaxy, lines
                )

                max_galaxy_num = max(i, j)
                min_galaxy_num = min(i, j)
                result = str((max_galaxy_num, min_galaxy_num))
                galaxy_distances[result] = distance

            j += 1
        i += 1

    sum_of_galaxy_distances = 0
    for distance in galaxy_distances.values():
        sum_of_galaxy_distances += distance

    print("The sum of galaxy distances is:", sum_of_galaxy_distances)
