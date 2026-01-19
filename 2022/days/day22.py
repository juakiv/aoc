import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day22", 2022, "\n\n")

        self.width = max(len(line) for line in self.data[0].split("\n"))
        self.height = len(self.data[0].split("\n"))

        self.map = [row.ljust(self.width, " ") for row in self.data[0].split("\n")]
        self.instructions = re.findall(r"\d+|[LR]", self.data[1])

    def part1(self) -> int:
        start = (0, self.map[0].index("."))
        direction = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in self.instructions:
            if instruction == "R":
                direction = (direction + 1) % 4
            elif instruction == "L":
                direction = (direction - 1) % 4
            else:
                for _ in range(int(instruction)):
                    next_row = start[0] + directions[direction][0]
                    next_col = start[1] + directions[direction][1]

                    # wrap logic
                    if next_row < 0 or next_row >= self.height or next_col < 0 or next_col >= self.width or self.map[next_row][next_col] == " ":
                        if direction == 0:  # right
                            next_col = next(i for i, c in enumerate(self.map[start[0]]) if c != " ")
                            next_row = start[0]

                        elif direction == 1:  # down
                            next_row = next(i for i in range(self.height) if self.map[i][start[1]] != " ")
                            next_col = start[1]

                        elif direction == 2:  # left
                            next_col = max(i for i, c in enumerate(self.map[start[0]]) if c != " ")
                            next_row = start[0]

                        elif direction == 3:  # up
                            next_row = max(i for i in range(self.height) if self.map[i][start[1]] != " ")
                            next_col = start[1]

                    if self.map[next_row][next_col] == "#":
                        break
                    else:
                        start = (next_row, next_col)

        final_row, final_col = start
        final_facing = direction

        return 1000 * (final_row + 1) + 4 * (final_col + 1) + final_facing

    @staticmethod
    def face(row, col):
        if row < 50 and 50 <= col < 100:
            return 1
        if row < 50 and 100 <= col < 150:
            return 2
        if 50 <= row < 100 and 50 <= col < 100:
            return 3
        if 100 <= row < 150 and col < 50:
            return 4
        if 100 <= row < 150 and 50 <= col < 100:
            return 5
        if 150 <= row < 200 and col < 50:
            return 6
        return None

    def part2(self) -> int:
        direction = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row = 0
        col = self.map[0].index(".")

        for instruction in self.instructions:
            if instruction == "R":
                direction = (direction + 1) % 4
                continue
            if instruction == "L":
                direction = (direction - 1) % 4
                continue

            for _ in range(int(instruction)):
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                next_direction = direction

                if next_row < 0 or next_row >= self.height or next_col < 0 or next_col >= self.width or self.map[next_row][next_col] == " ":
                    current_face = self.face(row, col)
                    local_row = row % 50
                    local_col = col % 50

                    # hard-coded cube transitions
                    if current_face == 1 and direction == 3:  # up → face 6
                        next_row = 150 + local_col
                        next_col = 0
                        next_direction = 0

                    elif current_face == 1 and direction == 2:  # left → face 4
                        next_row = 149 - local_row
                        next_col = 0
                        next_direction = 0

                    elif current_face == 2 and direction == 0:  # right → face 5
                        next_row = 149 - local_row
                        next_col = 99
                        next_direction = 2

                    elif current_face == 2 and direction == 3:  # up → face 6
                        next_row = 199
                        next_col = local_col
                        next_direction = 3

                    elif current_face == 2 and direction == 1:  # down → face 3
                        next_row = 50 + local_col
                        next_col = 99
                        next_direction = 2

                    elif current_face == 3 and direction == 0:  # right → face 2
                        next_row = 49
                        next_col = 100 + local_row
                        next_direction = 3

                    elif current_face == 3 and direction == 2:  # left → face 4
                        next_row = 100
                        next_col = local_row
                        next_direction = 1

                    elif current_face == 4 and direction == 2:  # left → face 1
                        next_row = 49 - local_row
                        next_col = 50
                        next_direction = 0

                    elif current_face == 4 and direction == 3:  # up → face 3
                        next_row = 50 + local_col
                        next_col = 50
                        next_direction = 0

                    elif current_face == 5 and direction == 0:  # right → face 2
                        next_row = 49 - local_row
                        next_col = 149
                        next_direction = 2

                    elif current_face == 5 and direction == 1:  # down → face 6
                        next_row = 150 + local_col
                        next_col = 49
                        next_direction = 2

                    elif current_face == 6 and direction == 0:  # right → face 5
                        next_row = 149
                        next_col = 50 + local_row
                        next_direction = 3

                    elif current_face == 6 and direction == 1:  # down → face 2
                        next_row = 0
                        next_col = 100 + local_col
                        next_direction = 1

                    elif current_face == 6 and direction == 2:  # left → face 1
                        next_row = 0
                        next_col = 50 + local_row
                        next_direction = 1

                if self.map[next_row][next_col] == "#":
                    break

                row, col, direction = next_row, next_col, next_direction
        return 1000 * (row + 1) + 4 * (col + 1) + direction


if __name__ == '__main__':
    Solution().run()
