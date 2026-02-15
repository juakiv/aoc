from collections import Counter
from itertools import combinations

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02", 2018)

    def part1(self) -> int:
        repeating_twice = 0
        repeating_thrice = 0

        for line in self.data:
            counts = Counter(line)

            if 2 in counts.values():
                repeating_twice += 1

            if 3 in counts.values():
                repeating_thrice += 1

        return repeating_twice * repeating_thrice

    def part2(self) -> str:
        common_letters = ""
        id_pairs = combinations(self.data, 2)

        for id1, id2 in id_pairs:
            differences = sum(1 for char1, char2 in zip(id1, id2) if char1 != char2)

            if differences == 1:
                common_letters = "".join(char1 for char1, char2 in zip(id1, id2) if char1 == char2)
                break

        return common_letters


if __name__ == '__main__':
    Solution().run()
