from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02", 2019)[0]
        self.nums: list[int] = [int(x) for x in self.data.split(",")]

    @staticmethod
    def run_program(nums: list[int]) -> list[int]:
        for i in range(0, len(nums), 4):
            opcode = nums[i]
            if opcode == 1:
                a, b, c = nums[i + 1:i + 4]
                nums[c] = nums[a] + nums[b]
            elif opcode == 2:
                a, b, c = nums[i + 1:i + 4]
                nums[c] = nums[a] * nums[b]
            elif opcode == 99:
                break
            else:
                raise ValueError(f"Unknown opcode: {opcode}")

        return nums

    def part1(self) -> int:
        nums = self.nums.copy()
        nums[1] = 12
        nums[2] = 2

        result = self.run_program(nums)

        return result[0]

    def part2(self) -> int:
        for noun in range(100):
            for verb in range(100):
                nums = self.nums.copy()
                nums[1] = noun
                nums[2] = verb

                result = self.run_program(nums)

                if result[0] == 19690720:
                    return 100 * noun + verb

        return 0


if __name__ == '__main__':
    Solution().run()
