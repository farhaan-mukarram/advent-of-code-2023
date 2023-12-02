from helper import parseFile

FILENAME = "input.txt"

LETTERS_TO_DIGITS_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}

WINDOW_SIZE = 5


def convertToDigit(item: str):
    if item.isdigit():
        return item
    else:
        return str(LETTERS_TO_DIGITS_MAP[item])


if __name__ == "__main__":
    lines = parseFile(FILENAME)

    sum = 0

    for line in lines:
        i = 0
        matches = []

        while i < len(line):
            buffer = ""
            prev_buffer = ""

            for j in range(WINDOW_SIZE):
                prev_buffer = buffer
                buffer = line[i : i + j + 1]

                if buffer == prev_buffer:
                    break
                if len(buffer) == 1 and buffer.isdigit():
                    matches.append(buffer)
                elif buffer in LETTERS_TO_DIGITS_MAP.keys():
                    matches.append(buffer)

            i += 1

        first_item, last_item = matches[0], matches[-1]
        number = convertToDigit(first_item) + convertToDigit(last_item)
        sum += int(number)

    print("The sum of all calibration values is {}".format(sum))
