from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day17", 2020)

        self.active_cubes = set()
        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                if char == "#":
                    self.active_cubes.add((x, y, 0))

    def part1(self) -> int:
        active_cubes = self.active_cubes.copy()
        neighbors = [(dx, dy, dz) for dx in (-1, 0, 1) for dy in (-1, 0, 1) for dz in (-1, 0, 1) if not (dx == 0 and dy == 0 and dz == 0)]

        for cycle in range(6):
            counts = defaultdict(int)

            for x, y, z in active_cubes:
                for dx, dy, dz in neighbors:
                    counts[(x + dx, y + dy, z + dz)] += 1

            new_active = set()
            for cube, n in counts.items():
                if cube in active_cubes and n in (2, 3):
                    new_active.add(cube)
                elif cube not in active_cubes and n == 3:
                    new_active.add(cube)

            active_cubes = new_active

        return len(active_cubes)

    def part2(self) -> int:
        active_cubes = set((x, y, 0, 0) for x, y, z in self.active_cubes)
        neighbors = [
            (dx, dy, dz, dw)
            for dx in (-1, 0, 1)
            for dy in (-1, 0, 1)
            for dz in (-1, 0, 1)
            for dw in (-1, 0, 1)
            if not (dx == 0 and dy == 0 and dz == 0 and dw == 0)
        ]

        for cycle in range(6):
            counts = defaultdict(int)

            for x, y, z, w in active_cubes:
                for dx, dy, dz, dw in neighbors:
                    counts[(x + dx, y + dy, z + dz, w + dw)] += 1

            new_active = set()
            for cube, n in counts.items():
                if cube in active_cubes and n in (2, 3):
                    new_active.add(cube)
                elif cube not in active_cubes and n == 3:
                    new_active.add(cube)

            active_cubes = new_active

        return len(active_cubes)


if __name__ == '__main__':
    Solution().run()
