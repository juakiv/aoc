from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day04")

    def part1(self) -> int:
        xmas_count = 0
        deltas = [(y, x) for y in range(-1, 2) for x in range(-1, 2) if y != 0 or x != 0]

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                for dy, dx in deltas:
                    if 0 <= y + 3 * dy < len(self.data) and 0 <= x + 3 * dx < len(self.data[y]) and \
                        self.data[y][x] == "X" and \
                        self.data[y + 1 * dy][x + 1 * dx] == "M" and \
                        self.data[y + 2 * dy][x + 2 * dx] == "A" and \
                        self.data[y + 3 * dy][x + 3 * dx] == "S":
                            xmas_count += 1

        return xmas_count

    def part2(self) -> int:
        x_mas_count = 0
        deltas = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

        for y in range(1, len(self.data) - 1):
            for x in range(1, len(self.data[y]) - 1):

                if self.data[y][x] == "A":
                    corner_letters = [self.data[y + dy][x + dx] for dy, dx in deltas]
                    x_mas_count += corner_letters.count("M") == 2 and \
                                   corner_letters.count("S") == 2 and \
                                   corner_letters[0] != corner_letters[1]

        return x_mas_count


if __name__ == '__main__':
    Solution().run()
