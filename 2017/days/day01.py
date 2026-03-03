from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01", 2017)[0]

    def part1(self) -> int:
        total_sum = 0

        for i in range(len(self.data)):
            if self.data[i] == self.data[(i + 1) % len(self.data)]:
                total_sum += int(self.data[i])

        return total_sum

    def part2(self) -> int:
        total_sum = 0

        for i in range(len(self.data)):
            if self.data[i] == self.data[(i + len(self.data) // 2) % len(self.data)]:
                total_sum += int(self.data[i])

        return total_sum


if __name__ == '__main__':
    Solution().run()
