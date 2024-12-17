from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day17")

        for line in self.data:
            if "Register A:" in line:
                self.register_a = int(line.split(": ")[1])
            elif "Register B:" in line:
                self.register_b = int(line.split(": ")[1])
            elif "Register C:" in line:
                self.register_c = int(line.split(": ")[1])
            elif "Program:" in line:
                self.program = [int(x) for x in line.split(": ")[1].split(",")]

    @staticmethod
    def run_program(register_a: int, register_b: int, register_c: int, program: list[int]) -> list[int]:
        instruction_pointer = 0
        program_output: list[int] = []

        while instruction_pointer < len(program):
            opcode = program[instruction_pointer]
            operand = program[instruction_pointer + 1]

            combo = operand if operand <= 3 else register_a if operand == 4 else register_b if operand == 5 else register_c if operand == 6 else 0

            if opcode == 0:
                register_a = register_a // 2**combo
            elif opcode == 1:
                register_b = register_b ^ operand
            elif opcode == 2:
                register_b = combo % 8
            elif opcode == 3:
                if register_a != 0:
                    instruction_pointer = operand
                    continue
            elif opcode == 4:
                register_b = register_b ^ register_c
            elif opcode == 5:
                program_output.append(combo % 8)
            elif opcode == 6:
                register_b = register_a // 2**combo
            elif opcode == 7:
                register_c = register_a // 2**combo

            instruction_pointer += 2

        return program_output

    def part1(self) -> str:
        program_output = self.run_program(self.register_a, self.register_b, self.register_c, self.program)
        return ",".join([str(x) for x in program_output])

    def part2(self) -> int:
        valid = [0]
        for i in range(1, len(self.program) + 1):
            new_valid = []
            for num in valid:
                for offset in range(8):
                    new_num = 8 * num + offset
                    if self.run_program(new_num, 0, 0, self.program) == self.program[-i:]:
                        new_valid.append(new_num)
            valid = new_valid

        return min(valid)


if __name__ == '__main__':
    Solution().run()
