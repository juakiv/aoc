import math

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09", 2021)

        self.grid: list[list[int]] = [list(map(int, list(line))) for line in self.data]

    def part1(self) -> int:
        risk_level = 0

        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                neighbors = []
                if x > 0:
                    neighbors.append(self.grid[y][x - 1])
                if x < len(row) - 1:
                    neighbors.append(self.grid[y][x + 1])
                if y > 0:
                    neighbors.append(self.grid[y - 1][x])
                if y < len(self.grid) - 1:
                    neighbors.append(self.grid[y + 1][x])

                if all(value < n for n in neighbors):
                    risk_level += value + 1

        return risk_level

    def part2(self) -> int:
        basin_sizes = []
        visited = set()

        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                if (x, y) in visited or value == 9:
                    continue

                basin_size = 0
                to_visit = [(x, y)]

                while to_visit:
                    current_x, current_y = to_visit.pop()
                    if (current_x, current_y) in visited:
                        continue

                    visited.add((current_x, current_y))
                    basin_size += 1

                    for new_x, new_y in [(current_x - 1, current_y), (current_x + 1, current_y), (current_x, current_y - 1), (current_x, current_y + 1)]:
                        if 0 <= new_x < len(row) and 0 <= new_y < len(self.grid):
                            if (new_x, new_y) not in visited and self.grid[new_y][new_x] != 9:
                                to_visit.append((new_x, new_y))

                basin_sizes.append(basin_size)

        return math.prod(sorted(basin_sizes, reverse=True)[:3])


if __name__ == '__main__':
    Solution().run()
