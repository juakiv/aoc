from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01", 2019)

        self.masses: list[int] = [int(line) for line in self.data]

    def part1(self) -> int:
        total_fuel = 0

        for mass in self.masses:
            total_fuel += mass // 3 - 2

        return total_fuel

    def part2(self) -> int:
        total_fuel = 0

        for mass in self.masses:
            additional_fuel = mass // 3 - 2

            while additional_fuel > 0:
                total_fuel += additional_fuel
                additional_fuel = additional_fuel // 3 - 2

        return total_fuel


if __name__ == '__main__':
    Solution().run()
