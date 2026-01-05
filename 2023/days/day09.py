from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09", 2023)

        self.reports: list[list[int]] = [list(map(int, line.split())) for line in self.data]

    def next_value(self, report: list[int], backwards = False) -> int:
        if all(num == 0 for num in report):
            return 0

        difference = [report[i + 1] - report[i] for i in range(len(report) - 1)]

        if backwards:
            return report[0] - self.next_value(difference, backwards)
        else:
            return report[-1] + self.next_value(difference, backwards)

    def part1(self) -> int:
        total = 0

        for report in self.reports:
            total += self.next_value(report, False)

        return total

    def part2(self) -> int:
        total = 0
        for report in self.reports:
            total += self.next_value(report, True)
        return total


if __name__ == '__main__':
    Solution().run()
