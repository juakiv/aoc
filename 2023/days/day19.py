import math
import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day19", 2023, "\n\n")

        self.workflows: dict[str, list[str]] = {}
        self.ratings: list[dict[str, int]] = []
        for workflow in self.data[0].split("\n"):
            name, rules = re.findall(r"(\w+){(.*?)}", workflow)[0]
            self.workflows[name] = [rule.strip() for rule in rules.split(",")]

        for rating in self.data[1].split("\n"):
            rating_dict = {}
            for item in rating[1:-1].split(","):
                key, value = item.split("=")
                rating_dict[key.strip()] = int(value.strip())
            self.ratings.append(rating_dict)

    def run_workflow(self, workflow_name: str, rating: dict[str, int]):
        if workflow_name == "R":
            return 0

        if workflow_name == "A":
            return sum(rating.values())

        rules = self.workflows[workflow_name]

        for rule in rules:
            if ":" in rule:
                condition, workflow = rule.split(":")
                condition_operand, condition_value = re.split(r"[<>]", condition)
                condition_value = int(condition_value)

                if "<" in condition:
                    if rating[condition_operand] < condition_value:
                        return self.run_workflow(workflow, rating)
                    else:
                        continue
                elif ">" in condition:
                    if rating[condition_operand] > condition_value:
                        return self.run_workflow(workflow, rating)
                    else:
                        continue
            else:
                return self.run_workflow(rule, rating)

        return 0


    def part1(self) -> int:
        return sum(self.run_workflow("in", rating) for rating in self.ratings)

    def part2(self) -> int:
        total_combinations = 0

        start = ("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})
        queue = [start]

        while queue:
            current_workflow, ranges = queue.pop()
            if current_workflow in ["R", "A"]:
                if current_workflow == "A":
                    total_combinations += math.prod(high - low + 1 for low, high in ranges.values())
                continue

            rules = self.workflows[current_workflow]
            for rule in rules[:-1]:
                rule_char = rule[0]
                low, high = ranges[rule_char]
                operator = rule[1]
                value, next_workflow = rule[2:].split(":")
                value = int(value)

                if (operator == ">" and value >= high) or (operator == "<" and value <= low):
                    continue

                if (operator == ">" and value < low) or (operator == "<" and value > high):
                    queue.append((next_workflow, ranges))
                    break

                if operator == ">":
                    new_low = (value + 1, high)
                    new_high = (low, value)
                else:
                    new_low = (low, value - 1)
                    new_high = (value, high)

                ranges[rule_char] = new_high
                new_ranges = ranges.copy()
                new_ranges[rule_char] = new_low
                queue.append((next_workflow, new_ranges))

            else:
                current_workflow_fallback = rules[-1]
                queue.append((current_workflow_fallback, ranges))

        return total_combinations


if __name__ == '__main__':
    Solution().run()
