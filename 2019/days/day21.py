from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day21", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    @staticmethod
    def run_springscript(program: list[int], instructions: list[str]) -> int:
        instructions_ascii = [ord(c) for instruction in instructions for c in instruction + "\n"]

        computer = IntcodeComputer(program, instructions_ascii)
        output = computer.run_full()

        if output[-1] > 255:
            return output[-1]
        else:
            print("".join(chr(x) for x in output if x < 256))
            return -1

    def part1(self) -> int:
        instructions: list[str] = ["NOT A J", "NOT B T", "OR T J", "NOT C T", "OR T J", "AND D J", "WALK"]
        return self.run_springscript(self.nums, instructions)

    def part2(self) -> int:
        instructions: list[str] = ["NOT A J", "NOT B T", "OR T J", "NOT C T", "OR T J", "AND D J", "NOT E T", "NOT T T", "OR H T", "AND T J", "RUN"]
        return self.run_springscript(self.nums, instructions)


if __name__ == '__main__':
    Solution().run()
