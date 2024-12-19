from functools import cache
from typing import Set

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day19")

        self.patterns: list[str] = []
        self.designs: list[str] = []

        for i, line in enumerate(self.data):
            if i == 0:
                self.patterns = line.split(", ")
            elif line != "":
                self.designs.append(line)

    @cache
    def is_design_possible(self, design: str) -> bool:
        if design == "":
            return True

        return any(
            (self.is_design_possible(design[len(pattern):]) if design.startswith(pattern) else False) for pattern in
            self.patterns)

    def part1(self) -> int:
        possible_designs = 0

        for design in self.designs:
            if self.is_design_possible(design):
                possible_designs += 1

        return possible_designs

    @cache
    def amount_possible_designs(self, design: str) -> int:
        if design == "":
            return 1

        return sum(
            (self.amount_possible_designs(design[len(pattern):]) for pattern in self.patterns if design.startswith(pattern)))

    def part2(self) -> int:
        possible_designs = 0

        for design in self.designs:
            possible_designs += self.amount_possible_designs(design)

        return possible_designs


if __name__ == '__main__':
    Solution().run()
