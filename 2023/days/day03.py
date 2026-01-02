import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day03", 2023)

        self.numbers: list[list[int]] = []
        for index, line in enumerate(self.data):
            for num in re.finditer(r"\d+", line):
                num_start = num.start() - 1
                num_end = num.end()
                number = int(num.group())
                self.numbers.append([index, num_start, num_end, number])

    @staticmethod
    def is_symbol(chars: str) -> bool:
        return any(char != "." and not char.isdigit() for char in chars)

    def part1(self) -> int:
        total: int = 0

        for number in self.numbers:
            line_index = number[0]
            num_start_index = max(0, number[1])
            num_end_index = min(len(self.data[line_index]) - 1, number[2])
            num_value = number[3]

            if (self.is_symbol(self.data[line_index][max(0, num_start_index)])) or \
                (num_end_index <= len(self.data[line_index]) and self.is_symbol(self.data[line_index][num_end_index])) or \
                (line_index - 1 >= 0 and self.is_symbol(self.data[line_index - 1][num_start_index:num_end_index + 1])) or \
                (line_index + 1 < len(self.data) and self.is_symbol(self.data[line_index + 1][num_start_index:num_end_index + 1])):
                total += num_value

        return total

    def part2(self) -> int:
        gear_ratio_sum: int = 0

        nums_on_line: list[list[tuple[int, int, int]]] = []
        for line_index, line in enumerate(self.data):
            nums_on_line.append([])
            for num in re.finditer(r"\d+", line):
                number = int(num.group())
                start_index = num.start() - 1
                end_index = num.end()
                nums_on_line[line_index].append((start_index, end_index, number))

        for line_index, line in enumerate(self.data):
            for char_index, char in enumerate(line):
                if char != "*":
                    continue

                adjacent_nums: list[int] = []

                for diff in [-1, 0, 1]:
                    check_line_index = line_index + diff
                    if check_line_index < 0 or check_line_index >= len(self.data):
                        continue

                    for num in nums_on_line[check_line_index]:
                        start_index, end_index, number = num
                        if start_index <= char_index <= end_index:
                            adjacent_nums.append(number)

                if len(adjacent_nums) == 2:
                    gear_ratio_sum += adjacent_nums[0] * adjacent_nums[1]

        return gear_ratio_sum


if __name__ == '__main__':
    Solution().run()
