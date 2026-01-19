from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day20", 2022)

        self.numbers = [int(line) for line in self.data]

    @staticmethod
    def mix(numbers: list[int], mix_times: int) -> int:
        mixed = list(enumerate(numbers))

        for _ in range(mix_times):
            for original_index in range(len(numbers)):
                current_index = next(i for i, (idx, _) in enumerate(mixed) if idx == original_index)
                value = mixed[current_index][1]
                mixed.pop(current_index)
                new_index = (current_index + value) % len(mixed)
                mixed.insert(new_index, (original_index, value))

        zero_index = next(i for i, (_, val) in enumerate(mixed) if val == 0)

        result = 0
        for offset in [1000, 2000, 3000]:
            result += mixed[(zero_index + offset) % len(mixed)][1]

        return result

    def part1(self) -> int:
        return self.mix(self.numbers, 1)

    def part2(self) -> int:
        new_numbers = [num * 811589153 for num in self.numbers]
        return self.mix(new_numbers, 10)


if __name__ == '__main__':
    Solution().run()
