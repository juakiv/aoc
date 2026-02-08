from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day13", 2019)
        self.nums = [int(x) for x in self.data[0].split(",")]

    def part1(self) -> int:
        computer = IntcodeComputer(self.nums).run_full()
        total_blocks = 0

        for i in range(0, len(computer), 3):
            _, _, tile_id = computer[i:i+3]

            if tile_id == 2:
                total_blocks += 1

        return total_blocks

    def part2(self) -> int:
        program = self.nums.copy()
        program[0] = 2

        computer = IntcodeComputer(program)

        score = 0
        ball_x = 0
        paddle_x = 0

        while not computer.halted:
            computer.run()
            while len(computer.outputs) >= 3:
                x = computer.outputs.pop(0)
                y = computer.outputs.pop(0)
                tile = computer.outputs.pop(0)

                if x == -1 and y == 0:
                    score = tile
                else:
                    if tile == 3:
                        paddle_x = x
                    elif tile == 4:
                        ball_x = x

            if computer.waiting:
                if ball_x < paddle_x:
                    computer.input_values.append(-1)
                elif ball_x > paddle_x:
                    computer.input_values.append(1)
                else:
                    computer.input_values.append(0)

        return score


if __name__ == '__main__':
    Solution().run()
