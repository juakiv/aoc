from collections import Counter
from functools import cmp_to_key

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07", 2023)

        self.hands = []
        for line in self.data:
            hand, bid = line.split(" ")
            self.hands.append((hand, int(bid)))

    @staticmethod
    def type_of_hand(hand: str) -> int:
        cards = sorted(Counter(hand).values(), reverse=True)

        if cards[0] == 5:
            return 6  # Five of a Kind
        elif cards[0] == 4:
            return 5  # Four of a Kind
        elif cards[0] == 3 and cards[1] == 2:
            return 4  # Full House
        elif cards[0] == 3:
            return 3  # Three of a Kind
        elif cards[0] == 2 and cards[1] == 2:
            return 2  # Two Pair
        elif cards[0] == 2:
            return 1  # One Pair

        return 0

    @staticmethod
    def type_of_hand_with_joker(hand: str) -> int:
        jokers = hand.count("J")
        hand = hand.replace("J", "")
        cards = sorted(Counter(hand).values(), reverse=True)

        if not cards:
            cards = [0]

        if cards[0] + jokers == 5:
            return 6  # Five of a Kind
        elif cards[0] + jokers == 4:
            return 5  # Four of a Kind
        elif cards[0] + jokers == 3 and cards[1] == 2:
            return 4  # Full House
        elif cards[0] + jokers == 3:
            return 3  # Three of a Kind
        elif cards[0] == 2 and (jokers or cards[1] == 2):
            return 2  # Two Pair
        elif cards[0] == 2 or jokers:
            return 1  # One Pair
        return 0

    def compare_hands(self, hand1: tuple[str, int], hand2: tuple[str, int]) -> int:
        type1 = self.type_of_hand(hand1[0])
        type2 = self.type_of_hand(hand2[0])

        cards_order = "23456789TJQKA"

        if type1 > type2:
            return 1

        if type1 < type2:
            return -1

        for card1, card2 in zip(hand1[0], hand2[0]):
            if card1 == card2:
                continue

            return 1 if cards_order.index(card1) > cards_order.index(card2) else -1

        return 0

    def compare_hands_with_joker(self, hand1: tuple[str, int], hand2: tuple[str, int]) -> int:
        type1 = self.type_of_hand_with_joker(hand1[0])
        type2 = self.type_of_hand_with_joker(hand2[0])

        cards_order = "J23456789TQKA"

        if type1 > type2:
            return 1

        if type1 < type2:
            return -1

        for card1, card2 in zip(hand1[0], hand2[0]):
            if card1 == card2:
                continue

            return 1 if cards_order.index(card1) > cards_order.index(card2) else -1

        return 0

    def part1(self) -> int:
        sorted_hands = sorted(self.hands, key=cmp_to_key(self.compare_hands))
        total_winnings = 0

        for rank, (hand, bid) in enumerate(sorted_hands, start=1):
            total_winnings += rank * bid

        return total_winnings

    def part2(self) -> int:
        sorted_hands = sorted(self.hands, key=cmp_to_key(self.compare_hands_with_joker))
        total_winnings = 0

        for rank, (hand, bid) in enumerate(sorted_hands, start=1):
            total_winnings += rank * bid

        return total_winnings


if __name__ == '__main__':
    Solution().run()
