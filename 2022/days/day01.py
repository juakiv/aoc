from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01", 2022, "\n\n")

        self.calories: list[list[int]] = []
        for calorie_block in self.data:
            self.calories.append([int(calorie) for calorie in calorie_block.split("\n")])

    def part1(self) -> int:
        return max(sum(calorie_list) for calorie_list in self.calories)

    def part2(self) -> int:
        return sum(
            sorted((sum(calorie_list) for calorie_list in self.calories), reverse=True)[:3]
        )


if __name__ == '__main__':
    Solution().run()
