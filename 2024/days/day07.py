from typing import Callable

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07")

        self.results: dict[int, list[int]] = {}

        for line in self.data:
            result, expression = line.split(": ")
            self.results[int(result)] = list(map(int, expression.split(" ")))

        self.operations = {
            "+": lambda x, y: x + y,
            "*": lambda x, y: x * y,
            "||": lambda x, y: int(str(x) + str(y))
        }

    def sums(self, target: int, current: int, numbers: list[int], operators: list[str]) -> bool:
        if len(numbers) == 0:
            return target == current

        return any(self.sums(target, self.operations[operator](current, numbers[0]), numbers[1:], operators) for operator in operators)

    def part1(self) -> int:
        total_sum = 0

        for target, numbers in self.results.items():
            total_sum += target if self.sums(target, numbers[0], numbers[1:], ["+", "*"]) else 0

        return total_sum

    def part2(self) -> int:
        total_sum = 0

        for target, numbers in self.results.items():
            total_sum += target if self.sums(target, numbers[0], numbers[1:], ["+", "*", "||"]) else 0

        return total_sum


if __name__ == '__main__':
    Solution().run()
