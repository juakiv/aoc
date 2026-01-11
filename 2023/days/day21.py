from collections import deque

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day21", 2023)

        self.starting_position: tuple[int, int] = (0, 0)
        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                if char == "S":
                    self.starting_position = (x, y)

    def bfs(self):
        visited = {}
        queue = deque([(self.starting_position, 0)])

        while queue:
            (x, y), steps = queue.popleft()

            if (x, y) in visited:
                continue

            visited[(x, y)] = steps

            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(self.data[0]) and 0 <= new_y < len(self.data):
                    if self.data[new_y][new_x] == "#" or (new_x, new_y) in visited:
                        continue

                    queue.append(((new_x, new_y), steps + 1))

        return visited

    def part1(self) -> int:
        visited_points = self.bfs()
        return len([step for step in visited_points.values() if step < 65 and step % 2 == 0])

    def part2(self) -> int:
        n = 202300
        visited_points = self.bfs()

        odd_tiles = len([step for step in visited_points.values() if step % 2 == 1])
        even_tiles = len([step for step in visited_points.values() if step % 2 == 0])
        odd_corners = len([step for step in visited_points.values() if step % 2 == 1 and step > 65])
        even_corners = len([step for step in visited_points.values() if step % 2 == 0 and step > 65])

        # a geometric solution to AoC 2023 day 21 part 2
        # github.com/villuna/aoc2023/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
        return ((n + 1) * (n + 1)) * odd_tiles + (n * n) * even_tiles - (n + 1) * odd_corners + n * even_corners


if __name__ == '__main__':
    Solution().run()
