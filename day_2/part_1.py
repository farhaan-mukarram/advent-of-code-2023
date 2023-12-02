import re

from helper import parseFile

FILENAME = "input.txt"

CUBE_CONFIG = {"red": 12, "green": 13, "blue": 14}

PATTERN = r"(\d+)\s+(\w+)"


def is_round_possible(round_details: list[str]):
    round_flag = True

    for item in round_details:
        res = re.search(PATTERN, item.strip())

        if res is not None:
            qty, color = res.group(1), res.group(2)

            round_flag = int(qty) <= CUBE_CONFIG[color]

            if not round_flag:
                return False

    return round_flag


def is_game_possible(rounds: list[str]):
    game_flag = True

    for round in rounds:
        cube_sets = round.split(",")
        round_flag = is_round_possible(cube_sets)

        if not round_flag:
            return False

    return game_flag


if __name__ == "__main__":
    sum_of_game_ids = 0
    lines = parseFile(FILENAME)

    for idx, line in enumerate(lines):
        game_number = idx + 1
        game_info = line.split(":")[-1]
        rounds = game_info.split(";")

        result = is_game_possible(rounds)

        if result:
            sum_of_game_ids += game_number

    print("The sum of all possible game ids is {}".format(sum_of_game_ids))
