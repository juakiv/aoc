import re
from heapq import heappush, heappop

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day23", 2018)

        self.nanobots: list[tuple[int, int, int, int]] = []
        for line in self.data:
            nums = re.findall(r"-?\d+", line)
            self.nanobots.append((int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])))

    @staticmethod
    def manhattan_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

    def part1(self) -> int:
        biggest_range_bot = max(self.nanobots, key=lambda x: x[3])
        x, y, z, biggest_range = biggest_range_bot
        count = 0

        for bot in self.nanobots:
            if self.manhattan_distance((x, y, z), (bot[0], bot[1], bot[2])) <= biggest_range:
                count += 1

        return count

    def part2(self) -> int:
        min_x = min(bot[0] for bot in self.nanobots)
        max_x = max(bot[0] for bot in self.nanobots)
        min_y = min(bot[1] for bot in self.nanobots)
        max_y = max(bot[1] for bot in self.nanobots)
        min_z = min(bot[2] for bot in self.nanobots)
        max_z = max(bot[2] for bot in self.nanobots)

        # subdivisible of 2 side length
        side_length = 1
        max_range = max(max_x - min_x, max_y - min_y, max_z - min_z)
        while side_length < max_range:
            side_length *= 2

        queue = [(-len(self.nanobots), side_length, 0, min_x, min_y, min_z)]
        while queue:
            neg_count, size, distance_to_zero, x, y, z = heappop(queue)

            if size == 1:
                return distance_to_zero

            # subdivision of the box into 8 smaller boxes
            half_size = size // 2
            for dx in [0, half_size]:
                for dy in [0, half_size]:
                    for dz in [0, half_size]:
                        new_x, new_y, new_z = x + dx, y + dy, z + dz

                        potential_bots = 0
                        for bot_x, bot_y, bot_z, bot_range in self.nanobots:
                            dist_to_box = 0

                            if bot_x < new_x:
                                dist_to_box += new_x - bot_x
                            elif bot_x > new_x + half_size - 1:
                                dist_to_box += bot_x - (new_x + half_size - 1)

                            if bot_y < new_y:
                                dist_to_box += new_y - bot_y
                            elif bot_y > new_y + half_size - 1:
                                dist_to_box += bot_y - (new_y + half_size - 1)

                            if bot_z < new_z:
                                dist_to_box += new_z - bot_z
                            elif bot_z > new_z + half_size - 1:
                                dist_to_box += bot_z - (new_z + half_size - 1)

                            if dist_to_box <= bot_range:
                                potential_bots += 1

                        if potential_bots > 0:
                            new_dist_zero = abs(new_x) + abs(new_y) + abs(new_z)
                            heappush(queue, (-potential_bots, half_size, new_dist_zero, new_x, new_y, new_z))
        return -1


if __name__ == '__main__':
    Solution().run()
