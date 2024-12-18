from heapq import heappop, heappush
from typing import Tuple, Set, Optional

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day18")

        self.is_test_data = len(self.data) < 100

        self.area_size: Tuple[int, int] = (71, 71) if not self.is_test_data else (7, 7)
        self.corrupted_bytes: Set[Tuple[int, int]] = set()


    def simulate_corruption(self, count: int):
        for byte in self.data:
            x, y = byte.split(",")
            self.corrupted_bytes.add((int(x), int(y)))

            if len(self.corrupted_bytes) == count:
                break

    def dijkstra(self, start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[Optional[list[Tuple[int, int]]], Optional[int]]:
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue: list[Tuple[int, Tuple[int, int], list[Tuple[int, int]]]] = [(0, start, [start])]
        visited = set()

        while queue:
            cost, current, path = heappop(queue)

            if current in visited:
                continue


            if current == end:
                return path, cost

            for dx, dy in deltas:
                nx, ny = current[0] + dx, current[1] + dy
                if 0 <= nx < self.area_size[0] and 0 <= ny < self.area_size[1] and (nx, ny) not in visited and (nx, ny) not in self.corrupted_bytes:
                    heappush(queue, (cost + 1, (nx, ny), path + [(nx, ny)]))
                    visited.add(current)


        return None, None

    def print_area(self, path: list[Tuple[int, int]]):
        for y in range(self.area_size[1]):
            for x in range(self.area_size[0]):
                if (x, y) in self.corrupted_bytes:
                    print("#", end="")
                elif (x, y) in path:
                    print("O", end="")
                else:
                    print(".", end="")
            print()

    def part1(self) -> int:
        self.simulate_corruption(1024)

        path, cost = self.dijkstra((0, 0), (70, 70))

        self.print_area(path)

        return cost

    def part2(self) -> Tuple[int, int]:
        answer: Tuple[int, int] = (0, 0)

        for i, position in enumerate(self.data[1024:]):
            x, y = position.split(",")
            self.corrupted_bytes.add((int(x), int(y)))

            path, cost = self.dijkstra((0, 0), (70, 70))

            if not path:
                answer = (int(x), int(y))
                break

        return answer


if __name__ == '__main__':
    Solution().run()
