from itertools import combinations

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01", 2020)

        self.nums: list[int] = [int(line) for line in self.data]

    def part1(self) -> int:
        for a, b in combinations(self.nums, 2):
            if a + b == 2020:
                return a * b

        return 0

    def part2(self) -> int:
        for a, b, c in combinations(self.nums, 3):
            if a + b + c == 2020:
                return a * b * c
        return 0


if __name__ == '__main__':
    Solution().run()
