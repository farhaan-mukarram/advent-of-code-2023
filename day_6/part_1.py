import re
import math
from helper import parseFile

FILENAME = "input.txt"


def evaluate_quadratic_equation(a: int, b: int, c: int, x: int):
    res = (a * (x**2)) + (b * x) + c
    return res


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    race_times = re.findall(r"\d+", lines[0])
    race_distances = re.findall(r"\d+", lines[1])
    product_of_combinations = 1

    for i in range(len(race_times)):
        time = int(race_times[i])
        distance = int(race_distances[i])

        # ((-b - sqrt(b^2 - 4ac)) / 2a
        min_time = math.trunc(((time) - math.sqrt((time**2 - (4 * distance)))) / (2))

        # ((-b + sqrt(b^2 - 4ac)) / 2a
        max_time = math.trunc(((time) + math.sqrt((time**2 - (4 * distance)))) / (2))

        if evaluate_quadratic_equation(a=1, b=-1 * time, c=distance, x=min_time) >= 0:
            min_time += 1

        if evaluate_quadratic_equation(a=1, b=-1 * time, c=distance, x=max_time) >= 0:
            max_time -= 1

        product_of_combinations *= (max_time + 1) - min_time

    print("The product of combinations is:", product_of_combinations)
