from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day13", 2023, "\n\n")

    @staticmethod
    def reflective_rows(rows: list[str], smudges: bool) -> int:
        for i in range(1, len(rows)):
            rows_above = rows[:i][::-1]
            rows_below = rows[i:]

            if smudges:
                if sum(sum(0 if a == b else 1 for a, b in zip(row_above, row_below)) for row_above, row_below in zip(rows_above, rows_below)) == 1:
                    return i
            else:
                if sum(0 if a == b else 1 for a, b in zip(rows_above, rows_below)) == 0:
                    return i

        return 0

    def part1(self) -> int:
        total = 0
        for grid in self.data:
            rows = grid.split("\n")
            total += self.reflective_rows(rows, False) * 100

            # transpose to check columns
            rows = list(zip(*rows))
            total += self.reflective_rows(rows, False)

        return total


    def part2(self) -> int:
        total = 0
        for grid in self.data:
            rows = grid.split("\n")
            total += self.reflective_rows(rows, True) * 100

            # transpose to check columns
            rows = list(zip(*rows))
            total += self.reflective_rows(rows, True)

        return total


if __name__ == '__main__':
    Solution().run()
