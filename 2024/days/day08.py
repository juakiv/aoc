from itertools import combinations
from typing import Tuple, Set

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08")

        self.nodes: dict[str, list[Tuple[int, int]]] = {}

        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if self.data[y][x] != ".":
                    if self.data[y][x] not in self.nodes:
                        self.nodes[self.data[y][x]] = [(x, y)]
                    else:
                        self.nodes[self.data[y][x]].append((x, y))

    @staticmethod
    def calculate_antinode_position(x1, x2, y1, y2) -> Tuple[int, int]:
        return x2 + (x2 - x1), y2 + (y2 - y1)

    def is_in_map(self, x: int, y: int) -> bool:
        return 0 <= x < len(self.data[0]) and 0 <= y < len(self.data)

    def part1(self) -> int:
        antinodes: Set[Tuple[int, int]] = set()

        for node_coordinates in self.nodes.values():
            for (x1, y1), (x2, y2) in combinations(node_coordinates, 2):
                antinode1 = self.calculate_antinode_position(x1, x2, y1, y2)
                antinode2 = self.calculate_antinode_position(x2, x1, y2, y1)

                if self.is_in_map(*antinode1):
                    antinodes.add(antinode1)

                if self.is_in_map(*antinode2):
                    antinodes.add(antinode2)

        return len(antinodes)

    def part2(self) -> int:
        antinodes: Set[Tuple[int, int]] = set()

        for node_coordinates in self.nodes.values():
            for (x1, y1), (x2, y2) in combinations(node_coordinates, 2):
                antinode1 = list(self.calculate_antinode_position(x1, x2, y1, y2))
                antinode2 = list(self.calculate_antinode_position(x2, x1, y2, y1))

                antinodes.add((x1, y1))
                antinodes.add((x2, y2))

                while self.is_in_map(*antinode1):
                    antinodes.add((antinode1[0], antinode1[1]))
                    antinode1[0] += x2 - x1
                    antinode1[1] += y2 - y1

                while self.is_in_map(*antinode2):
                    antinodes.add((antinode2[0], antinode2[1]))
                    antinode2[0] += x1 - x2
                    antinode2[1] += y1 - y2

        return len(antinodes)


if __name__ == '__main__':
    Solution().run()
