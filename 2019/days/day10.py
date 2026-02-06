import math

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day10", 2019)

        self.asteroids: set[tuple[int, int]] = set()
        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                if char == "#":
                    self.asteroids.add((x, y))

        self.best_x, self.best_y = 0, 0

    def count_visible(self, x: int, y: int) -> int:
        visible = set()

        for ax, ay in self.asteroids:
            if (ax, ay) == (x, y):
                continue

            dx = ax - x
            dy = ay - y

            gcd = math.gcd(dx, dy)
            visible.add((dx // gcd, dy // gcd))

        return len(visible)

    def part1(self) -> int:
        max_count = 0

        for x, y in self.asteroids:
            count = self.count_visible(x, y)
            if count > max_count:
                max_count = count
                self.best_x, self.best_y = x, y

        return max_count

    def part2(self) -> int:
        angles = []

        for asteroid_x, asteroid_y in self.asteroids:
            if (asteroid_x, asteroid_y) == (self.best_x, self.best_y):
                continue # dont vaporize self :)

            dx = asteroid_x - self.best_x
            dy = asteroid_y - self.best_y

            angle = math.atan2(dx, -dy)
            if angle < 0:
                angle += 2 * math.pi

            distance = math.sqrt(dx * dx + dy * dy)
            angles.append((angle, distance, asteroid_x, asteroid_y))

        count = 0
        last_angle = None
        for angle, distance, asteroid_x, asteroid_y in sorted(angles):
            if angle != last_angle:
                count += 1
                last_angle = angle

            if count == 200:
                return asteroid_x * 100 + asteroid_y

        return 0


if __name__ == '__main__':
    Solution().run()
