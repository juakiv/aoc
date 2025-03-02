from typing import Tuple

from solution.base import SolutionBase
import re


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day03")

    def part1(self) -> int:
        regular_expression = r"mul\((\d+),(\d+)\)"
        matches: list[Tuple[int, int]] = []

        for case in self.data:
            matches.extend(re.findall(regular_expression, case))

        return sum([int(x) * int(y) for x, y in matches])

    def part2(self) -> int:
        regular_expression = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
        sum_of_multiplications = 0
        is_do = True

        for case in self.data:
            for x, y, do, dont in re.findall(regular_expression, case):
                if do or dont:
                    is_do = True if do else False
                else:
                    sum_of_multiplications += int(x) * int(y) if is_do else 0

        return sum_of_multiplications


if __name__ == '__main__':
    Solution().run()
