from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06", 2017)[0]

        self.banks: list[int] = [int(x) for x in self.data.split()]

    @staticmethod
    def redistribute(banks: list[int]) -> tuple[int, tuple]:
        seen = set()
        steps = 0

        while True:
            state = tuple(banks)

            if state in seen:
                return steps, state

            seen.add(state)

            max_blocks = max(banks)
            index = banks.index(max_blocks)
            banks[index] = 0

            for _ in range(max_blocks):
                index = (index + 1) % len(banks)
                banks[index] += 1

            steps += 1

    def part1(self) -> int:
        steps, _ = self.redistribute(self.banks.copy())
        return steps

    def part2(self) -> int:
        _, state = self.redistribute(self.banks.copy())
        return self.redistribute(list(state))[0]



if __name__ == '__main__':
    Solution().run()
