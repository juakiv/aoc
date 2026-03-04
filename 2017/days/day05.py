from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05", 2017)

        self.offsets: list[int] = [int(x) for x in self.data]

    def part1(self) -> int:
        offsets = self.offsets.copy()
        total_jumps = 0
        current_index = 0

        while 0 <= current_index < len(offsets):
            jump = offsets[current_index]
            offsets[current_index] += 1
            current_index += jump
            total_jumps += 1

        return total_jumps

    def part2(self) -> int:
        offsets = self.offsets.copy()
        total_jumps = 0
        current_index = 0

        while 0 <= current_index < len(offsets):
            jump = offsets[current_index]
            if jump >= 3:
                offsets[current_index] -= 1
            else:
                offsets[current_index] += 1

            current_index += jump
            total_jumps += 1

        return total_jumps


if __name__ == '__main__':
    Solution().run()
