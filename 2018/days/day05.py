from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05", 2018)[0]

    @staticmethod
    def react_polymer(polymer: str) -> str:
        stack = []
        for unit in polymer:
            if stack and unit.swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(unit)

        return "".join(stack)

    def part1(self) -> int:
        return len(self.react_polymer(self.data))

    def part2(self) -> int:
        best_length = len(self.data)

        for unit_type in set(self.data.lower()):
            modified_polymer = self.data.replace(unit_type, "").replace(unit_type.upper(), "")
            reacted_polymer = self.react_polymer(modified_polymer)
            best_length = min(best_length, len(reacted_polymer))

        return best_length


if __name__ == '__main__':
    Solution().run()
