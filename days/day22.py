from collections import defaultdict
from typing import Tuple

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day22")

        self.prices: list[list[int]] = []

    def calculate_secret_number(self, initial: int, times: int) -> int:
        secret = initial
        price: list[int] = []

        for _ in range(times):
            secret = ((secret * 64) ^ secret) % 16777216
            secret = ((secret // 32) ^ secret) % 16777216
            secret = ((secret * 2048) ^ secret) % 16777216

            price.append(secret % 10)

        self.prices.append(price)

        return secret

    def part1(self) -> int:
        return sum(self.calculate_secret_number(int(num), 2000) for num in self.data)

    def part2(self) -> int:
        differences = [[b - a for a, b in zip(price, price[1:])] for price in self.prices]

        result = defaultdict(int)

        for i, diffs in enumerate(differences):
            seen_pattern = set()
            for j in range(len(diffs) - 3):
                pattern = tuple(diffs[j:j + 4])
                if pattern not in seen_pattern:
                    seen_pattern.add(pattern)
                    result[pattern] += self.prices[i][j + 4]

        return max(result.values())


if __name__ == '__main__':
    Solution().run()
