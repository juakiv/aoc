from typing import Tuple

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day15")

        self.direction_deltas: dict[str, Tuple[int, int]] = { "^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0) }

        self.map_size: Tuple[int, int] = (0, 0)
        self.walls: set[Tuple[int, int]] = set()
        self.robot: Tuple[int, int] = (0, 0)
        self.robot2: Tuple[int, int] = (0, 0)
        self.boxes: set[Tuple[int, int]] = set()
        self.sequence: list[str] = []

        self.grid: dict[Tuple[int, int], str] = {}

        map_height = 0
        for y in range(len(self.data)):
            if "#" in self.data[y]:
                map_height += 1
                for x in range(len(self.data[y])):
                    if self.data[y][x] == "#":
                        self.walls.add((x, y))
                    elif self.data[y][x] == "@":
                        self.robot = (x, y)
                    elif self.data[y][x] == "O":
                        self.boxes.add((x, y))
            else:
                self.sequence.extend(self.data[y])

        for y, row in enumerate(self.data):
            for x, character in enumerate(row):
                if character in "#.":
                    self.grid[(2 * x, y)] = character
                    self.grid[(2 * x + 1, y)] = character
                elif character == "O":
                    self.grid[(2 * x, y)] = "["
                    self.grid[(2 * x + 1, y)] = "]"
                elif character == "@":
                    self.grid[(2 * x, y)] = character
                    self.grid[(2 * x + 1, y)] = "."
                    self.robot2 = (2 * x, y)

        self.map_size = (len(self.data[0]), map_height)

    def push(self, from_tile: Tuple[int, int], direction: str) -> bool:
        delta = self.direction_deltas[direction]
        to_tile = (from_tile[0] + delta[0], from_tile[1] + delta[1])

        if to_tile not in self.walls and to_tile not in self.boxes:
            self.robot = to_tile
            return True
        elif to_tile in self.walls:
            return False
        elif to_tile in self.boxes:
            if self.push(to_tile, direction):
                self.boxes.remove(to_tile)
                self.boxes.add((to_tile[0] + delta[0], to_tile[1] + delta[1]))
                self.robot = to_tile
                return True
            else:
                return False

    def print_map(self):
        for y in range(self.map_size[1]):
            for x in range(self.map_size[0]):
                if (x, y) in self.walls:
                    print("#", end="")
                elif (x, y) == self.robot:
                    print("@", end="")
                elif (x, y) in self.boxes:
                    print("O", end="")
                else:
                    print(".", end="")
            print()

    def part1(self) -> int:
        for direction in self.sequence:
            self.push(self.robot, direction)

        return sum([box[1] * 100 + box[0] for box in self.boxes])


    # part 2

    def print_map_part2(self):
        for y in range(self.map_size[1]):
            for x in range(self.map_size[0] * 2):
                print(self.grid[(x, y)], end="")
            print()

    def try_move(self, from_tile: Tuple[int, int], direction: str) -> bool:
        delta = self.direction_deltas[direction]
        positions = [from_tile]

        if delta[1] != 0:
            if self.grid[from_tile] == "[":
                positions.append((from_tile[0] + 1, from_tile[1]))
            elif self.grid[from_tile] == "]":
                positions.append((from_tile[0] - 1, from_tile[1]))

        for position in positions:
            to_tile = (position[0] + delta[0], position[1] + delta[1])
            if self.grid[to_tile] == ".":
                continue
            elif self.grid[to_tile] == "#":
                return False
            elif self.grid[to_tile] in "[]":
                if not self.try_move(to_tile, direction):
                    return False

        return True

    def push_part2(self, from_tile: Tuple[int, int], direction: str) -> bool:
        if not self.try_move(from_tile, direction):
            return False

        delta = self.direction_deltas[direction]
        positions = [from_tile]

        if delta[1] != 0:
            if self.grid[from_tile] == "[":
                positions.append((from_tile[0] + 1, from_tile[1]))
            elif self.grid[from_tile] == "]":
                positions.append((from_tile[0] - 1, from_tile[1]))

        for position in positions:
            character_at = self.grid[position]
            to_tile = (position[0] + delta[0], position[1] + delta[1])
            if self.grid[to_tile] == ".":
                self.grid[position] = "."
                self.grid[to_tile] = character_at
            elif self.grid[to_tile] == "#":
                continue
            elif self.grid[to_tile] in "[]":
                self.push_part2(to_tile, direction)
                self.grid[position] = "."
                self.grid[to_tile] = character_at

        return True


    def part2(self) -> int:
        self.print_map_part2()

        robot_position = self.robot2
        for direction in self.sequence:
            if self.push_part2(robot_position, direction):
                robot_position = (robot_position[0] + self.direction_deltas[direction][0], robot_position[1] + self.direction_deltas[direction][1])

        print()
        self.print_map_part2()
        return sum(100 * y + x for (x, y) in self.grid if self.grid[(x, y)] == "[")


if __name__ == '__main__':
    Solution().run()
