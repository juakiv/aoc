from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day25", 2022)

    @staticmethod
    def snafu_to_decimal(snafu: str) -> int:
        mapping = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
        decimal_value = 0

        for i, char in enumerate(reversed(snafu)):
            decimal_value += mapping[char] * (5 ** i)

        return decimal_value

    @staticmethod
    def decimal_to_snafu(decimal_value: int) -> str:
        snafu_digits = []
        n = decimal_value

        while n != 0:
            n, remainder = divmod(n, 5)
            if remainder > 2:
                remainder -= 5
                n += 1
            snafu_digits.append(remainder)

        mapping = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
        snafu_string = "".join(mapping[digit] for digit in reversed(snafu_digits))

        return snafu_string

    def part1(self) -> str:
        total = sum(self.snafu_to_decimal(line) for line in self.data)
        return self.decimal_to_snafu(total)

    def part2(self) -> str:
        return ":)"


if __name__ == '__main__':
    Solution().run()
