from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day10", 2020)

        self.adapters: list[int] = [int(line) for line in self.data]

    def part1(self) -> int:
        differences = { 1: 0, 2: 0, 3: 1 }
        sorted_adapters = sorted(self.adapters)

        current_joltage = 0
        for adapter in sorted_adapters:
            diff = adapter - current_joltage
            if diff in differences:
                differences[diff] += 1
            current_joltage = adapter

        return differences[1] * differences[3]

    def part2(self) -> int:
        total_arrangements = { 0: 1 }
        sorted_adapters = sorted(self.adapters)

        for adapter in sorted_adapters:
            total_arrangements[adapter] = (
                total_arrangements.get(adapter - 1, 0) +
                total_arrangements.get(adapter - 2, 0) +
                total_arrangements.get(adapter - 3, 0)
            )

        return total_arrangements[sorted_adapters[-1]]


if __name__ == '__main__':
    Solution().run()
