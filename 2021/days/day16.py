import math

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day16", 2021)[0]

    @staticmethod
    def hexadecimal_to_binary(hex_string: str) -> str:
        num_of_bits = len(hex_string) * 4
        return bin(int(hex_string, 16))[2:].zfill(num_of_bits)

    def parse_packet(self, binary_string: str) -> tuple[int, int, int]:
        version_sum = int(binary_string[0:3], 2)
        type_id = int(binary_string[3:6], 2)

        index = 6

        if type_id == 4:
            value = ""
            while True:
                group = binary_string[index:index+5]
                value += group[1:]
                index += 5
                if group[0] == "0":
                    break

            return version_sum, index, int(value, 2)

        length_type_id = binary_string[index]
        index += 1
        values = []

        if length_type_id == "0":
            total_length_in_bits = int(binary_string[index:index+15], 2)
            index += 15
            end = index + total_length_in_bits

            while index < end:
                version, idx, value = self.parse_packet(binary_string[index:])
                version_sum += version
                index += idx
                values.append(value)

        else:
            number_of_subpackets = int(binary_string[index:index+11], 2)
            index += 11

            for _ in range(number_of_subpackets):
                version, idx, value = self.parse_packet(binary_string[index:])
                version_sum += version
                index += idx
                values.append(value)

        operations = {
            0: sum,
            1: lambda vals: math.prod(vals),
            2: min,
            3: max,
            5: lambda vals: 1 if vals[0] > vals[1] else 0,
            6: lambda vals: 1 if vals[0] < vals[1] else 0,
            7: lambda vals: 1 if vals[0] == vals[1] else 0,
        }

        value = operations[type_id](values)
        return version_sum, index, value

    def part1(self) -> int:
        binary_string = self.hexadecimal_to_binary(self.data)
        version_sum, _, _ = self.parse_packet(binary_string)
        return version_sum

    def part2(self) -> int:
        binary_string = self.hexadecimal_to_binary(self.data)
        _, _, value = self.parse_packet(binary_string)
        return value


if __name__ == '__main__':
    Solution().run()
