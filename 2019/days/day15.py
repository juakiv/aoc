import copy
from collections import deque

from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day15", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    def oxygen_position(self) -> tuple[dict[tuple[int, int], int], tuple[int, int] | None]:
        start_computer = IntcodeComputer(self.nums.copy())
        directions = { 1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0) }

        start = (0, 0)
        queue = deque([(start[0], start[1], start_computer, 0)])
        distances = {start: 0}

        oxygen_position = None

        while queue:
            x, y, computer, d = queue.popleft()

            for cmd, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if (nx, ny) in distances:
                    continue

                new_computer = copy.deepcopy(computer)
                new_computer.input_values.append(cmd)
                output = new_computer.run()
                status = output[-1]

                if status == 0:
                    distances[(nx, ny)] = -1
                    continue

                distances[(nx, ny)] = d + 1

                if status == 2:
                    oxygen_position = (nx, ny)

                queue.append((nx, ny, new_computer, d + 1))

        return distances, oxygen_position

    def part1(self) -> int:
        visited, oxygen_position = self.oxygen_position()
        return visited[oxygen_position]

    def part2(self) -> int:
        visited, oxygen_position = self.oxygen_position()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        queue = deque([oxygen_position])
        distances = {oxygen_position: 0}

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) in distances or visited.get((new_x, new_y), -1) == -1:
                    continue

                distances[(new_x, new_y)] = distances[(x, y)] + 1
                queue.append((new_x, new_y))

        return max(distances.values())


if __name__ == '__main__':
    Solution().run()
