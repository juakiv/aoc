from heapq import heappop, heappush

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day17", 2023)

    def add_to_heap(self, queue, cost, x, y, dir_x, dir_y, steps):
        new_x = x + dir_x
        new_y = y + dir_y

        if not (0 <= new_x < len(self.data[0]) and 0 <= new_y < len(self.data)):
            return

        heappush(queue, (cost + int(self.data[new_y][new_x]), (new_x, new_y, dir_x, dir_y), steps))

    def dijkstra(self, min_steps: int, max_steps: int) -> int:
        queue = [
            (0, (0, 0, 0, 0), 0)
        ]
        seen = set()

        while queue:
            cost, (x, y, dir_x, dir_y), steps = heappop(queue)

            if steps >= min_steps and x == len(self.data[0]) - 1 and y == len(self.data) - 1:
                return cost

            if (x, y, dir_x, dir_y, steps) in seen:
                continue

            seen.add((x, y, dir_x, dir_y, steps))

            if steps < max_steps and (dir_x, dir_y) != (0, 0):
                self.add_to_heap(queue, cost, x, y, dir_x, dir_y, steps + 1)

            if steps >= min_steps or (dir_x, dir_y) == (0, 0):
                for new_dir_x, new_dir_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if (new_dir_x, new_dir_y) != (dir_x, dir_y) and (new_dir_x, new_dir_y) != (-dir_x, -dir_y):
                        self.add_to_heap(queue, cost, x, y, new_dir_x, new_dir_y, 1)

        return 0


    def part1(self) -> int:
        return self.dijkstra(0, 3)

    def part2(self) -> int:
        return self.dijkstra(4, 10)


if __name__ == '__main__':
    Solution().run()
