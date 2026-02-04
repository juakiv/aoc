from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    # day 2, intcode computer
    @staticmethod
    def run_program(nums: list[int], input_value: int) -> list[int]:
        i = 0
        outputs = []

        while True:
            instruction = nums[i]
            opcode = instruction % 100
            mode1 = (instruction // 100) % 10
            mode2 = (instruction // 1000) % 10

            if opcode == 99:
                break

            if opcode == 1:
                a = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                b = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                nums[nums[i + 3]] = a + b
                i += 4

            elif opcode == 2:
                a = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                b = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                nums[nums[i + 3]] = a * b
                i += 4

            elif opcode == 3:
                nums[nums[i + 1]] = input_value
                i += 2

            elif opcode == 4:
                value = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                outputs.append(value)
                i += 2

            elif opcode == 5:
                a = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                b = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                if a != 0:
                    i = b
                else:
                    i += 3
            elif opcode == 6:
                a = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                b = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                if a == 0:
                    i = b
                else:
                    i += 3

            elif opcode == 7:
                a = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                b = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                nums[nums[i + 3]] = 1 if a < b else 0
                i += 4

            elif opcode == 8:
                a = nums[nums[i + 1]] if mode1 == 0 else nums[i + 1]
                b = nums[nums[i + 2]] if mode2 == 0 else nums[i + 2]
                nums[nums[i + 3]] = 1 if a == b else 0
                i += 4

            else:
                raise ValueError(f"Invalid opcode {opcode}")

        return outputs

    def part1(self) -> int:
        outputs = self.run_program(self.nums.copy(), 1)
        return outputs[-1] if outputs else 0

    def part2(self) -> int:
        outputs = self.run_program(self.nums.copy(), 5)
        return outputs[-1] if outputs else 0


if __name__ == '__main__':
    Solution().run()
