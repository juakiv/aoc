from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01", 2025)

        self.rotations = [(rotation[0], int(rotation[1:])) for rotation in self.data]

    def part1(self) -> int:
        password = 50
        number_of_zeroes = 0

        for rotation in self.rotations:
            direction_multiplier = 1 if rotation[0] == 'R' else -1
            password = (password + direction_multiplier * rotation[1]) % 100

            if password == 0:
                number_of_zeroes += 1

        return number_of_zeroes

    def part2(self) -> int:
        password = 50
        number_of_zeroes = 0

        for rotation in self.rotations:
            for _step in range(rotation[1]):
                direction_multiplier = 1 if rotation[0] == 'R' else -1
                password = (password + direction_multiplier) % 100

                if password == 0:
                    number_of_zeroes += 1

        return number_of_zeroes


if __name__ == '__main__':
    Solution().run()
