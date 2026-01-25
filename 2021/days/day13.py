from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day13", 2021, "\n\n")

        self.dots: set[tuple[int, int]] = set()
        self.folds: list[tuple[str, int]] = []
        for line in self.data[0].split("\n"):
            x, y = map(int, line.split(","))
            self.dots.add((x, y))

        for line in self.data[1].split("\n"):
            axis, value = line.split("=")
            self.folds.append((axis[-1], int(value)))

    @staticmethod
    def fold(axis: str, value: int, dots: set[tuple[int, int]]) -> set[tuple[int, int]]:
        new_dots: set[tuple[int, int]] = set()
        for x, y in dots:
            if axis == "x" and x > value:
                x = value - (x - value)
            elif axis == "y" and y > value:
                y = value - (y - value)
            new_dots.add((x, y))

        return new_dots

    def part1(self) -> int:
        return len(self.fold(self.folds[0][0], self.folds[0][1], self.dots.copy()))

    def part2(self) -> str:
        dots = self.dots.copy()

        for axis, value in self.folds:
            dots = self.fold(axis, value, dots)

        max_x = max(x for x, y in dots)
        max_y = max(y for x, y in dots)

        for y in range(max_y + 1):
            line = ""
            for x in range(max_x + 1):
                if (x, y) in dots:
                    line += " # "
                else:
                    line += "   "
            print(line)

        return "See the console output above. :)"


if __name__ == '__main__':
    Solution().run()
