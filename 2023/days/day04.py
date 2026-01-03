from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day04", 2023)

        self.cards: dict[int, dict[str, list[int]]] = {}

        for line in self.data:
            card, numbers = line.split(": ")
            card_number = int(card.replace("Card ", ""))
            winning_numbers, drawn_numbers = numbers.split(" | ")

            self.cards[card_number] = {
                "winning_numbers": [int(x) for x in winning_numbers.split(" ") if x != ""],
                "drawn_numbers": [int(x) for x in drawn_numbers.split(" ") if x != ""],
            }

    def part1(self) -> int:
        total_points: int = 0

        for numbers in self.cards.values():
            total_matches = set(numbers["winning_numbers"]) & set(numbers["drawn_numbers"])
            total_points += 2 ** (len(total_matches) - 1) if total_matches else 0

        return total_points

    def part2(self) -> int:
        card_counts = [1] * len(self.cards)

        for index, (card_id, numbers) in enumerate(self.cards.items()):
            total_matches = set(numbers["winning_numbers"]) & set(numbers["drawn_numbers"])

            for card_copy in range(len(total_matches)):
                card_counts[index + card_copy + 1] += card_counts[index]

        return sum(card_counts)


if __name__ == '__main__':
    Solution().run()
