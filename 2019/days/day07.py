from itertools import permutations

from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    def part1(self) -> int:
        phase_settings = permutations([0, 1, 2, 3, 4])
        max_output = float("-inf")

        for settings in phase_settings:
            input_signal = 0

            for phase in settings:
                input_signal = IntcodeComputer(self.nums.copy(), [phase, input_signal]).run_full()[0]

            max_output = max(max_output, input_signal)

        return max_output

    def part2(self) -> int:
        best = 0
        for phases in permutations([5, 6, 7, 8, 9]):
            amps = [IntcodeComputer(self.nums.copy(), [phase]) for phase in phases]
            signal = 0

            while not amps[4].halted:
                for amp in amps:
                    amp.input_values.append(signal)
                    outputs = amp.run()

                    if outputs:
                        signal = outputs[-1]

            best = max(best, signal)

        return best


if __name__ == '__main__':
    Solution().run()
