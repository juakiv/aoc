from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day16", 2018, "\n\n\n")

        self.samples: list[list[list[int]]] = []
        self.program: list[list[int]] = []
        self.opcodes = { "addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr" }

        for sample in self.data[0].split("\n\n"):
            lines = sample.split("\n")
            before = list(map(int, lines[0][9:-1].split(", ")))
            instruction = list(map(int, lines[1].split()))
            after = list(map(int, lines[2][9:-1].split(", ")))

            self.samples.append([before, instruction, after])

        for line in self.data[1].split("\n"):
            if line.strip():
                self.program.append(list(map(int, line.split())))

    @staticmethod
    def run_op(opcode, registers, a, b, c):
        register = registers.copy()

        if opcode == "addr":
            register[c] = register[a] + register[b]

        elif opcode == "addi":
            register[c] = register[a] + b

        elif opcode == "mulr":
            register[c] = register[a] * register[b]

        elif opcode == "muli":
            register[c] = register[a] * b

        elif opcode == "banr":
            register[c] = register[a] & register[b]

        elif opcode == "bani":
            register[c] = register[a] & b

        elif opcode == "borr":
            register[c] = register[a] | register[b]

        elif opcode == "bori":
            register[c] = register[a] | b

        elif opcode == "setr":
            register[c] = register[a]

        elif opcode == "seti":
            register[c] = a

        elif opcode == "gtir":
            register[c] = 1 if a > register[b] else 0

        elif opcode == "gtri":
            register[c] = 1 if register[a] > b else 0

        elif opcode == "gtrr":
            register[c] = 1 if register[a] > register[b] else 0

        elif opcode == "eqir":
            register[c] = 1 if a == register[b] else 0

        elif opcode == "eqri":
            register[c] = 1 if register[a] == b else 0

        elif opcode == "eqrr":
            register[c] = 1 if register[a] == register[b] else 0

        return register

    def part1(self) -> int:
        count = 0

        for before, instruction, after in self.samples:
            matches = 0

            for opcode in self.opcodes:
                if self.run_op(opcode, before, instruction[1], instruction[2], instruction[3]) == after:
                    matches += 1

            if matches >= 3:
                count += 1

        return count

    def part2(self) -> int:
        possible_opcodes = { i: set(self.opcodes) for i in range(16) }

        for before, instruction, after in self.samples:
            opcode, a, b, c = instruction

            matches = set()
            for op in self.opcodes:
                if self.run_op(op, before, a, b, c) == after:
                    matches.add(op)

            possible_opcodes[opcode] = possible_opcodes[opcode].intersection(matches)

        resolved = {}
        while len(resolved) < 16:
            newly_resolved = { opcode: next(iter(ops)) for opcode, ops in possible_opcodes.items() if len(ops) == 1 and opcode not in resolved }

            for opcode, op_name in newly_resolved.items():
                resolved[opcode] = op_name
                for other_opcode in possible_opcodes:
                    if other_opcode != opcode:
                        possible_opcodes[other_opcode].discard(op_name)

        registers = [0, 0, 0, 0]
        for opcode, a, b, c in self.program:
            registers = self.run_op(resolved[opcode], registers, a, b, c)

        return registers[0]


if __name__ == '__main__':
    Solution().run()
