from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02")

    @staticmethod
    def is_safe_report(report: str) -> int:
        levels = [int(level) for level in report.split()]
        should_increase = True if levels[0] < levels[1] else False

        for a, b in zip(levels[:-1], levels[1:]):
            if should_increase and a > b or not should_increase and a < b or not (1 <= abs(a - b) <= 3):
                return 0

        return 1

    def part1(self) -> int:
        safe_count = 0

        for report in self.data:
            safe_count += self.is_safe_report(report)

        return safe_count

    def part2(self) -> int:
        
        return 0

if __name__ == '__main__':
    Solution().run()