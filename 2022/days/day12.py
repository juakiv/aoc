from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day12", 2022)

        self.start = None
        self.end = None
        self.grid = []

        for y, line in enumerate(self.data):
            if "S" in line:
                self.start = (line.index("S"), y)
            if "E" in line:
                self.end = (line.index("E"), y)

            self.grid.append([ord(c) - ord("a") for c in line.replace("S", "a").replace("E", "z")])

    def bfs(self, starts: list[tuple[int, int]]) -> int:
        queue = [(start, 0) for start in starts]
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            (x, y), steps = queue.pop(0)
            if (x, y) == self.end:
                return steps

            if (x, y) in visited:
                continue

            visited.add((x, y))

            current_height = self.grid[y][x]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.grid[0]) and 0 <= ny < len(self.grid):
                    neighbor_height = self.grid[ny][nx]
                    if neighbor_height <= current_height + 1:
                        queue.append(((nx, ny), steps + 1))

        return 0

    def part1(self) -> int:
        return self.bfs([self.start])

    def part2(self) -> int:
        starts = [(x, y) for y, row in enumerate(self.grid) for x, height in enumerate(row) if height == 0]
        return self.bfs(starts)


if __name__ == '__main__':
    Solution().run()
