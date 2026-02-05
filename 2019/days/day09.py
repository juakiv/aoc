from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09", 2019)

        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    def part1(self) -> int:
        return IntcodeComputer(self.nums.copy(), [1]).run()[0]

    def part2(self) -> int:
        return IntcodeComputer(self.nums.copy(), [2]).run()[0]


if __name__ == '__main__':
    Solution().run()
