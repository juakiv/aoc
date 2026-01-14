from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day04", 2022)

        self.pairs: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
        for line in self.data:
            first, second = line.split(",")
            first_range = tuple(map(int, first.split("-")))
            second_range = tuple(map(int, second.split("-")))
            self.pairs.append((first_range, second_range))

    def part1(self) -> int:
        fully_overlapping_count = 0

        for first_range, second_range in self.pairs:
            first_start, first_end = first_range
            second_start, second_end = second_range

            if (first_start <= second_start and first_end >= second_end) or \
               (second_start <= first_start and second_end >= first_end):
                fully_overlapping_count += 1

        return fully_overlapping_count

    def part2(self) -> int:
        overlapping_count = 0

        for first_range, second_range in self.pairs:
            first_start, first_end = first_range
            second_start, second_end = second_range

            if not (first_end < second_start or second_end < first_start):
                overlapping_count += 1

        return overlapping_count


if __name__ == '__main__':
    Solution().run()
