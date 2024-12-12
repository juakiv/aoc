from typing import Tuple, Set

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day12")

        self.regions: list[Set[Tuple[int, int]]] = []

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if not any((x, y) in region for region in self.regions):
                    self.regions.append(self.find_same_type_neighbors(x, y, set()))

    def find_same_type_neighbors(self, x: int, y: int, neighbors: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        if (x, y) in neighbors:
            return neighbors

        neighbors.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(self.data[0]) and 0 <= new_y < len(self.data) and self.data[new_y][new_x] == self.data[y][x]:
                neighbors = self.find_same_type_neighbors(new_x, new_y, neighbors)

        return neighbors

    @staticmethod
    def get_area_perimeter(area: Set[Tuple[int, int]]) -> int:
        perimeter = 0
        for x, y in area:
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (x + dx, y + dy) not in area:
                    perimeter += 1
        return perimeter

    @staticmethod
    def get_area_corner_count(area: Set[Tuple[int, int]]) -> int:
        corners = 0
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for x, y in area:
            for i in range(len(deltas)):
                (dx1, dy1), (dx2, dy2) = deltas[i], deltas[(i + 1) % 4]
                point1 = (x + dx1, y + dy1)
                point2 = (x + dx2, y + dy2)
                point3 = (point2[0] + dx1, point2[1] + dy1)
                if point1 not in area and point2 not in area:
                    corners += 1
                elif point1 in area and point2 in area and point3 not in area:
                    corners += 1

        return corners


    def part1(self) -> int:
        areas = [len(region) for region in self.regions]
        perimeters = [self.get_area_perimeter(region) for region in self.regions]

        return sum([area * perimeter for area, perimeter in zip(areas, perimeters)])

    def part2(self) -> int:
        areas = [len(region) for region in self.regions]
        corner_counts = [self.get_area_corner_count(region) for region in self.regions]

        return sum([area * corner_count for area, corner_count in zip(areas, corner_counts)])


if __name__ == '__main__':
    Solution().run()
