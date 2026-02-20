import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day10", 2018)

        self.points: list[tuple[int, int]] = []
        self.velocities: list[tuple[int, int]] = []

        for line in self.data:
            nums = re.findall(r'-?\d+', line)
            self.points.append((int(nums[0]), int(nums[1])))
            self.velocities.append((int(nums[2]), int(nums[3])))

    def simulate_movement(self, steps: int) -> list[tuple[int, int]]:
        new_points = []
        for i in range(len(self.points)):
            x = self.points[i][0] + self.velocities[i][0] * steps
            y = self.points[i][1] + self.velocities[i][1] * steps
            new_points.append((x, y))
        return new_points

    @staticmethod
    def bounding_area(points: list[tuple[int, int]]) -> int:
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)
        return (max_x - min_x) * (max_y - min_y)

    @staticmethod
    def print_points(points: list[tuple[int, int]]):
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)

        grid = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

        for x, y in points:
            grid[y - min_y][x - min_x] = "#"

        for row in grid:
            print("".join(row))

    def run_simulation(self) -> tuple[list[tuple[int, int]], int]:
        prev_area = float("inf")
        best_points = None

        time = 0
        while True:
            points = self.simulate_movement(time)
            area = self.bounding_area(points)

            if area > prev_area:
                return best_points, time - 1

            prev_area = area
            best_points = points
            time += 1


    def part1(self) -> str:
        self.print_points(self.run_simulation()[0])
        return "Read above."

    def part2(self) -> int:
        return self.run_simulation()[1]


if __name__ == '__main__':
    Solution().run()
