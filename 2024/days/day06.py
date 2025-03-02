from typing import Tuple, Set

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06")

        self.guard_initial_position: Tuple[int, int] = (0,0)
        self.obstacles: list[Tuple[int, int]] = []
        self.visited_tiles: Set[Tuple[int, int]] = set()
        self.step_deltas = { "^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0) } # (x, y)

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "#":
                    self.obstacles.append((x, y))
                if self.data[y][x] == "^":
                    self.guard_initial_position = (x, y)

    def guard_is_on_map(self, guard_position: Tuple[int, int]) -> bool:
        return 0 <= guard_position[0] < len(self.data[0]) and 0 <= guard_position[1] < len(self.data)

    def part1(self) -> int:
        current_direction = "^"
        guard_position = self.guard_initial_position
        while self.guard_is_on_map(guard_position):
            self.visited_tiles.add(guard_position)

            next_step = (guard_position[0] + self.step_deltas[current_direction][0], guard_position[1] + self.step_deltas[current_direction][1])
            if next_step in self.obstacles:
                current_direction = list(self.step_deltas.keys())[(list(self.step_deltas.keys()).index(current_direction) + 1) % 4]
            else:
                guard_position = next_step

        return len(self.visited_tiles)

    def part2(self) -> int:
        possible_obstacles = 0

        for obstacle in self.visited_tiles:
            current_direction = "^"
            guard_position = self.guard_initial_position
            guard_positions: Set[Tuple[str, Tuple[int, int]]] = set()

            while self.guard_is_on_map(guard_position):
                next_step = (guard_position[0] + self.step_deltas[current_direction][0], guard_position[1] + self.step_deltas[current_direction][1])
                if next_step in self.obstacles or next_step == obstacle:
                    current_direction = list(self.step_deltas.keys())[(list(self.step_deltas.keys()).index(current_direction) + 1) % 4]
                else:
                    guard_position = next_step

                if (current_direction, guard_position) in guard_positions:
                    possible_obstacles += 1
                    break

                guard_positions.add((current_direction, guard_position))

        return possible_obstacles


if __name__ == '__main__':
    Solution().run()
