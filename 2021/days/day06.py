from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06", 2021)

        self.lanternfish = [int(x) for x in self.data[0].split(",")]

    @staticmethod
    def progress_day(fish: list[int]) -> list[int]:
        new_fish = 0
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                new_fish += 1
            else:
                fish[i] -= 1
        fish.extend([8] * new_fish)

        return fish

    def part1(self) -> int:
        fish = self.lanternfish.copy()
        for _ in range(80):
            fish = self.progress_day(fish)

        return len(fish)

    def part2(self) -> int:
        # simulating day by day is too slow for 256 days so instead we can count them by timer value
        fish_counts: list[int] = [0] * 9
        for f in self.lanternfish:
            fish_counts[f] += 1

        for _ in range(256):
            new_fish_counts = fish_counts[1:] + [fish_counts[0]]
            new_fish_counts[6] += fish_counts[0]
            fish_counts = new_fish_counts

        return sum(fish_counts)


if __name__ == '__main__':
    Solution().run()
