from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09", 2020)

        self.nums = [int(line) for line in self.data]

    def find_invalid_number(self, preamble_length: int) -> int:
        for i in range(preamble_length, len(self.nums)):
            preamble = self.nums[i - preamble_length:i]
            current_num = self.nums[i]
            found = False

            for j in range(preamble_length):
                for k in range(j + 1, preamble_length):
                    if preamble[j] + preamble[k] == current_num:
                        found = True
                        break

                if found:
                    break

            if not found:
                return current_num

        return 0

    def part1(self) -> int:
        preamble_length = 5 if self.is_test else 25
        return self.find_invalid_number(preamble_length)

    def part2(self) -> int:
        invalid_number = self.find_invalid_number(5 if self.is_test else 25)

        for start_index in range(len(self.nums)):
            total = 0
            end_index = start_index

            while total < invalid_number and end_index < len(self.nums):
                total += self.nums[end_index]
                end_index += 1

            if total == invalid_number:
                contiguous_range = self.nums[start_index:end_index]
                return min(contiguous_range) + max(contiguous_range)

        return 0


if __name__ == '__main__':
    Solution().run()
