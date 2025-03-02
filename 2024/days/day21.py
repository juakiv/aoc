from functools import cache
from heapq import heappop, heappush
from typing import Tuple

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day21")

        self.codes: list[str] = self.data

        self.keypad: list[list[str]] = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [" ", "0", "A"]
        ]

        self.directional_keypad: list[list[str]] = [
            [" ", "^", "A"],
            ["<", "v", ">"]
        ]

    def paths(self, keypad: list[list[str]], start: Tuple[int, int], end: Tuple[int, int]):
        deltas = {(0, 1): "v", (0, -1): "^", (1, 0): ">", (-1, 0): "<"}
        queue: list[Tuple[int, Tuple[int, int], list[Tuple[int, int]]]] = [(0, start, [])]
        paths = []
        visited = set()

        visited.add(start)
        visited.add(self.find_position(" ", keypad))

        distance = 0
        min_distance = float("inf")

        while queue and distance <= min_distance:
            cost, current, path = heappop(queue)

            distance = len(path)

            if current == end:
                min_distance = distance
                paths.append("".join(path) + "A")
                continue

            for dx, dy in deltas.keys():
                new_x, new_y = current[0] + dx, current[1] + dy
                if 0 <= new_x < len(keypad[0]) and 0 <= new_y < len(keypad) and (new_x, new_y) not in visited:
                    heappush(queue, (cost + 1, (new_x, new_y), path + [deltas[(dx, dy)]]))
                    visited.add(current)

        return paths

    @staticmethod
    def find_position(character: str, keypad: list[list[str]]) -> Tuple[int, int]:
        for y in range(len(keypad)):
            for x in range(len(keypad[y])):
                if keypad[y][x] == character:
                    return x, y

    @cache
    def complexity_dpad(self, sequence: str, depth: int):
        if depth == 0:
            return len(sequence)

        start = self.find_position("A", self.directional_keypad)
        total = 0

        for character in sequence:
            end = self.find_position(character, self.directional_keypad)
            paths = self.paths(self.directional_keypad, start, end)

            complexities = [self.complexity_dpad(path, depth - 1) for path in paths]
            total += min(complexities)

            start = end

        return total

    def complexity(self, sequence: str, depth: int) -> int:
        start = self.find_position("A", self.keypad)
        total = 0

        for character in sequence:
            end = self.find_position(character, self.keypad)
            paths = self.paths(self.keypad, start, end)

            complexities = [self.complexity_dpad(path, depth) for path in paths]
            total += min(complexities)

            start = end

        return total * int(sequence[:-1])

    def part1(self) -> int:
        return sum(self.complexity(code, 2) for code in self.codes)

    def part2(self) -> int:
        return sum(self.complexity(code, 25) for code in self.codes)


if __name__ == '__main__':
    Solution().run()
