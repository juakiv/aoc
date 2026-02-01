from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day18", 2020)

        self.expressions = [line.strip() for line in self.data]

    def evaluate_expression(self, expression: str, index: int, part2: bool = False) -> tuple[int, int]:
        values = []
        operations = []

        while index < len(expression):
            c = expression[index]

            if c == " ":
                index += 1
                continue

            if c.isdigit():
                values.append(int(c))
                index += 1

            elif c == "(":
                value, index = self.evaluate_expression(expression, index + 1, part2)
                values.append(value)

            elif c == ")":
                break

            else:
                if part2:
                    while operations and operations[-1] == "+":
                        b = values.pop()
                        a = values.pop()
                        operations.pop()
                        values.append(a + b)
                else:
                    while operations:
                        b = values.pop()
                        a = values.pop()
                        op = operations.pop()
                        values.append(a + b if op == "+" else a * b)

                operations.append(c)
                index += 1
                continue

            if part2 and operations and operations[-1] == "+":
                b = values.pop()
                a = values.pop()
                operations.pop()
                values.append(a + b)

        while operations:
            b = values.pop()
            a = values.pop()
            op = operations.pop()
            values.append(a + b if op == "+" else a * b)

        return values[0], index + 1

    def part1(self) -> int:
        total = 0

        for expression in self.expressions:
            result, _ = self.evaluate_expression(expression, 0)
            total += result

        return total

    def part2(self) -> int:
        total = 0

        for expression in self.expressions:
            result, _ = self.evaluate_expression(expression, 0, part2=True)
            total += result

        return total


if __name__ == '__main__':
    Solution().run()
