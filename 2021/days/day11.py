import copy

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day11", 2021)

        self.octopuses: list[list[int]] = [list(map(int, list(line))) for line in self.data]

    @staticmethod
    def run_step(octopuses: list[list[int]]) -> tuple[int, list[list[int]]]:
        flashed = set()

        def flash(x: int, y: int) -> None:
            if (x, y) in flashed:
                return

            flashed.add((x, y))
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(octopuses) and 0 <= ny < len(octopuses[0]):
                    octopuses[nx][ny] += 1
                    if octopuses[nx][ny] > 9:
                        flash(nx, ny)

        for x in range(len(octopuses)):
            for y in range(len(octopuses[0])):
                octopuses[x][y] += 1

        for x in range(len(octopuses)):
            for y in range(len(octopuses[0])):
                if octopuses[x][y] > 9:
                    flash(x, y)

        for x, y in flashed:
            octopuses[x][y] = 0

        return len(flashed), octopuses

    def part1(self) -> int:
        total_flashes = 0
        octopuses = copy.deepcopy(self.octopuses)

        for _ in range(100):
            flashes, octopuses = self.run_step(octopuses)
            total_flashes += flashes

        return total_flashes

    def part2(self) -> int:
        step = 0
        octopuses = copy.deepcopy(self.octopuses)

        while True:
            step += 1
            flashes, octopuses = self.run_step(octopuses)

            if flashes == len(octopuses) * len(octopuses[0]):
                break

        return step


if __name__ == '__main__':
    Solution().run()
