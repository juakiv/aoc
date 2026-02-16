from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day03", 2018)

        self.claims: dict[int, tuple[tuple[int, int], tuple[int, int]]] = {}
        self.fabric_usage: dict[tuple[int, int], int] = defaultdict(int)
        for line in self.data:
            claim_id, data = line.split(" @ ")
            claim_id = int(claim_id[1:])
            position, size = data.split(": ")

            pos_x, pos_y = position.split(",")
            size_x, size_y = size.split("x")

            for x in range(int(pos_x), int(pos_x) + int(size_x)):
                for y in range(int(pos_y), int(pos_y) + int(size_y)):
                    self.fabric_usage[(x, y)] += 1

            self.claims[claim_id] = ((int(pos_x), int(pos_y)), (int(size_x), int(size_y)))

    def part1(self) -> int:
        return sum(1 for usage in self.fabric_usage.values() if usage > 1)

    def part2(self) -> int:
        non_overlapping_id = -1

        for claim_id, ((left, top), (width, height)) in self.claims.items():
            overlap = False

            for x in range(left, left + width):
                for y in range(top, top + height):
                    if self.fabric_usage[(x, y)] != 1:
                        overlap = True
                        break

                if overlap:
                    break

            if not overlap:
                non_overlapping_id = claim_id
                break

        return non_overlapping_id


if __name__ == '__main__':
    Solution().run()
