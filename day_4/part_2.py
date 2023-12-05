import re
from helper import parseFile

FILENAME = "input.txt"

table = []

card_count_cache = {}


# Recursive function to count the number of cards for a given index
def count_cards(index: int):
    num_of_cards = len(table[index])

    if num_of_cards == 0:
        return 1

    else:
        total_num_of_cards = 1

        for i in range(index + 1, index + num_of_cards + 1):
            total_num_of_cards += count_cards(i)

        return total_num_of_cards


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    total_number_of_cards = 0

    # fill table
    for line_idx, line in enumerate(lines):
        winning_cards = set()
        players_winning_cards = set()
        winning_numbers, player_numbers = line.split(":")[-1].split("|")

        winning_numbers_list = re.findall(r"\d+", winning_numbers)
        player_numbers_list = re.findall(r"\d+", player_numbers)

        for number in winning_numbers_list:
            winning_cards.add(number)

        for number in winning_cards:
            if number in player_numbers_list:
                players_winning_cards.add(number)

        table.append(players_winning_cards)

    for i in range(len(table)):
        total_number_of_cards += count_cards(i)

    print("The total number of cards is {}".format(total_number_of_cards))
