from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day14", 2020)

        self.instructions = [line.split(" = ") for line in self.data]

    def part1(self) -> int:
        memory = {}
        mask = None

        for instruction in self.instructions:
            if instruction[0] == "mask":
                mask = instruction[1]
                continue

            address = int(instruction[0][4:-1])
            value = list(bin(int(instruction[1]))[2:].zfill(36))

            for i, bit in enumerate(mask):
                if bit != "X":
                    value[i] = bit

            memory[address] = int("".join(value), 2)

        return sum(memory.values())

    def part2(self) -> int:
        memory = {}
        mask = None

        for instruction in self.instructions:
            if instruction[0] == "mask":
                mask = instruction[1]
                continue

            address = list(bin(int(instruction[0][4:-1]))[2:].zfill(36))
            value = int(instruction[1])

            floating = []

            for i, bit in enumerate(mask):
                if bit == "1":
                    address[i] = "1"
                elif bit == "X":
                    address[i] = "X"
                    floating.append(i)

            for combination in range(2 ** len(floating)):
                combination_bits = bin(combination)[2:].zfill(len(floating))
                address_copy = address.copy()

                for bit_index, bit_value in enumerate(combination_bits):
                    address_copy[floating[bit_index]] = bit_value

                final_address = int("".join(address_copy), 2)
                memory[final_address] = value

        return sum(memory.values())


if __name__ == '__main__':
    Solution().run()
