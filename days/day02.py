from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02")

    @staticmethod
    def is_safe_report(levels: list[int]) -> int:
        should_increase = True if levels[0] < levels[1] else False

        for a, b in zip(levels[:-1], levels[1:]):
            if should_increase and a > b or not should_increase and a < b or not (1 <= abs(a - b) <= 3):
                return False

        return True

    def part1(self) -> int:
        safe_count = 0

        for report in self.data:
            levels = [int(level) for level in report.split()]
            safe_count += int(self.is_safe_report(levels))

        return safe_count

    def part2(self) -> int:
        dampened_safe_count = 0
        for report in self.data:
            levels = [int(level) for level in report.split()]
            is_safe = self.is_safe_report(levels)

            for i in range(len(levels)):
                is_safe = is_safe or self.is_safe_report([x for idx, x in enumerate(levels) if idx != i])

            dampened_safe_count += int(is_safe)

        return dampened_safe_count

if __name__ == '__main__':
    Solution().run()