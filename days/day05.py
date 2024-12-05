from typing import Tuple

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05")

        self.rules = []
        self.updates = []

        for line in self.data:
            if "," in line:
                self.updates.append(line.split(","))
            if "|" in line:
                self.rules.append(line.split("|"))

    def check_validity(self, update: list[int]) -> bool:
        for rule_left, rule_right in self.rules:
            if rule_left in update and rule_right in update and update.index(rule_left) > update.index(rule_right):
                return False

        return True

    def reorder(self, update: list[int]) -> list[int]:
        if len(update) <= 1:
            return update

        left_sort = []
        right_sort = []

        left_update = update[0]
        for right_update in update[1:]:
            if [right_update, left_update] in self.rules:
                left_sort.append(right_update)
            else:
                right_sort.append(right_update)

        return self.reorder(left_sort) + [left_update] + self.reorder(right_sort)

    def part1(self) -> int:
        sum_of_middle_numbers = 0

        for update in self.updates:
            if self.check_validity(update):
                sum_of_middle_numbers += int(update[len(update) // 2])

        return sum_of_middle_numbers

    def part2(self) -> int:
        sum_of_middle_numbers = 0

        for update in self.updates:
            if not self.check_validity(update):
                sum_of_middle_numbers += int(self.reorder(update)[len(update) // 2])

        return sum_of_middle_numbers


if __name__ == '__main__':
    Solution().run()
