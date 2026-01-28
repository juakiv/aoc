from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06", 2020, "\n\n")

        self.answers = [set(group.replace("\n", "")) for group in self.data]

    def part1(self) -> int:
        return sum(len(answer) for answer in self.answers)

    def part2(self) -> int:
        total = 0
        for group in self.data:
            people = group.split("\n")
            common_answers = set(people[0])

            for person in people[1:]:
                common_answers &= set(person)

            total += len(common_answers)

        return total


if __name__ == '__main__':
    Solution().run()
