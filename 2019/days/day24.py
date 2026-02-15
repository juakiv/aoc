from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day24", 2019)

        self.grid: list[list[str]] = [list(line) for line in self.data]
        self.bugs: set[tuple[int, int]] = set()
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == "#":
                    self.bugs.add((x, y))

    @staticmethod
    def simulate_bugs(grid: list[list[str]]) -> list[list[str]]:
        new_grid = [row.copy() for row in grid]

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                adjacent = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < len(grid[y]) and 0 <= new_y < len(grid):
                        if grid[new_y][new_x] == "#":
                            adjacent += 1

                if grid[y][x] == "#" and adjacent != 1:
                    new_grid[y][x] = "."
                elif grid[y][x] == "." and adjacent in (1, 2):
                    new_grid[y][x] = "#"

        return new_grid

    def part1(self) -> int:
        grid = [row.copy() for row in self.grid]
        seen = set()

        while True:
            grid_tuple = tuple(tuple(row) for row in grid)
            if grid_tuple in seen:
                break
            seen.add(grid_tuple)
            grid = self.simulate_bugs(grid)

        biodiversity_rating = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "#":
                    biodiversity_rating += 2 ** (y * len(grid[y]) + x)

        return biodiversity_rating

    @staticmethod
    def count_neighbors(x: int, y: int, level: int, all_bugs: set[tuple[int, int, int]]) -> int:
        count = 0

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy

            if (new_x < 0 and (1, 2, level - 1) in all_bugs) or \
                (new_x > 4 and (3, 2, level - 1) in all_bugs) or \
                (new_y < 0 and (2, 1, level - 1) in all_bugs) or \
                (new_y > 4 and (2, 3, level - 1) in all_bugs):
                count += 1

            elif new_x == 2 and new_y == 2:
                if x == 1:
                    count += sum(1 for i in range(5) if (0, i, level + 1) in all_bugs)
                elif x == 3:
                    count += sum(1 for i in range(5) if (4, i, level + 1) in all_bugs)
                elif y == 1:
                    count += sum(1 for i in range(5) if (i, 0, level + 1) in all_bugs)
                elif y == 3:
                    count += sum(1 for i in range(5) if (i, 4, level + 1) in all_bugs)

            else:
                if (new_x, new_y, level) in all_bugs:
                    count += 1

        return count

    def part2(self) -> int:
        bugs = set((x, y, 0) for x, y in self.bugs)

        for _ in range(200):
            new_bugs = set()
            levels = { level for _, _, level in bugs }
            min_level, max_level = min(levels) - 1, max(levels) + 1

            for level in range(min_level, max_level + 1):
                for y in range(5):
                    for x in range(5):
                        if x == 2 and y == 2:
                            continue

                        count = self.count_neighbors(x, y, level, bugs)
                        if (x, y, level) in bugs and count == 1:
                            new_bugs.add((x, y, level))
                        elif (x, y, level) not in bugs and count in (1, 2):
                            new_bugs.add((x, y, level))

            bugs = new_bugs

        return len(bugs)


if __name__ == '__main__':
    Solution().run()
