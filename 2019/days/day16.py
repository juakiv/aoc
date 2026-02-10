from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day16", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0]]

    @staticmethod
    def fft(numbers: list[int]) -> list[int]:
        pattern = [0, 1, 0, -1]
        output = []

        for i in range(len(numbers)):
            total = 0

            for j in range(len(numbers)):
                total += numbers[j] * pattern[((j + 1) // (i + 1)) % 4]

            output.append(abs(total) % 10)

        return output

    def part1(self) -> int:
        nums = self.nums.copy()

        for _ in range(100):
            nums = self.fft(nums)

        return int("".join(str(x) for x in nums[:8]))

    def part2(self) -> int:
        nums = self.nums.copy() * 10000
        offset = int("".join(str(x) for x in nums[:7]))

        for _ in range(100):
            total = 0

            for i in range(len(nums) - 1, offset - 1, -1):
                total += nums[i]
                nums[i] = total % 10

        return int("".join(str(x) for x in nums[offset:offset + 8]))


if __name__ == '__main__':
    Solution().run()
