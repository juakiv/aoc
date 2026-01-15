import copy
import math

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day11", 2022, "\n\n")

        self.monkeys = []
        for block in self.data:
            lines = block.split("\n")
            starting_items = list(map(int, lines[1].split(": ")[1].split(", ")))
            operation = lines[2].split(" = ")[1].split()
            test_divisor = int(lines[3].split("by ")[1])
            true_target = int(lines[4].split("monkey ")[1])
            false_target = int(lines[5].split("monkey ")[1])

            self.monkeys.append({
                "items": starting_items,
                "operation": operation,
                "test_divisor": test_divisor,
                "true_target": true_target,
                "false_target": false_target,
                "times_inspected": 0
            })

    def run_rounds(self, rounds: int, part2: bool = False):
        monkeys = copy.deepcopy(self.monkeys)
        modulus = math.lcm(*(monkey["test_divisor"] for monkey in monkeys))

        for _ in range(rounds):
            for monkey in monkeys:
                items = []

                for item in monkey["items"]:
                    monkey["times_inspected"] += 1
                    old_item = item

                    if monkey["operation"][1] == '+':
                        if monkey["operation"][2] == 'old':
                            item = old_item + old_item
                        else:
                            item = old_item + int(monkey["operation"][2])

                    elif monkey["operation"][1] == '*':
                        if monkey["operation"][2] == 'old':
                            item = old_item * old_item
                        else:
                            item = old_item * int(monkey["operation"][2])

                    if part2:
                        item %= modulus
                    else:
                        item //= 3

                    if item % monkey["test_divisor"] == 0:
                        target_monkey = monkey["true_target"]
                    else:
                        target_monkey = monkey["false_target"]

                    monkeys[target_monkey]["items"].append(item)

                monkey["items"] = items

        return monkeys

    def part1(self) -> int:
        sorted_monkeys = sorted(self.run_rounds(20), key=lambda m: m["times_inspected"], reverse=True)
        return sorted_monkeys[0]["times_inspected"] * sorted_monkeys[1]["times_inspected"]

    def part2(self) -> int:
        sorted_monkeys = sorted(self.run_rounds(10000, part2=True), key=lambda m: m["times_inspected"], reverse=True)
        return sorted_monkeys[0]["times_inspected"] * sorted_monkeys[1]["times_inspected"]


if __name__ == '__main__':
    Solution().run()
