from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07", 2021)

        self.crabs = [int(x) for x in self.data[0].split(",")]

    def part1(self) -> int:
        total_fuel = 0

        median = sorted(self.crabs)[len(self.crabs) // 2]
        for crab in self.crabs:
            total_fuel += abs(crab - median)

        return total_fuel

    def part2(self) -> int:
        total_fuel = float("inf")

        for pos in range(min(self.crabs), max(self.crabs) + 1):
            fuel = 0
            for crab in self.crabs:
                distance = abs(crab - pos)
                fuel += distance * (distance + 1) // 2
            total_fuel = min(total_fuel, fuel)

        return total_fuel


if __name__ == '__main__':
    Solution().run()
