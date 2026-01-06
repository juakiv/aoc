from functools import cache

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day12", 2023)

        self.rows: list[tuple[str, tuple[int, ...]]] = []

        for line in self.data:
            conditions, rules = line.split()
            self.rows.append((conditions, tuple(map(int, rules.split(",")))))

    @cache
    def arrangements(self, conditions: str, rules: tuple[int, ...]) -> int:
        if not conditions:
            return len(rules) == 0

        if not rules:
            return 1 if "#" not in conditions else 0

        current, rest = conditions[0], conditions[1:]

        if current == ".":
            return self.arrangements(rest, rules)

        if current == "#":
            rule = rules[0]
            if len(conditions) >= rule and \
                all(char != "." for char in conditions[:rule]) \
                and(len(conditions) == rule or conditions[rule] != "#"):
                return self.arrangements(conditions[rule + 1:], rules[1:])

            return 0

        if current == "?":
            return self.arrangements(f"#{rest}", rules) + self.arrangements(f".{rest}", rules)

        return 0

    def part1(self) -> int:
        return sum(
            self.arrangements(conditions, rules)
            for conditions, rules in self.rows
        )

    def part2(self) -> int:
        total = 0
        for conditions, rules in self.rows:
            conditions = "?".join([conditions] * 5)
            rules *= 5

            total += self.arrangements(conditions, rules)

        return total


if __name__ == '__main__':
    Solution().run()
