from collections import deque
from heapq import heappop, heappush

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day15", 2021)

        self.grid: list[list[int]] = [[int(x) for x in line] for line in self.data]
        self.start: tuple[int, int] = (0, 0)
        self.end: tuple[int, int] = (len(self.grid) - 1, len(self.grid[0]) - 1)

    @staticmethod
    def dijkstra(start: tuple[int, int], end: tuple[int, int], grid: list[list[int]]) -> int:
        risk_level = 0
        queue = [(0, start)]
        visited = set()

        while queue:
            risk, (x, y) = heappop(queue)

            if (x, y) in visited:
                continue

            visited.add((x, y))

            if (x, y) == end:
                risk_level = risk
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    heappush(queue, (risk + grid[nx][ny], (nx, ny)))

        return risk_level

    def part1(self) -> int:
        return self.dijkstra(self.start, self.end, self.grid)

    def part2(self) -> int:
        full_grid: list[list[int]] = []

        height, width = len(self.grid), len(self.grid[0])
        for y in range(height * 5):
            row = []
            for x in range(width * 5):
                base = self.grid[y % height][x % width]
                inc = (y // height) + (x // width)
                row.append((base + inc - 1) % 9 + 1)
            full_grid.append(row)

        new_end = (len(full_grid) - 1, len(full_grid[0]) - 1)
        return self.dijkstra(self.start, new_end, full_grid)


if __name__ == '__main__':
    Solution().run()
