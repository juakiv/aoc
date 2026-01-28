from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day03", 2020)

        self.grid: list[list[str]] = [list(line) for line in self.data]

    def part1(self) -> int:
        width, height = len(self.grid[0]), len(self.grid)
        x = trees = 0

        for _y in range(height):
            if self.grid[_y][x % width] == '#':
                trees += 1
            x += 3

        return trees

    def part2(self) -> int:
        width, height = len(self.grid[0]), len(self.grid)
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        result = 1

        for slope_x, slope_y in slopes:
            x = y = trees = 0
            while y < height:
                if self.grid[y][x % width] == '#':
                    trees += 1
                x += slope_x
                y += slope_y
            result *= trees

        return result


if __name__ == '__main__':
    Solution().run()
