from collections import defaultdict

from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day11", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    @staticmethod
    def run_painter(nums: list[int], start_color: int) -> tuple[set[tuple[int, int]], dict[tuple[int, int], int]]:
        computer = IntcodeComputer(nums)

        x, y = 0, 0
        direction_index = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        panels = defaultdict(int)
        panels[(x, y)] = start_color
        painted = set()

        while not computer.halted:
            computer.input_values.append(panels[(x, y)])
            computer.run()
            if computer.halted:
                break

            paint_color = computer.outputs[-1]
            computer.run()

            turn = computer.outputs[-1]
            panels[(x, y)] = paint_color
            painted.add((x, y))

            if turn == 0:
                direction_index = (direction_index - 1) % 4
            else:
                direction_index = (direction_index + 1) % 4

            dx, dy = directions[direction_index]
            x += dx
            y += dy

        return painted, panels

    def part1(self) -> int:
        return len(self.run_painter(self.nums.copy(), 0)[0])

    def part2(self) -> str:
        _, panels = self.run_painter(self.nums.copy(), 1)

        min_x = min(x for x, _ in panels)
        max_x = max(x for x, _ in panels)
        min_y = min(y for _, y in panels)
        max_y = max(y for _, y in panels)

        for y in range(max_y, min_y - 1, -1):
            row = ""
            for x in range(min_x, max_x + 1):
                row += "#" if panels[(x, y)] == 1 else " "
            print(row)

        return "See print above :)"


if __name__ == '__main__':
    Solution().run()
