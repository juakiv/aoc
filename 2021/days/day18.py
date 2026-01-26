from itertools import permutations

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day18", 2021)

        depth = 0
        self.parsed = []
        for line in self.data:
            parsed_line = []
            for char in line:
                if char == "[":
                    depth += 1
                elif char == "]":
                    depth -= 1
                elif char.isdigit():
                    parsed_line.append((int(char), depth))
            self.parsed.append(parsed_line)

    @staticmethod
    def explode(number):
        for i in range(len(number) - 1):
            if number[i][1] > 4 and number[i][1] == number[i + 1][1]:
                if i > 0:
                    number[i - 1] = (number[i - 1][0] + number[i][0], number[i - 1][1])
                if i + 2 < len(number):
                    number[i + 2] = (number[i + 2][0] + number[i + 1][0], number[i + 2][1])
                number[i] = (0, number[i][1] - 1)
                del number[i + 1]
                return True
        return False

    @staticmethod
    def split(number):
        for i in range(len(number)):
            if number[i][0] >= 10:
                left = number[i][0] // 2
                right = number[i][0] - left
                depth = number[i][1] + 1
                number[i] = (left, depth)
                number.insert(i + 1, (right, depth))
                return True
        return False

    def reduce(self, number):
        while True:
            if self.explode(number):
                continue
            if self.split(number):
                continue
            break

        return number

    @staticmethod
    def calculate_magnitude(number):
        while len(number) > 1:
            for i in range(len(number) - 1):
                if number[i][1] == number[i + 1][1]:
                    magnitude = 3 * number[i][0] + 2 * number[i + 1][0]
                    depth = number[i][1] - 1
                    number[i] = (magnitude, depth)
                    del number[i + 1]
                    break
        return number[0][0]

    def add(self, left, right):
        combined = [(v, d + 1) for v, d in left + right]
        return self.reduce(combined)

    def part1(self) -> int:
        total = self.parsed[0]

        for number in self.parsed[1:]:
            total = self.add(total, number)

        return self.calculate_magnitude(total)

    def part2(self) -> int:
        maximum_magnitude = 0

        for left, right, in permutations(self.parsed, 2):
            summed = self.add(left, right)
            magnitude = self.calculate_magnitude(summed)
            maximum_magnitude = max(maximum_magnitude, magnitude)

        return maximum_magnitude


if __name__ == '__main__':
    Solution().run()
