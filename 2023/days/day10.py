from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day10", 2023)

        for y, row in enumerate(self.data):
            if "S" in row:
                self.start = (row.index("S"), y)

        self.connection_dirs = {
            "|": [(0, -1), (0, 1)],
            "-": [(-1, 0), (1, 0)],
            "L": [(1, 0), (0, -1)],
            "J": [(-1, 0), (0, -1)],
            "7": [(0, 1), (-1, 0)],
            "F": [(1, 0), (0, 1)],
            "S": [(-1, 0), (1, 0), (0, -1), (0, 1)],
            ".": []
        }

    def get_connections(self, position: tuple[int, int]) -> list[tuple[int, int]]:
        x, y = position
        connections = []

        for dx, dy in self.connection_dirs[self.data[y][x]]:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_y < len(self.data) and 0 <= new_x < len(self.data[0]):
                if self.data[new_y][new_x] == ".":
                    continue

                does_connection_come_back = False
                for back_dx, back_dy in self.connection_dirs[self.data[new_y][new_x]]:
                    if new_x + back_dx == x and new_y + back_dy == y:
                        does_connection_come_back = True
                        break

                if does_connection_come_back:
                    connections.append((new_x, new_y))

        return connections

    def get_loop(self):
        points = [self.start]

        current = self.get_connections(self.start)[0]

        while True:
            last = points[-1]
            points.append(current)
            neighbor1, neighbor2 = self.get_connections(current)

            if (self.start in (neighbor1, neighbor2)) and last != self.start:
                break

            current = neighbor1 if neighbor2 == last else neighbor2

        return points

    @staticmethod
    def shoelace(points: list[tuple[int, int]]) -> int:
        n = len(points)
        area = 0

        for i in range(n):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % n]
            area += x1 * y2 - x2 * y1

        return area // 2

    def part1(self) -> int:
        loop = self.get_loop()
        return len(loop) // 2

    def part2(self) -> int:
        loop = self.get_loop()
        area = self.shoelace(loop)
        return int(abs(area) - 0.5  * len(loop) + 1)


if __name__ == '__main__':
    Solution().run()
