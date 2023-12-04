import re
from helper import parseFile

FILENAME = "input.txt"


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    sum_of_card_points = 0

    for line in lines:
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

        if len(players_winning_cards) > 0:
            card_points = 2 ** (len(players_winning_cards) - 1)
            sum_of_card_points += card_points

    print("The card pile is worth {} points".format(sum_of_card_points))
