import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05", 2022, "\n\n")

        self.stacks: list[list[str]] = []
        self.instructions: list[list[int]] = []

        for stacks in reversed(self.data[0].split("\n")[:-1]):
            for i in range(0, len(stacks), 4):
                if len(self.stacks) <= i // 4:
                    self.stacks.append([])

                if stacks[i:i + 3].strip():
                    self.stacks[i // 4].append(stacks[i + 1])

        for instruction in self.data[1].split("\n"):
            nums = list(map(int, re.findall(r'\d+', instruction)))
            self.instructions.append(nums)


    def part1(self) -> str:
        stacks = [stack.copy() for stack in self.stacks]

        for instruction in self.instructions:
            count, source, destination = instruction

            for _ in range(count):
                crate = stacks[source - 1].pop()
                stacks[destination - 1].append(crate)

        return ''.join(stack[-1] for stack in stacks)

    def part2(self) -> str:
        stacks = [stack.copy() for stack in self.stacks]

        for instruction in self.instructions:
            count, source, destination = instruction

            crates = stacks[source - 1][-count:]
            stacks[source - 1] = stacks[source - 1][:-count]
            stacks[destination - 1].extend(crates)

        return ''.join(stack[-1] for stack in stacks)


if __name__ == '__main__':
    Solution().run()
