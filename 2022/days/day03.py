from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day03", 2022)

        self.rucksacks: list[tuple[str, str]] = []
        for line in self.data:
            mid = len(line) // 2
            self.rucksacks.append((line[:mid], line[mid:]))

    def part1(self) -> int:
        sum_priority = 0

        for rucksack in self.rucksacks:
            compartment1, compartment2 = rucksack
            common_items = set(compartment1) & set(compartment2)

            for item in common_items:
                if item.islower():
                    sum_priority += ord(item) - ord('a') + 1
                else:
                    sum_priority += ord(item) - ord('A') + 27

        return sum_priority

    def part2(self) -> int:
        sum_priority = 0

        for i in range(0, len(self.rucksacks), 3):
            rucksack1 = ''.join(self.rucksacks[i])
            rucksack2 = ''.join(self.rucksacks[i + 1])
            rucksack3 = ''.join(self.rucksacks[i + 2])

            common_items = set(rucksack1) & set(rucksack2) & set(rucksack3)

            for item in common_items:
                if item.islower():
                    sum_priority += ord(item) - ord('a') + 1
                else:
                    sum_priority += ord(item) - ord('A') + 27

        return sum_priority


if __name__ == '__main__':
    Solution().run()
