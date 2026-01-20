from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01", 2021)

        self.measurements: list[int] = [int(line) for line in self.data]

    def part1(self) -> int:
        increased_measurements = 0

        for i, measurement in enumerate(self.measurements[1:], start=1):
            if measurement > self.measurements[i - 1]:
                increased_measurements += 1

        return increased_measurements

    def part2(self) -> int:
        increased_measurements = 0

        for i in range(3, len(self.measurements)):
            previous_window_sum = sum(self.measurements[i - 3:i])
            current_window_sum = sum(self.measurements[i - 2:i + 1])

            if current_window_sum > previous_window_sum:
                increased_measurements += 1

        return increased_measurements


if __name__ == '__main__':
    Solution().run()
