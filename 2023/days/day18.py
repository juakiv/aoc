import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day18", 2023)

        self.dig_plan = []
        for line in self.data:
            direction, distance, hex_value = re.findall(r"(\w) (\d+) \(#(\w+)\)", line)[0]
            self.dig_plan.append((direction, int(distance), hex_value))

    @staticmethod
    def get_loop(dig_plan: list[tuple[str, int, str]]) -> tuple[list[tuple[int, int]], int]:
        direction_offsets = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }
        points = [(0, 0)]
        outline_length = 0

        for direction, distance, _ in dig_plan:
            last_x, last_y = points[-1]
            offset_x, offset_y = direction_offsets[direction]

            new_point = (offset_x * distance + last_x, offset_y * distance + last_y)
            points.append(new_point)
            outline_length += distance

        return points, outline_length

    # from day 10, 2023
    @staticmethod
    def shoelace(points: list[tuple[int, int]]) -> int:
        n = len(points)
        area = 0

        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            area += x1 * y2 - x2 * y1

        return area // 2

    def part1(self) -> int:
        loop, outline_length = self.get_loop(self.dig_plan)
        area = self.shoelace(loop)

        # picks theorem for calculating number of interior points + loop points (day 10, 2023)
        return int(abs(area) - 0.5  * outline_length + 1) + outline_length

    def part2(self) -> int:
        new_dig_plan = []
        for _, _, hex_value in self.dig_plan:
            direction_int = int(hex_value[-1])
            direction = "R" if direction_int == 0 else "D" if direction_int == 1 else "L" if direction_int == 2 else "U"
            new_dig_plan.append((direction, int(hex_value[:-1], 16), ""))

        loop, outline_length = self.get_loop(new_dig_plan)
        area = self.shoelace(loop)

        return int(abs(area) - 0.5  * outline_length + 1) + outline_length


if __name__ == '__main__':
    Solution().run()
