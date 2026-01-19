from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day21", 2022)

        self.monkeys = {}
        for line in self.data:
            name, job = line.split(": ")
            self.monkeys[name] = job.split(" ") if not job.isdigit() else int(job)

    def yell(self, monkey_name: str) -> int:
        job = self.monkeys[monkey_name]
        if isinstance(job, int):
            return int(job)
        else:
            left, op, right = job
            left_val = self.yell(left)
            right_val = self.yell(right)
            if op == "+":
                return left_val + right_val
            elif op == "-":
                return left_val - right_val
            elif op == "*":
                return left_val * right_val
            elif op == "/":
                return left_val // right_val

        return -1

    def part1(self) -> int:
        return self.yell("root")

    def part2(self) -> int:
        values = {}
        changed = True

        while changed:
            changed = False
            for name, value in self.monkeys.items():
                if name in values:
                    continue
                if name == "humn":
                    continue
                if isinstance(value, int):
                    values[name] = value
                    changed = True
                else:
                    a, operator, b = value
                    if a in values and b in values:
                        if operator == "+":
                            values[name] = values[a] + values[b]
                        elif operator == "-":
                            values[name] = values[a] - values[b]
                        elif operator == "*":
                            values[name] = values[a] * values[b]
                        elif operator == "/":
                            values[name] = values[a] // values[b]
                        changed = True

        left, _, right = self.monkeys["root"]
        if left in values:
            target = values[left]
            current = right
        else:
            target = values[right]
            current = left

        while current != "humn":
            a, operator, b = self.monkeys[current]

            if a in values:
                known = values[a]
                if operator == "+":
                    target = target - known
                elif operator == "-":
                    target = known - target
                elif operator == "*":
                    target = target // known
                elif operator == "/":
                    target = known // target
                current = b
            else:
                known = values[b]
                if operator == "+":
                    target = target - known
                elif operator == "-":
                    target = target + known
                elif operator == "*":
                    target = target // known
                elif operator == "/":
                    target = target * known
                current = a

        return target


if __name__ == '__main__':
    Solution().run()
