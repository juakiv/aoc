from itertools import combinations
from sympy import symbols, solve

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day24", 2023)

        self.hailstones = []
        for line in self.data:
            coordinates, velocities = line.split("@")
            self.hailstones.append((*map(int, coordinates.split(",")), *map(int, velocities.split(","))))

    def part1(self) -> int:
        total_collisions = 0
        low_bound = 200_000_000_000_000
        high_bound = 400_000_000_000_000

        for hail1, hail2 in combinations(self.hailstones, 2):
            x1, y1, _, vx1, vy1, _ = hail1
            x2, y2, _, vx2, vy2, _ = hail2

            slope1 = vy1 / vx1
            slope2 = vy2 / vx2

            if slope1 == slope2: # parallel, will never collide
                continue

            trajectory1 = y1 - slope1 * x1
            trajectory2 = y2 - slope2 * x2

            intersection_x = (trajectory2 - trajectory1) / (slope1 - slope2)
            intersection_y = slope1 * intersection_x + trajectory1

            if low_bound <= intersection_x <= high_bound and low_bound <= intersection_y <= high_bound and \
                    ((intersection_x > x1 and vx1 > 0) or (intersection_x < x1 and vx1 < 0)) and \
                    ((intersection_x > x2 and vx2 > 0) or (intersection_x < x2 and vx2 < 0)):
                total_collisions += 1

        return total_collisions

    def part2(self) -> int:
        x, y, z, vx, vy, vz = symbols("x y z vx vy vz")
        three_hails = self.hailstones[:3]

        equations = []
        for hail in three_hails:
            x0, y0, z0, vx0, vy0, vz0 = hail

            equations.append((y0 - y) * (vz0 - vz) - (z0 - z) * (vy0 - vy))
            equations.append((z0 - z) * (vx0 - vx) - (x0 - x) * (vz0 - vz))
            equations.append((x0 - x) * (vy0 - vy) - (y0 - y) * (vx0 - vx))

        solution = solve(equations, (x, y, z, vx, vy, vz), dict=True)[0]
        return solution[x] + solution[y] + solution[z]


if __name__ == '__main__':
    Solution().run()
