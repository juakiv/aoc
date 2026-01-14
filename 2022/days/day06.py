from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06", 2022)[0]

    def get_processed_chars_count(self, window_length: int) -> int:
        for i in range(len(self.data) - window_length):
            chars = self.data[i:i + window_length]
            if len(set(chars)) == window_length:
                return i + window_length
        return 0

    def part1(self) -> int:
        return self.get_processed_chars_count(4)

    def part2(self) -> int:
        return self.get_processed_chars_count(14)


if __name__ == '__main__':
    Solution().run()
