import re

from helper import parseFile

FILENAME = "input.txt"

CUBE_CONFIG = {"red": 12, "green": 13, "blue": 14}

PATTERN = r"(\d+)\s+(\w+)"

game_details = {}


def is_round_possible(round_details: list[str], game_number: int):
    round_flag = True

    for item in round_details:
        res = re.search(PATTERN, item.strip())

        if res is not None:
            qty, color = res.group(1), res.group(2)

            round_flag = int(qty) <= CUBE_CONFIG[color]

            if game_number not in game_details.keys():
                game_details[game_number] = {"red": 0, "green": 0, "blue": 0}

            game_details[game_number][color] = max(
                int(qty), game_details[game_number][color]
            )

    return round_flag


def is_game_possible(rounds: list[str], game_number: int):
    game_flag = True

    for round in rounds:
        cube_sets = round.split(",")
        round_flag = is_round_possible(round_details=cube_sets, game_number=game_number)

        game_flag = round_flag

    return game_flag


def get_game_power(game_number: int):
    power = 1

    for item in game_details[game_number].values():
        power *= item if item > 0 else 1

    return power


if __name__ == "__main__":
    sum_of_game_powers = 0
    lines = parseFile(FILENAME)

    for idx, line in enumerate(lines):
        game_number = idx + 1
        game_info = line.split(":")[-1]
        rounds = game_info.split(";")

        result = is_game_possible(rounds=rounds, game_number=game_number)

        game_power = get_game_power(game_number)
        sum_of_game_powers += game_power

    print("The sum of all game powers is {}".format(sum_of_game_powers))
