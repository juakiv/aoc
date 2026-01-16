import json
from functools import cmp_to_key

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day13", 2022, "\n\n")

        self.pairs = []
        for block in self.data:
            first, second = block.split("\n")

            self.pairs.append((json.loads(first), json.loads(second)))

    def compare(self, left, right) -> int:
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            elif left > right:
                return 1
            else:
                return 0

        elif isinstance(left, list) and isinstance(right, list):
            for left_item, right_item in zip(left, right):
                result = self.compare(left_item, right_item)
                if result != 0:
                    return result

            if len(left) < len(right):
                return -1
            elif len(left) > len(right):
                return 1
            else:
                return 0

        elif isinstance(left, int):
            return self.compare([left], right)

        else:
            return self.compare(left, [right])

    def part1(self) -> int:
        total = 0
        for i, (left, right) in enumerate(self.pairs, start=1):
            if self.compare(left, right) == -1:
                total += i
        return total

    def part2(self) -> int:
        packets = [[[2]], [[6]]]
        for left, right in self.pairs:
            packets.append(left)
            packets.append(right)

        sorted_packets = sorted(packets, key=cmp_to_key(self.compare))
        return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


if __name__ == '__main__':
    Solution().run()
