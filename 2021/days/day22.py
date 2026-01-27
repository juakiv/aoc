from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day22", 2021)

        self.steps = []
        for line in self.data:
            action, coords = line.split(" ")
            x_range, y_range, z_range = coords.split(",")
            x_min, x_max = map(int, x_range[2:].split(".."))
            y_min, y_max = map(int, y_range[2:].split(".."))
            z_min, z_max = map(int, z_range[2:].split(".."))
            self.steps.append((action, (x_min, x_max), (y_min, y_max), (z_min, z_max)))

    def part1(self) -> int:
        reactor = set()

        for step in self.steps:
            action, x_range, y_range, z_range = step

            for x in range(max(x_range[0], -50), min(x_range[1], 50) + 1):
                for y in range(max(y_range[0], -50), min(y_range[1], 50) + 1):
                    for z in range(max(z_range[0], -50), min(z_range[1], 50) + 1):
                        if action == "on":
                            reactor.add((x, y, z))
                        else:
                            reactor.discard((x, y, z))

        return len(reactor)

    @staticmethod
    def cuboid_intersection(cuboid1: tuple[tuple[int, int], tuple[int, int], tuple[int, int]], cuboid2: tuple[tuple[int, int], tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]] | None:
        x1_min, x1_max = cuboid1[0]
        y1_min, y1_max = cuboid1[1]
        z1_min, z1_max = cuboid1[2]

        x2_min, x2_max = cuboid2[0]
        y2_min, y2_max = cuboid2[1]
        z2_min, z2_max = cuboid2[2]

        x_min = max(x1_min, x2_min)
        x_max = min(x1_max, x2_max)
        y_min = max(y1_min, y2_min)
        y_max = min(y1_max, y2_max)
        z_min = max(z1_min, z2_min)
        z_max = min(z1_max, z2_max)

        if x_min <= x_max and y_min <= y_max and z_min <= z_max:
            return (x_min, x_max), (y_min, y_max), (z_min, z_max)
        else:
            return None


    @staticmethod
    def volume(x_range: tuple[int, int], y_range: tuple[int, int], z_range: tuple[int, int]) -> int:
        return (x_range[1] - x_range[0] + 1) * (y_range[1] - y_range[0] + 1) * (z_range[1] - z_range[0] + 1)

    def part2(self) -> int:
        cuboids = []

        for step in self.steps:
            action, x_range, y_range, z_range = step
            new_cuboid = (x_range, y_range, z_range)
            updates = []

            for existing_cuboid, sign in cuboids:
                intersection = self.cuboid_intersection(existing_cuboid, new_cuboid)
                if intersection:
                    updates.append((intersection, -sign))

            if action == "on":
                updates.append((new_cuboid, 1))

            cuboids.extend(updates)

        total_volume = 0
        for cuboid, sign in cuboids:
            total_volume += sign * self.volume(cuboid[0], cuboid[1], cuboid[2])

        return total_volume


if __name__ == '__main__':
    Solution().run()
