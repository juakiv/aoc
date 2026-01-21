from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05", 2021)

        self.points = []
        for line in self.data:
            start, end = line.split(" -> ")
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            self.points.append(((x1, y1), (x2, y2)))

    def part1(self) -> int:
        points = {}
        for (x1, y1), (x2, y2) in self.points:
            if x1 == x2:
                step = 1 if y2 > y1 else -1
                for y in range(y1, y2 + step, step):
                    points[(x1, y)] = points.get((x1, y), 0) + 1
            elif y1 == y2:
                step = 1 if x2 > x1 else -1
                for x in range(x1, x2 + step, step):
                    points[(x, y1)] = points.get((x, y1), 0) + 1

        return sum(1 for count in points.values() if count >= 2)

    def part2(self) -> int:
        points = {}
        for (x1, y1), (x2, y2) in self.points:
            if x1 == x2:
                step = 1 if y2 > y1 else -1
                for y in range(y1, y2 + step, step):
                    points[(x1, y)] = points.get((x1, y), 0) + 1
            elif y1 == y2:
                step = 1 if x2 > x1 else -1
                for x in range(x1, x2 + step, step):
                    points[(x, y1)] = points.get((x, y1), 0) + 1
            else:
                x_step = 1 if x2 > x1 else -1
                y_step = 1 if y2 > y1 else -1
                x_range = range(x1, x2 + x_step, x_step)
                y_range = range(y1, y2 + y_step, y_step)
                for x, y in zip(x_range, y_range):
                    points[(x, y)] = points.get((x, y), 0) + 1

        return sum(1 for count in points.values() if count >= 2)


if __name__ == '__main__':
    Solution().run()
