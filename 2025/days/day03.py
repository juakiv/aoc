from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day03", 2025)

    def max_joltage(self, bank: str, num_batteries: int) -> str:
        if num_batteries == 1:
            return max(bank)

        # the first max digit needs to be picked so that enough numbers are left for remaining batteries
        highest_first_digit = max(bank[:-(num_batteries - 1)])
        return highest_first_digit + self.max_joltage(bank[bank.index(highest_first_digit) + 1:], num_batteries - 1)

    def part1(self) -> int:
        return sum(int(self.max_joltage(bank, 2)) for bank in self.data)

    def part2(self) -> int:
        return sum(int(self.max_joltage(bank, 12)) for bank in self.data)


if __name__ == '__main__':
    Solution().run()
