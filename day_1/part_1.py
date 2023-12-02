from helper import parseFile

FILENAME = "input.txt"

if __name__ == "__main__":
    lines = parseFile(FILENAME)

    sum = 0

    for line in lines:
        digits = [x for x in line if x.isdigit()]

        number = digits[0] + digits[-1]
        sum += int(number)

    print("The sum of all calibration values is {}".format(sum))
