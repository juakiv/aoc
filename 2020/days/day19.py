import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day19", 2020, "\n\n")

        self.rules = {}
        self.messages = []

        for line in self.data[0].split("\n"):
            key, rule = line.split(": ")
            self.rules[int(key)] = rule.replace("\"", "")

        self.messages = self.data[1].split("\n")

    def regex(self, rule_num: int, part2: bool = False) -> str:
        rule = self.rules[rule_num]
        if part2:
            if rule_num == 8:
                return f"({self.regex(42, part2)})+"

            if rule_num == 11:
                rule_42 = self.regex(42, part2)
                rule_31 = self.regex(31, part2)

                # regex doesn't have recursion, so unrolling the rule a few times
                return "(" + "|".join(f"({rule_42}){{{i}}}({rule_31}){{{i}}}" for i in range(1, 10)) + ")"

        if rule in ("a", "b"):
            return rule

        parts = []
        for option in rule.split(" | "):
            parts.append("".join(self.regex(int(r), part2) for r in option.split()))

        return "(" + "|".join(parts) + ")"

    def part1(self) -> int:
        valid_count = 0
        pattern = re.compile("^" + self.regex(0, part2=False) + "$")

        for message in self.messages:
            if pattern.match(message):
                valid_count += 1

        return valid_count

    def part2(self) -> int:
        valid_count = 0
        pattern = re.compile("^" + self.regex(0, part2=True) + "$")

        for message in self.messages:
            if pattern.match(message):
                valid_count += 1

        return valid_count


if __name__ == '__main__':
    Solution().run()
