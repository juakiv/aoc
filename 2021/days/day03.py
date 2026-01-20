from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day03", 2021)

    def part1(self) -> int:
        most_common_bits = []
        least_common_bits = []

        for i in range(len(self.data[0])):
            bit_column = [line[i] for line in self.data]
            ones = bit_column.count("1")
            zeros = bit_column.count("0")

            if ones >= zeros:
                most_common_bits.append("1")
                least_common_bits.append("0")
            else:
                most_common_bits.append("0")
                least_common_bits.append("1")

        return int("".join(most_common_bits), 2) * int("".join(least_common_bits), 2)

    def part2(self) -> int:
        oxygen_generator_rating = 0
        co2_scrubber_rating = 0

        for rating_type in ["oxygen", "co2"]:
            filtered_data = self.data[:]
            bit_position = 0

            while len(filtered_data) > 1:
                bit_column = [line[bit_position] for line in filtered_data]
                ones = bit_column.count("1")
                zeros = bit_column.count("0")

                if rating_type == "oxygen":
                    if ones >= zeros:
                        desired_bit = "1"
                    else:
                        desired_bit = "0"
                else:
                    if zeros <= ones:
                        desired_bit = "0"
                    else:
                        desired_bit = "1"

                filtered_data = [line for line in filtered_data if line[bit_position] == desired_bit]
                bit_position += 1

            if rating_type == "oxygen":
                oxygen_generator_rating = int(filtered_data[0], 2)
            else:
                co2_scrubber_rating = int(filtered_data[0], 2)

        return oxygen_generator_rating * co2_scrubber_rating


if __name__ == '__main__':
    Solution().run()
