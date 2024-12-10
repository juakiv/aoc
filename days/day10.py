from typing import Tuple, Set

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day10")

        self.possible_trail_starts: list[Tuple[int, int]] = []
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if int(self.data[y][x]) == 0:
                    self.possible_trail_starts.append((x, y))

    def check_neighbors(self, x: int, y: int, current_step: int, visited: Set[Tuple[int, int]], part: int) -> int:
        if int(self.data[y][x]) == 9 and (x, y) not in visited:
            if part == 1:
                visited.add((x, y))
            return 1

        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        return sum(
            self.check_neighbors(x + dx, y + dy, current_step + 1, visited, part)
            for dx, dy in deltas
            if 0 <= x + dx < len(self.data[0]) and 0 <= y + dy < len(self.data) and int(
                self.data[y + dy][x + dx]) == current_step + 1
        )

    def part1(self) -> int:
        return sum(
            self.check_neighbors(x, y, 0, set(), 1)
            for x, y in self.possible_trail_starts
        )

    def part2(self) -> int:
        return sum(
            self.check_neighbors(x, y, 0, set(), 2)
            for x, y in self.possible_trail_starts
        )


if __name__ == '__main__':
    Solution().run()
