import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05", 2023, "\n\n")
        self.seeds = map(int, re.findall(r"\d+", self.data[0]))
        self.maps = [
            [
                [int(num) for num in map_line.split(" ")] for map_line in map_lines.split("\n")[1::]
            ]
            for map_lines in self.data[1:]
        ]

    def part1(self) -> int:
        lowest = float("inf")
        for seed in self.seeds:
            for map_ in self.maps:

                for dst_range_start, src_range_start, range_length in map_:
                    if src_range_start <= seed < src_range_start + range_length:
                        seed = dst_range_start + (seed - src_range_start)
                        break

            lowest = min(lowest, seed)

        return lowest

    def part2(self) -> int:
        lowest = float("inf")
        seed_ranges = []

        for seed in re.findall(r"(\d+) (\d+)", self.data[0]):
            seed_ranges.append((int(seed[0]), int(seed[0]) + int(seed[1]), 1))

        # somewhat similar merging as day 5 2025 :)
        while seed_ranges:
            start, length, map_level = seed_ranges.pop(0)

            if map_level == 8:
                lowest = min(lowest, start)
                continue

            for map_ in re.findall(r"(\d+) (\d+) (\d+)", self.data[map_level]):
                dst_range_start, src_range_start, range_length = map(int, map_)
                src_range_end = src_range_start + range_length

                # when no overlap
                if length <= src_range_start or src_range_end <= start:
                    continue

                # partial overlap, left side
                if start < src_range_start:
                    seed_ranges.append((start, src_range_start, map_level))
                    start = src_range_start

                # partial overlap, right side
                if src_range_end < length:
                    seed_ranges.append((src_range_end, length, map_level))
                    length = src_range_end

                # full overlap
                seed_ranges.append((start + (dst_range_start - src_range_start), length + (dst_range_start - src_range_start), map_level + 1))
                break
            else:
                # no mapping found
                seed_ranges.append((start, length, map_level + 1))

        return lowest


if __name__ == '__main__':
    Solution().run()
