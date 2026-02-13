from collections import defaultdict, deque

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day20", 2019)

        self.grid: list[str] = [line for line in self.data]
        self.rows_count = len(self.grid)
        self.cols_count = max(len(line) for line in self.grid) if self.grid else 0

    def get_char(self, r, c):
        if 0 <= r < len(self.grid) and 0 <= c < len(self.grid[r]):
            return self.grid[r][c]
        return " "

    def part1(self) -> int:
        portals = defaultdict(set)
        maze = set()

        for row in range(self.rows_count):
            for col in range(len(self.grid[row])):
                char = self.grid[row][col]

                if char == ".":
                    maze.add((row, col))

                if char.isupper():
                    char_right = self.get_char(row, col + 1)
                    if char_right.isupper():
                        label = char + char_right
                        if self.get_char(row, col - 1) == ".":
                            portals[label].add((row, col - 1))
                        elif self.get_char(row, col + 2) == ".":
                            portals[label].add((row, col + 2))

                    char_down = self.get_char(row + 1, col)
                    if char_down.isupper():
                        label = char + char_down
                        if self.get_char(row - 1, col) == ".":
                            portals[label].add((row - 1, col))
                        elif self.get_char(row + 2, col) == ".":
                            portals[label].add((row + 2, col))

        jump_map = {}
        start_pos = list(portals["AA"])[0]
        end_pos = list(portals["ZZ"])[0]

        for label, coords in portals.items():
            if len(coords) == 2:
                c1, c2 = list(coords)
                jump_map[c1] = c2
                jump_map[c2] = c1

        queue = [(start_pos, 0)]
        visited = {start_pos}

        while queue:
            (row, col), distance = queue.pop()

            if (row, col) == end_pos:
                return distance

            possible_moves = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            if (row, col) in jump_map:
                possible_moves.append(jump_map[(row, col)])

            for new_row, new_col in possible_moves:
                if (new_row, new_col) in maze and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append(((new_row, new_col), distance + 1))

        return -1

    def part2(self) -> int:
        portals = defaultdict(set)
        maze = set()

        for row in range(self.rows_count):
            for col in range(len(self.grid[row])):
                char = self.grid[row][col]

                if char == ".":
                    maze.add((row, col))

                if char.isupper():
                    if self.get_char(row, col + 1).isupper():
                        label = char + self.get_char(row, col + 1)
                        pos = (row, col - 1) if self.get_char(row, col - 1) == "." else (row, col + 2)
                        if self.get_char(pos[0], pos[1]) == ".":
                            portals[label].add(pos)

                    elif self.get_char(row + 1, col).isupper():
                        label = char + self.get_char(row + 1, col)
                        pos = (row - 1, col) if self.get_char(row - 1, col) == "." else (row + 2, col)
                        if self.get_char(pos[0], pos[1]) == ".":
                            portals[label].add(pos)

        jump_map = {}
        start_pos = list(portals.pop("AA"))[0]
        end_pos = list(portals.pop("ZZ"))[0]

        for label, coords in portals.items():
            c1, c2 = list(coords)
            for current, target in [(c1, c2), (c2, c1)]:
                is_outer = current[0] <= 2 or current[0] >= self.rows_count - 3 or current[1] <= 2 or current[1] >= self.cols_count - 3
                jump_map[current] = (target, -1 if is_outer else 1)

        queue = deque([(start_pos[0], start_pos[1], 0, 0)])
        visited = {(start_pos[0], start_pos[1], 0)}

        while queue:
            row, col, level, distance = queue.popleft()

            if (row, col) == end_pos and level == 0:
                return distance

            for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + d_row, col + d_col
                if (new_row, new_col) in maze and (new_row, new_col, level) not in visited:
                    visited.add((new_row, new_col, level))
                    queue.append((new_row, new_col, level, distance + 1))

            if (row, col) in jump_map:
                (portal_row, portal_col), level_change = jump_map[(row, col)]
                new_level = level + level_change

                if new_level >= 0 and (portal_row, portal_col, new_level) not in visited:
                    visited.add((portal_row, portal_col, new_level))
                    queue.append((portal_row, portal_col, new_level, distance + 1))

        return -1


if __name__ == '__main__':
    Solution().run()
