from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day04", 2025)

        self.map: dict[tuple[int, int], str] = {
            (x, y): value
            for y, line in enumerate(self.data)
            for x, value in enumerate(line)
            if value == "@"
        }
        self.adjacent_cells = [(-1, -1,), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def part1(self) -> int:
        accessible_cells: set[tuple[int, int]] = set()

        for (x, y), value in self.map.items():
            if sum(1 for dx, dy in self.adjacent_cells if self.map.get((x + dx, y + dy))) < 4:
                accessible_cells.add((x, y))

        return len(accessible_cells)

    def part2(self) -> int:
        total_removed_rolls = 0

        while True:
            cells_to_remove: set[tuple[int, int]] = set()

            for (x, y), value in self.map.items():
                if sum(1 for dx, dy in self.adjacent_cells if self.map.get((x + dx, y + dy))) < 4:
                    cells_to_remove.add((x, y))

            if not cells_to_remove:
                break

            for cell in cells_to_remove:
                del self.map[cell]

            total_removed_rolls += len(cells_to_remove)

        return total_removed_rolls


if __name__ == '__main__':
    Solution().run()
