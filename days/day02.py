from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02")

    def part1(self) -> int:
        raise NotImplementedError()

    def part2(self) -> int:
        raise NotImplementedError()

if __name__ == '__main__':
    Solution().run()