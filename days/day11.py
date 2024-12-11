from collections import Counter, defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day11")[0]
        self.stones: list[int] = [int(x) for x in self.data.split(" ")]

    @staticmethod
    def blink(stones: dict[int, int]) -> dict[int, int]:
        new_stones: dict[int, int] = defaultdict(int)

        for stone, stone_count in stones.items():
            if stone == 0:
                new_stones[1] += stones[0]
            elif len(str(stone)) % 2 == 0:
                first_half = int(str(stone)[:len(str(stone)) // 2])
                second_half = int(str(stone)[len(str(stone)) // 2:])

                new_stones[first_half] += stones[stone]
                new_stones[second_half] += stones[stone]
            else:
                new_stones[stone * 2024] += stones[stone]

        return new_stones


    def part1(self) -> int:
        current_iteration: int = 1
        stones: dict[int, int] = Counter(self.stones)

        while current_iteration <= 25:
            stones = self.blink(stones)
            current_iteration += 1

        return sum(stones.values())

    def part2(self) -> int:
        current_iteration: int = 1
        stones: dict[int, int] = Counter(self.stones)

        while current_iteration <= 75:
            stones = self.blink(stones)
            current_iteration += 1

        return sum(stones.values())


if __name__ == '__main__':
    Solution().run()
