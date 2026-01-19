from collections import deque

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day18", 2022)

        self.cubes: list[tuple[int, int, int]] = []
        for line in self.data:
            x, y, z = map(int, line.split(","))
            self.cubes.append((x, y, z))

    def part1(self) -> int:
        total_surface_area = 0

        for x, y, z in self.cubes:
            exposed_faces = 6
            for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
                neighbor = (x + dx, y + dy, z + dz)
                if neighbor in self.cubes:
                    exposed_faces -= 1
            total_surface_area += exposed_faces

        return total_surface_area

    def part2(self) -> int:
        total_exterior_surface_area = 0

        min_x, max_x = min([x for x, _, _ in self.cubes]) - 1, max([x for x, _, _ in self.cubes]) + 1
        min_y, max_y = min([y for _, y, _ in self.cubes]) - 1, max([y for _, y, _ in self.cubes]) + 1
        min_z, max_z = min([z for _, _, z in self.cubes]) - 1, max([z for _, _, z in self.cubes]) + 1

        queue = deque([(min_x, min_y, min_z)])
        visited = { (min_x, min_y, min_z) }

        while queue:
            x, y, z = queue.popleft()

            for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
                nx, ny, nz = x + dx, y + dy, z + dz
                neighbor = (nx, ny, nz)

                if neighbor in self.cubes:
                    total_exterior_surface_area += 1
                    continue

                if min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return total_exterior_surface_area


if __name__ == '__main__':
    Solution().run()
