import math

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06", 2025)

    def part1(self) -> int:
        grand_total = 0

        for problem in list(zip(*[line.split() for line in self.data])):
            operation = problem[-1]
            numbers_in_problem = map(int, problem[:-1])

            grand_total += sum(numbers_in_problem) if operation == "+" else math.prod(numbers_in_problem)

        return grand_total

    def part2(self) -> int:
        grand_total = 0

        max_width = max(len(line) for line in self.data)
        padded_data = [line.ljust(max_width) for line in self.data]
        problem_data = ["".join(item).strip() for item in zip(*padded_data)]

        current_problem_operands = []
        current_problem_operation = None
        for i, problem in enumerate(reversed(problem_data)):
            if "+" in problem or "*" in problem:
                current_problem_operation = problem[-1]
                current_problem_operands.append(int(problem[:-1].strip()))
            elif problem != "":
                current_problem_operands.append(int(problem.strip()))

            if problem == "" or i == len(problem_data) - 1:
                grand_total += sum(current_problem_operands) if current_problem_operation == "+" else math.prod(current_problem_operands)

                current_problem_operands = []
                current_problem_operation = None

        return grand_total


if __name__ == '__main__':
    Solution().run()
