import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06", 2023)

        times = map(int, re.findall(r"\d+", self.data[0]))
        distances = map(int, re.findall(r"\d+", self.data[1]))

        self.races: list[tuple[int, int]] = []
        for time, distance in zip(times, distances):
            self.races.append((time, distance))

    def part1(self) -> int:
        total = 1

        for time, distance in self.races:
            wins = 0
            for speed in range(1, time):
                distance_travelled = (time - speed) * speed
                if distance_travelled > distance:
                    wins += 1

            total *= wins

        return total

    def part2(self) -> int:
        wins = 0

        time = int("".join(str(a) for a, _ in self.races))
        distance = int("".join(str(b) for _, b in self.races))

        for speed in range(1, time):
            distance_travelled = (time - speed) * speed
            if distance_travelled > distance:
                wins += 1

        return wins


if __name__ == '__main__':
    Solution().run()
