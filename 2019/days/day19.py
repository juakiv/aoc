from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day19", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    @staticmethod
    def is_in_beam(program: list[int], x: int, y: int) -> bool:
        computer = IntcodeComputer(program, [x, y])
        return computer.run_full()[-1] == 1

    def part1(self) -> int:
        count = 0

        for y in range(50):
            for x in range(50):
                count += self.is_in_beam(self.nums, x, y)

        return count

    def part2(self) -> int:
        x, y = 0, 100

        while True:
            while not self.is_in_beam(self.nums, x, y):
                x += 1

            if self.is_in_beam(self.nums, x + 99, y - 99):
                return x * 10000 + (y - 99)

            y += 1


if __name__ == '__main__':
    Solution().run()
