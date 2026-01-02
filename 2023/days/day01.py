from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01", 2023)

    def part1(self) -> int:
        calibration_value: int = 0

        for line in self.data:
            digits = [char for char in line if char.isdigit()]
            two_digit_num = int("".join([digits[0], digits[-1]]))
            calibration_value += two_digit_num

        return calibration_value

    def part2(self) -> int:
        calibration_value: int = 0
        numbers_as_string: dict[str, int] = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9
        }

        for line in self.data:
            digits = []

            for index, char in enumerate(line):
                if char.isdigit():
                    digits.append(char)
                else:
                    for word in numbers_as_string.keys():
                        if line[index:].startswith(word):
                            digits.append(str(numbers_as_string[word]))

            two_digit_num = int("".join([digits[0], digits[-1]]))
            calibration_value += two_digit_num

        return calibration_value


if __name__ == '__main__':
    Solution().run()
