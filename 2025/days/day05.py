from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05", 2025)

        self.fresh_ranges: list[range] = []
        self.ingredients: list[int] = []

        for line in self.data:
            if "-" in line:
                start, end = map(int, line.split("-"))
                self.fresh_ranges.append(range(start, end + 1))
            elif line != "":
                self.ingredients.append(int(line))

    def part1(self) -> int:
        fresh_ingredients_count = 0

        for ingredient in self.ingredients:
            if any(ingredient in fresh_range for fresh_range in self.fresh_ranges):
                fresh_ingredients_count += 1

        return fresh_ingredients_count

    def part2(self) -> int:
        ranges = self.fresh_ranges.copy()

        merging = True
        while merging:
            merging = False
            new_ranges = set()

            for first_range in ranges:
                for second_range in ranges:
                    if (first_range.start, first_range.stop) == (second_range.start, second_range.stop):
                        continue

                    if first_range.start <= second_range.stop and first_range.stop >= second_range.start:
                        new_start = min(first_range.start, second_range.start)
                        new_end = max(first_range.stop, second_range.stop)
                        first_range = range(new_start, new_end)
                        merging = True

                new_ranges.add(first_range)

            ranges = new_ranges

        return sum(r.stop - r.start for r in ranges)


if __name__ == '__main__':
    Solution().run()
