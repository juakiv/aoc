from itertools import combinations, pairwise

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09", 2025)

        self.red_tiles: list[tuple[int, ...]] = [tuple(map(int, tile.split(","))) for tile in self.data]

    def part1(self) -> int:
        largest_area = 0

        for (x1, y1), (x2, y2) in combinations(self.red_tiles, 2):
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > largest_area:
                largest_area = area

        return largest_area

    def part2(self) -> int:
        largest_area = 0

        red_tile_bounds = [(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)) for (x1, y1), (x2, y2) in combinations(self.red_tiles, 2)]
        green_tile_bounds = [(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)) for (x1, y1), (x2, y2) in pairwise(self.red_tiles)]

        for x_min, y_min, x_max, y_max in red_tile_bounds:
            area = (abs(x_min - x_max) + 1) * (abs(y_min - y_max) + 1)

            if area > largest_area:
                for green_x1, green_y1, green_x2, green_y2 in green_tile_bounds:
                    if x_min < green_x2 and y_min < green_y2 and x_max > green_x1 and y_max > green_y1:
                        break
                else:
                    largest_area = area

        return largest_area


if __name__ == '__main__':
    Solution().run()
