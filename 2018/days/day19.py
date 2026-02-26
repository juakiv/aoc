from solution.base import SolutionBase

from day16 import Solution as Day16


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day19", 2018)

        self.ip_register = int(self.data[0].split()[1])
        self.instructions = []

        for line in self.data[1:]:
            parts = line.split()
            opcode = parts[0]
            a, b, c = map(int, parts[1:])
            self.instructions.append((opcode, a, b, c))

    def part1(self) -> int:
        registers = [0] * 6
        ip = 0

        while 0 <= ip < len(self.instructions):
            registers[self.ip_register] = ip
            opcode, a, b, c = self.instructions[ip]
            registers = Day16.run_op(opcode, registers, a, b, c)
            ip = registers[self.ip_register] + 1

        return registers[0]

    def part2(self) -> int:
        registers = [0] * 6
        registers[0] = 1
        ip = 0

        while ip != 1:
            registers[self.ip_register] = ip
            op, a, b, c = self.instructions[ip]
            registers = Day16.run_op(op, registers, a, b, c)
            ip = registers[self.ip_register] + 1

        target = max(registers)

        total = 0
        for i in range(1, int(target ** 0.5) + 1):
            if target % i == 0:
                total += i
                if i != target // i:
                    total += target // i

        return total


if __name__ == '__main__':
    Solution().run()
