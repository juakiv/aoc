from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02", 2017)

        self.rows: list[list[int]] = []
        for line in self.data:
            self.rows.append(list(map(int, line.split())))

    def part1(self) -> int:
        checksum = 0

        for row in self.rows:
            checksum += max(row) - min(row)

        return checksum

    def part2(self) -> int:
        total = 0

        for row in self.rows:
            for i in range(len(row)):
                for j in range(i + 1, len(row)):
                    if row[i] % row[j] == 0:
                        total += row[i] // row[j]
                    elif row[j] % row[i] == 0:
                        total += row[j] // row[i]

        return total


if __name__ == '__main__':
    Solution().run()
