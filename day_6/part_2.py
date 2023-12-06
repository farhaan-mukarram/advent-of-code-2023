import re
import math
from helper import parseFile

FILENAME = "input.txt"


def evaluate_quadratic_equation(a: int, b: int, c: int, x: int):
    res = (a * (x**2)) + (b * x) + c
    return res


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    race_time = int("".join(re.findall(r"\d+", lines[0])))
    race_distance = int("".join(re.findall(r"\d+", lines[1])))

    # ((-b - sqrt(b^2 - 4ac)) / 2a
    min_time = math.trunc(
        ((race_time) - math.sqrt((race_time**2 - (4 * race_distance)))) / (2)
    )

    # ((-b + sqrt(b^2 - 4ac)) / 2a
    max_time = math.trunc(
        ((race_time) + math.sqrt((race_time**2 - (4 * race_distance)))) / (2)
    )

    if (
        evaluate_quadratic_equation(a=1, b=-1 * race_time, c=race_distance, x=min_time)
        >= 0
    ):
        min_time += 1

    if (
        evaluate_quadratic_equation(a=1, b=-1 * race_time, c=race_distance, x=max_time)
        >= 0
    ):
        max_time -= 1

    number_of_combinations = (max_time + 1) - min_time
