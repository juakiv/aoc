from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day24")

        self.inputs = {}
        self.gates = {}

        handling_gates = False
        for line in self.data:
            if line == "":
                handling_gates = True
                continue

            if not handling_gates:
                input_key, input_value = line.split(": ")
                self.inputs[input_key] = int(input_value)

            else:
                gate, gate_output = line.split(" -> ")
                self.gates[gate_output] = gate.split(" ")

    def calculate_gate(self, gate: str) -> int:
        if gate in self.inputs:
            return self.inputs[gate]

        output = None
        a, op, b = self.gates[gate]
        if op == "AND":
            output = self.calculate_gate(a) and self.calculate_gate(b)
        elif op == "OR":
            output = self.calculate_gate(a) or self.calculate_gate(b)
        elif op == "XOR":
            output = self.calculate_gate(a) ^ self.calculate_gate(b)

        self.inputs[gate] = output
        return output

    def part1(self) -> int:
        result = ""

        for gate_key in sorted(self.gates.keys()):
            if gate_key.startswith("z"):
                output = self.calculate_gate(gate_key)
                result += str(output)

        return int(result[::-1], 2)
    
    def find_gate(self, a, b, operator):
        for key, value in self.gates.items():
            if value[0] == a and value[2] == b and value[1] == operator or value[0] == b and value[2] == a and value[1] == operator:
                return key
            
        return None
    
    def part2(self) -> str:
        swapped = []
        prev_carry = None
        for i in range(45):
            number = str(i).zfill(2)
            xor_gate, and_gate, and_gate_carry, temp_swap, curr_carry = None, None, None, None, None
            
            xor_gate = self.find_gate(f"x{number}", f"y{number}", "XOR")
            and_gate = self.find_gate(f"x{number}", f"y{number}", "AND")
            
            if prev_carry:
                and_gate_carry = self.find_gate(prev_carry, xor_gate, "AND")
                if not and_gate_carry:
                    xor_gate, and_gate = and_gate, xor_gate
                    swapped.extend([xor_gate, and_gate])
                    and_gate_carry = self.find_gate(prev_carry, xor_gate, "AND")
                
                temp_swap = self.find_gate(prev_carry, xor_gate, "XOR")
                
                if xor_gate and xor_gate.startswith("z"):
                    xor_gate, temp_swap = temp_swap, xor_gate
                    swapped.extend([xor_gate, temp_swap])
                    
                if and_gate and and_gate.startswith("z"):
                    and_gate, temp_swap = temp_swap, and_gate
                    swapped.extend([and_gate, temp_swap])
                    
                if and_gate_carry and and_gate_carry.startswith("z"):
                    and_gate_carry, temp_swap = temp_swap, and_gate_carry
                    swapped.extend([and_gate_carry, temp_swap])
                    
                curr_carry = self.find_gate(and_gate_carry, and_gate, "OR")
                
            if curr_carry and curr_carry.startswith("z") and curr_carry != "z45":
                curr_carry, temp_swap = temp_swap, curr_carry
                swapped.extend([curr_carry, temp_swap])
            
            prev_carry = curr_carry if prev_carry else and_gate
            
        return ",".join(sorted(swapped))


if __name__ == '__main__':
    Solution().run()
