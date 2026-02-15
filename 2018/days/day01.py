from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day01", 2018)
        self.nums: list[int] = [int(x) for x in self.data]

    def part1(self) -> int:
        frequency = 0

        for num in self.nums:
            frequency += num

        return frequency

    def part2(self) -> int:
        repeated_frequency = 0

        frequencies = set()
        while True:
            for num in self.nums:
                repeated_frequency += num

                if repeated_frequency in frequencies:
                    return repeated_frequency

                frequencies.add(repeated_frequency)

if __name__ == '__main__':
    Solution().run()
