from heapq import heappop, heappush
from typing import Tuple, Optional

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day16_test")

        self.walls: set[Tuple[int, int]] = set()
        self.start = (0, 0)
        self.end = (0, 0)

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "#":
                    self.walls.add((x, y))
                elif self.data[y][x] == "S":
                    self.start = (x, y)
                elif self.data[y][x] == "E":
                    self.end = (x, y)

        self.map_size = (len(self.data[0]), len(self.data))

    def dijkstra_pathfinding(self, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[Optional[list[Tuple[int, int]]], Optional[int]]:
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue: list[Tuple[int, Tuple[int, int], list[Tuple[int, int]], Tuple[int, int] | None]] = [(0, start, [start], (1, 0))]
        visited = set()

        while queue:
            cost, current, path, prev_direction = heappop(queue)

            if current in visited:
                continue

            visited.add(current)

            if current == end:
                return path, cost

            for dx, dy in deltas:
                neighbor = (current[0] + dx, current[1] + dy)
                if neighbor in visited or neighbor in self.walls:
                    continue

                movement_cost = 1
                if prev_direction and (dx, dy) != prev_direction:
                    movement_cost += 1000

                heappush(queue, (cost + movement_cost, neighbor, path + [neighbor], (dx, dy)))

        return None, None

    def print_path(self, path: list[Tuple[int, int]]):
        for y in range(self.map_size[1]):
            for x in range(self.map_size[0]):
                if (x, y) in self.walls:
                    print("#", end="")
                elif (x, y) == self.start:
                    print("S", end="")
                elif (x, y) == self.end:
                    print("E", end="")
                elif (x, y) in path:
                    print("X", end="")
                else:
                    print(".", end="")
            print()

    def part1(self) -> int:
        path, cost = self.dijkstra_pathfinding(self.start, self.end)
        return cost

    def part2(self) -> int:
        path, lowest_cost = self.dijkstra_pathfinding(self.start, self.end)
        tiles_on_path = set()
        tiles_on_path.update(path)

        for tile_x, tile_y in path:
            if (tile_x, tile_y) == self.start or (tile_x, tile_y) == self.end:
                continue

            self.walls.add((tile_x, tile_y))
            path, cost = self.dijkstra_pathfinding(self.start, self.end)
            if cost == lowest_cost:
                tiles_on_path.update(path)

            self.walls.remove((tile_x, tile_y))

        return len(tiles_on_path)


if __name__ == '__main__':
    Solution().run()
