from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day25", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    def part1(self) -> int:
        # terminal adventure ! :)
        computer = IntcodeComputer(self.nums)

        while not computer.halted:
            computer.run_full()
            output_str = "".join(chr(c) for c in computer.outputs)
            print(output_str, end="")
            computer.outputs = []

            if computer.halted:
                break

            try:
                command = input() + "\n"
            except EOFError:
                break

            computer.input_values.extend([ord(c) for c in command])
            computer.waiting = False

        return 0

    def part2(self) -> str:
        return ":)"


if __name__ == '__main__':
    Solution().run()
