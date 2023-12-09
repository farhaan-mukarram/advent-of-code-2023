import functools
from helper import parseFile


FILENAME = "input.txt"

CARD_STRENGTHS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

card_info = {
    "five_kind": [],
    "four_kind": [],
    "full_house": [],
    "three_kind": [],
    "two_pair": [],
    "one_pair": [],
    "high_card": [],
}


def get_hand_type(hand: str):
    number_of_joker_cards = 0
    card_count = {}

    for card in hand:
        if card == "J":
            number_of_joker_cards += 1
        else:
            card_count[card] = card_count.get(card, 0) + 1

    # sort by frequency in desc order
    sorted_card_count_by_frequency = dict(
        sorted(card_count.items(), key=lambda x: x[1], reverse=True),
    )

    # Determine card with max frequency (defaults to "J")
    card_with_max_frequency = (
        list(sorted_card_count_by_frequency.keys())[0]
        if len(list(sorted_card_count_by_frequency.keys())) > 0
        else "J"
    )

    # Add number of joker cards to card with max frequency
    sorted_card_count_by_frequency[card_with_max_frequency] = (
        sorted_card_count_by_frequency.get(card_with_max_frequency, 0)
        + number_of_joker_cards
    )

    # five of a kind
    if len(sorted_card_count_by_frequency) == 1:
        return "five_kind"

    if len(sorted_card_count_by_frequency) == 5:
        return "high_card"

    # four of a kind or full-house
    if len(sorted_card_count_by_frequency) == 2:
        max_card_frequency = list(sorted_card_count_by_frequency.values())[0]

        if (max_card_frequency) == 4:
            return "four_kind"

        return "full_house"

    # three of a kind or two-pair
    if len(sorted_card_count_by_frequency) == 3:
        max_card_frequency = list(sorted_card_count_by_frequency.values())[0]

        if (max_card_frequency) == 3:
            return "three_kind"

        return "two_pair"

    return "one_pair"


def determine_stronger_hand(
    hand_1_tuple: tuple[str, str], hand_2_tuple: tuple[str, str]
):
    hand_1, hand_2 = hand_1_tuple[0], hand_2_tuple[0]

    for i in range(len(hand_1)):
        hand_1_card = hand_1[i]
        hand_2_card = hand_2[i]

        # hand_1 is stronger
        if CARD_STRENGTHS[hand_1_card] > CARD_STRENGTHS[hand_2_card]:
            return 1

        # hand_2 is stronger
        elif CARD_STRENGTHS[hand_2_card] > CARD_STRENGTHS[hand_1_card]:
            return -1

    return 0


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    total_winnings = 0

    for line in lines:
        hand, bid = line.split(" ")
        hand_type = get_hand_type(hand=hand)
        card_info[hand_type].append((hand, bid))

    max_rank = len(lines)

    rank = max_rank
    for key, val in card_info.items():
        if len(val) > 0:
            sorted_val = sorted(
                val, key=functools.cmp_to_key(determine_stronger_hand), reverse=True
            )

            for hand, bid in sorted_val:
                total_winnings += int(bid) * rank
                rank -= 1

    print("Total winnings:", total_winnings)
