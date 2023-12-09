import re
from threading import local
from helper import parseFile


FILENAME = "input.txt"


def all_zeroes(sequence: list[int]):
    for number in sequence:
        if number != 0:
            return False

    return True


def extrapolate_previous_value(sequence: list[int]):
    differences = [sequence]

    current_difference = sequence

    while not all_zeroes(current_difference):
        i = 0
        local_diffs = []

        while i < len(current_difference) - 1:
            diff = current_difference[i + 1] - current_difference[i]
            local_diffs.append(diff)
            i += 1

        differences.append(local_diffs)
        current_difference = local_diffs

    j = len(differences) - 1

    while j > 0:
        diff = differences[j][-1]
        item_to_add = differences[j - 1][-1] + diff
        differences[j - 1].append(item_to_add)
        j -= 1

    return differences[0][-1]


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    sum_of_extrapolated_values = 0

    for line in lines:
        sequence = re.findall(r"-?\d+", line)
        integer_sequence = [int(x) for x in sequence]
        integer_sequence.reverse()
        extrapolated_value = extrapolate_previous_value(sequence=integer_sequence)
        sum_of_extrapolated_values += extrapolated_value

    print("The sum of all extrapolated values is:", sum_of_extrapolated_values)
