from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day23", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    def part1(self) -> int:
        computers = [IntcodeComputer(self.nums, [i]) for i in range(50)]

        while True:
            for i in range(50):
                computer = computers[i]

                if not computer.input_values:
                    computer.input_values.append(-1)

                computer.run()

                if len(computer.outputs) == 3:
                    dest = computer.outputs.pop(0)
                    x = computer.outputs.pop(0)
                    y = computer.outputs.pop(0)

                    if dest == 255:
                        return y

                    if 0 <= dest < 50:
                        computers[dest].input_values.append(x)
                        computers[dest].input_values.append(y)

    def part2(self) -> int:
        computers = [IntcodeComputer(self.nums, [i]) for i in range(50)]

        nat_last_packet = None
        nat_last_y = None

        while True:
            idle_count = 0

            for i in range(50):
                computer = computers[i]

                if len(computer.input_values) == 0:
                    computer.input_values.append(-1)

                computer.run()
                if not computer.outputs and len(computer.input_values) == 0:
                    idle_count += 1

                if len(computer.outputs) == 3:
                    dest = computer.outputs.pop(0)
                    x = computer.outputs.pop(0)
                    y = computer.outputs.pop(0)

                    if dest == 255:
                        nat_last_packet = [x, y]
                    elif 0 <= dest < 50:
                        computers[dest].input_values.append(x)
                        computers[dest].input_values.append(y)

                    idle_count = 0

            if idle_count == 50 and nat_last_packet:
                nat_x, nat_y = nat_last_packet

                if nat_y == nat_last_y:
                    return nat_y

                nat_last_y = nat_y
                computers[0].input_values.append(nat_x)
                computers[0].input_values.append(nat_y)


if __name__ == '__main__':
    Solution().run()
