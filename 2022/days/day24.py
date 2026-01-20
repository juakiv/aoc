import math
from collections import deque

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day24", 2022)

        self.start = (self.data[0].index('.'), 0)
        self.end = (self.data[-1].index('.'), len(self.data) - 1)

        self.grid = [[cell for cell in row] for row in self.data]
        self.walls = set()

        self.blizzards = []
        for y, row in enumerate(self.data):
            for x, cell in enumerate(row):
                if cell == '#':
                    self.walls.add((x, y))
                if cell in '^v<>':
                    self.blizzards.append((x, y, cell))

        self.blizzard_states = []

        self.height, self.width = len(self.data), len(self.data[0])
        cycle_length = math.lcm(self.height - 2, self.width - 2)

        for time in range(cycle_length):
            occupied = set()
            for x, y, direction in self.blizzards:
                if direction == ">":
                    x = 1 + (x - 1 + time) % (self.width - 2)
                elif direction == "<":
                    x = 1 + (x - 1 - time) % (self.width - 2)
                elif direction == "v":
                    y = 1 + (y - 1 + time) % (self.height - 2)
                elif direction == "^":
                    y = 1 + (y - 1 - time) % (self.height - 2)
                occupied.add((x, y))
            self.blizzard_states.append(occupied)

    def travel(self, start: tuple[int, int], end: tuple[int, int], time: int) -> int:
        queue = deque([(start[0], start[1], time)])
        visited = set()

        while queue:
            x, y, time = queue.popleft()
            if (x, y) == end:
                return time

            next_time = time + 1
            blizzards = self.blizzard_states[next_time % len(self.blizzard_states)]

            for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < self.width and 0 <= ny < self.height) or (nx, ny) in self.walls or (nx, ny) in blizzards:
                    continue
                state = (nx, ny, next_time % len(self.blizzard_states))
                if state in visited:
                    continue
                visited.add(state)
                queue.append((nx, ny, next_time))

        return 0

    def part1(self) -> int:
        return self.travel(self.start, self.end, 0)

    def part2(self) -> int:
        start_to_end = self.travel(self.start, self.end, 0)
        end_to_start = self.travel(self.end, self.start, start_to_end)
        start_to_end_again = self.travel(self.start, self.end, end_to_start)
        return start_to_end_again


if __name__ == '__main__':
    Solution().run()
