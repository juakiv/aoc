from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08", 2020)

        self.instructions: list[tuple[str, int]] = []
        for line in self.data:
            op, arg = line.split()
            self.instructions.append((op, int(arg)))

    def part1(self) -> int:
        accumulator = 0
        executed = set()

        program_counter = 0
        while program_counter not in executed and program_counter < len(self.instructions):
            executed.add(program_counter)
            operation, argument = self.instructions[program_counter]
            if operation == "acc":
                accumulator += argument
                program_counter += 1
            elif operation == "jmp":
                program_counter += argument
            elif operation == "nop":
                program_counter += 1

        return accumulator

    def part2(self) -> int:
        for i in range(len(self.instructions)):
            modified_instructions = self.instructions.copy()
            operation, argument = modified_instructions[i]
            if operation == "jmp":
                modified_instructions[i] = ("nop", argument)
            elif operation == "nop":
                modified_instructions[i] = ("jmp", argument)
            else:
                continue

            executed = set()
            program_counter = 0
            accumulator = 0
            terminated_normally = False

            while program_counter not in executed:
                if program_counter >= len(modified_instructions):
                    terminated_normally = True
                    break

                executed.add(program_counter)
                operation, argument = modified_instructions[program_counter]

                if operation == "acc":
                    accumulator += argument
                    program_counter += 1
                elif operation == "jmp":
                    program_counter += argument
                elif operation == "nop":
                    program_counter += 1

            if terminated_normally:
                return accumulator

        return 0


if __name__ == '__main__':
    Solution().run()
