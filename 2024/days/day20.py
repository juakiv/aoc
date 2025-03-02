from typing import Tuple, Set

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day20")

        self.start: Tuple[int, int] = (0, 0)
        self.end: Tuple[int, int] = (0, 0)
        self.track: Set[Tuple[int, int]] = set()

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "S":
                    self.start = (x, y)
                    self.track.add((x, y))
                elif self.data[y][x] == "E":
                    self.end = (x, y)
                    self.track.add((x, y))
                elif self.data[y][x] == ".":
                    self.track.add((x, y))

    @staticmethod
    def cheat_savings(position: Tuple[int, int], track: Set[Tuple[int, int]], savings: int, allowed_cheats: int) -> int:
        path: list[Tuple[int, int]] = []
        while track:
            path.append(position)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_position = (position[0] + dx, position[1] + dy)
                if new_position in track:
                    break

            track.remove(position)
            position = new_position

        count_cheats = 0
        for i, point in enumerate(path):
            offset = i + savings
            for j, point2 in enumerate(path[offset + 2:], offset + 2):
                distance = tuple(a - b for a, b in zip(point, point2))
                if abs(distance[0]) + abs(distance[1]) <= min(j - offset, allowed_cheats):
                    count_cheats += 1

        return count_cheats

    def part1(self) -> int:
        starting_position = self.start
        track = self.track.copy()
        return self.cheat_savings(starting_position, track, 100, 2)

    def part2(self) -> int:
        starting_position = self.start
        track = self.track.copy()
        return self.cheat_savings(starting_position, track, 100, 20)


if __name__ == '__main__':
    Solution().run()
