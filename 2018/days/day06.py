from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06", 2018)
        self.coords: list[tuple[int, int]] = [(int(x), int(y)) for x, y in (line.split(", ") for line in self.data)]

        self.bounding_box: tuple[int, int, int, int] = (
            min(x for x, _ in self.coords),
            max(x for x, _ in self.coords),
            min(y for _, y in self.coords),
            max(y for _, y in self.coords)
        )

    def part1(self) -> int:
        area_counts = defaultdict(int)
        infinite_ids = set()

        for x in range(self.bounding_box[0], self.bounding_box[1] + 1):
            for y in range(self.bounding_box[2], self.bounding_box[3] + 1):
                distances = []
                for i, (coord_x, coord_y) in enumerate(self.coords):
                    distances.append((abs(x - coord_x) + abs(y - coord_y), i))

                distances.sort()

                if distances[0][0] < distances[1][0]:
                    closest_id = distances[0][1]
                    area_counts[closest_id] += 1

                    if x in (self.bounding_box[0], self.bounding_box[1]) or y in (self.bounding_box[2], self.bounding_box[3]):
                        infinite_ids.add(closest_id)

        finite_areas = [count for i, count in area_counts.items() if i not in infinite_ids]
        return max(finite_areas)

    def part2(self) -> int:
        region_size = 0

        for x in range(self.bounding_box[0], self.bounding_box[1] + 1):
            for y in range(self.bounding_box[2], self.bounding_box[3] + 1):
                total_distance = sum(abs(x - coord_x) + abs(y - coord_y) for coord_x, coord_y in self.coords)

                if total_distance < 10_000:
                    region_size += 1

        return region_size


if __name__ == '__main__':
    Solution().run()
