from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08", 2017)

        self.instructions: list[dict[str, str | int]] = []
        for line in self.data:
            parts = line.split()
            self.instructions.append({
                "register": parts[0],
                "operation": parts[1],
                "amount": int(parts[2]),
                "condition_register": parts[4],
                "condition_operator": parts[5],
                "condition_amount": int(parts[6])
            })

    @staticmethod
    def process_instruction(registers: dict[str, int], instruction: dict[str, str | int]) -> dict[str, int]:
        condition_register = instruction["condition_register"]
        condition_operator = instruction["condition_operator"]
        condition_amount = instruction["condition_amount"]

        if condition_register not in registers:
            registers[condition_register] = 0

        condition_met = False
        if condition_operator == "==":
            condition_met = registers[condition_register] == condition_amount
        elif condition_operator == "!=":
            condition_met = registers[condition_register] != condition_amount
        elif condition_operator == ">":
            condition_met = registers[condition_register] > condition_amount
        elif condition_operator == "<":
            condition_met = registers[condition_register] < condition_amount
        elif condition_operator == ">=":
            condition_met = registers[condition_register] >= condition_amount
        elif condition_operator == "<=":
            condition_met = registers[condition_register] <= condition_amount

        if condition_met:
            register = instruction["register"]
            operation = instruction["operation"]
            amount = instruction["amount"]

            if register not in registers:
                registers[register] = 0

            if operation == "inc":
                registers[register] += amount
            elif operation == "dec":
                registers[register] -= amount

        return registers

    def part1(self) -> int:
        registers = {}
        for instruction in self.instructions:
            registers = self.process_instruction(registers, instruction)

        return max(registers.values()) if registers else 0

    def part2(self) -> int:
        registers = {}
        max_value = 0

        for instruction in self.instructions:
            registers = self.process_instruction(registers, instruction)
            current_max = max(registers.values()) if registers else 0
            max_value = max(max_value, current_max)

        return max_value


if __name__ == '__main__':
    Solution().run()
