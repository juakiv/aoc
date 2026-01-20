from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02", 2021)

        self.instructions: list[tuple[str, int]] = [(line.split()[0], int(line.split()[1])) for line in self.data]

    def part1(self) -> int:
        horizontal_position = 0
        depth = 0

        for instruction in self.instructions:
            command, value = instruction
            if command == "forward":
                horizontal_position += value
            elif command == "down":
                depth += value
            elif command == "up":
                depth -= value

        return horizontal_position * depth

    def part2(self) -> int:
        horizontal_position = 0
        depth = 0
        aim = 0

        for instruction in self.instructions:
            command, value = instruction
            if command == "forward":
                horizontal_position += value
                depth += aim * value
            elif command == "down":
                aim += value
            elif command == "up":
                aim -= value

        return horizontal_position * depth


if __name__ == '__main__':
    Solution().run()
