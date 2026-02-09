from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day14", 2019)

        self.reactions = {}
        for line in self.data:
            inputs, output = line.split(" => ")
            output_amount, output_chemical = output.split(" ")
            input_chemicals = []
            for input_ in inputs.split(", "):
                input_amount, input_chem = input_.split(" ")
                input_chemicals.append((input_chem, int(input_amount)))
            self.reactions[output_chemical] = (int(output_amount), input_chemicals)

    def ore_for_fuel(self, fuel_amount: int) -> int:
        needed_chemicals = defaultdict(int)
        needed_chemicals["FUEL"] = fuel_amount
        surplus_chemicals = defaultdict(int)
        total_ore = 0

        while needed_chemicals:
            chemical, amount_needed = needed_chemicals.popitem()

            if chemical == "ORE":
                total_ore += amount_needed
                continue

            if surplus_chemicals[chemical] >= amount_needed:
                surplus_chemicals[chemical] -= amount_needed
                continue

            amount_needed -= surplus_chemicals[chemical]
            surplus_chemicals[chemical] = 0

            output_amount, inputs = self.reactions[chemical]
            runs = (amount_needed + output_amount - 1) // output_amount
            surplus_chemicals[chemical] += runs * output_amount - amount_needed

            for in_chemical, in_amount in inputs:
                needed_chemicals[in_chemical] += in_amount * runs

        return total_ore

    def part1(self) -> int:
        return self.ore_for_fuel(1)

    def part2(self) -> int:
        ore_budget = 1_000_000_000_000

        low, high = 1, 1
        while self.ore_for_fuel(high) <= ore_budget:
            high *= 2

        while low < high:
            mid = (low + high + 1) // 2
            if self.ore_for_fuel(mid) <= ore_budget:
                low = mid
            else:
                high = mid - 1

        return low


if __name__ == '__main__':
    Solution().run()
