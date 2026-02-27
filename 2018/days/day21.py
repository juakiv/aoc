from solution.base import SolutionBase

from day16 import Solution as Day16


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day21", 2018)

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

            if ip == len(self.instructions) - 1:
                break

            op, a, b, c = self.instructions[ip]
            registers = Day16.run_op(op, registers, a, b, c)

            ip = registers[self.ip_register] + 1

        return max(registers)

    def part2(self) -> int:
        magic_constant = max(a for (op, a, b, c) in self.instructions if op == "seti")

        seen = set()
        last = None
        register4 = 0

        # thank you reddit :(
        while True:
            register3 = register4 | 65536
            register4 = magic_constant

            while True:
                register4 = (register4 + (register3 & 255)) & 16777215
                register4 = (register4 * 65899) & 16777215

                if register3 < 256:
                    break
                register3 //= 256

            if register4 in seen:
                break

            seen.add(register4)
            last = register4

        return last



if __name__ == '__main__':
    Solution().run()
