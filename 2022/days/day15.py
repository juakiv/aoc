import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day15", 2022)

        self.sensor_beacon_pairs = []
        for line in self.data:
            nums = re.findall(r'\d+', line)
            sensor_x, sensor_y, beacon_x, beacon_y = map(int, nums)
            self.sensor_beacon_pairs.append(((sensor_x, sensor_y), (beacon_x, beacon_y)))

    def free_positions(self, y: int) -> int:
        occupied_positions = set()

        for (sensor_x, sensor_y), (beacon_x, beacon_y) in self.sensor_beacon_pairs:
            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            vertical_distance = abs(sensor_y - y)

            if vertical_distance <= distance:
                horizontal_range = distance - vertical_distance

                for x in range(sensor_x - horizontal_range, sensor_x + horizontal_range + 1):
                    occupied_positions.add(x)

        for _, (beacon_x, beacon_y) in self.sensor_beacon_pairs:
            if beacon_y == y and beacon_x in occupied_positions:
                occupied_positions.remove(beacon_x)

        return len(occupied_positions)

    def part1(self) -> int:
        return self.free_positions(2_000_000 if not self.is_test else 10)

    def part2(self) -> int:
        limit = 4_000_000 if not self.is_test else 20

        for (sensor_x, sensor_y), (beacon_x, beacon_y) in self.sensor_beacon_pairs:
            distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            perimeter_distance = distance + 1

            for dx in range(perimeter_distance + 1):
                dy = perimeter_distance - dx

                possible_positions = [
                    (sensor_x + dx, sensor_y + dy),
                    (sensor_x + dx, sensor_y - dy),
                    (sensor_x - dx, sensor_y + dy),
                    (sensor_x - dx, sensor_y - dy),
                ]

                for x, y in possible_positions:
                    if 0 <= x <= limit and 0 <= y <= limit:
                        if all(abs(x - sx) + abs(y - sy) > abs(sx - bx) + abs(sy - by) for (sx, sy), (bx, by) in self.sensor_beacon_pairs):
                            return x * 4_000_000 + y

        return 0


if __name__ == '__main__':
    Solution().run()
