from solution.base import SolutionBase
from collections import Counter


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01")

        self.list1: list[int] = []
        self.list2: list[int] = []

        for pair in self.data:
            a, b = pair.split()
            self.list1.append(int(a))
            self.list2.append(int(b))

        self.list1.sort()
        self.list2.sort()

    def part1(self) -> int:
        difference_sum: int = 0

        for a, b in zip(self.list1, self.list2):
            difference_sum += abs(a - b)

        return difference_sum

    def part2(self) -> int:
        similarity_score: int = 0
        list2_counts: dict[int, int] = Counter(self.list2)

        for a in self.list1:
            if a in list2_counts:
                similarity_score += a * list2_counts[a]

        return similarity_score

if __name__ == '__main__':
    Solution().run()