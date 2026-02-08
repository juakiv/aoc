import math
import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day12", 2019)

        io, europa, ganymede, callisto = re.findall(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", "\n".join(self.data))
        self.moons: list[list[int]] = [[int(x), int(y), int(z)] for x, y, z in (io, europa, ganymede, callisto)]

    def part1(self) -> int:
        velocities = [[0, 0, 0] for _ in self.moons]
        positions = [moon.copy() for moon in self.moons]

        for _ in range(1000):

            # gravity
            for i in range(4):
                for j in range(i + 1, 4):
                    for axis in range(3):
                        if positions[i][axis] < positions[j][axis]:
                            velocities[i][axis] += 1
                            velocities[j][axis] -= 1
                        elif positions[i][axis] > positions[j][axis]:
                            velocities[i][axis] -= 1
                            velocities[j][axis] += 1

            # velocity
            for i in range(4):
                for axis in range(3):
                    positions[i][axis] += velocities[i][axis]

        total_energy = 0
        for i in range(4):
            potential = sum(abs(v) for v in positions[i])
            kinetic = sum(abs(v) for v in velocities[i])
            total_energy += potential * kinetic

        return total_energy

    def part2(self) -> int:
        cycles = []

        for axis in range(3):
            positions = [moon[axis] for moon in self.moons]
            velocities = [0] * 4

            initial_positions = positions[:]
            initial_velocities = velocities[:]

            steps = 0
            while True:

                # gravity
                for i in range(4):
                    for j in range(i + 1, 4):
                        if positions[i] < positions[j]:
                            velocities[i] += 1
                            velocities[j] -= 1
                        elif positions[i] > positions[j]:
                            velocities[i] -= 1
                            velocities[j] += 1

                # velocity
                for i in range(4):
                    positions[i] += velocities[i]

                steps += 1

                if positions == initial_positions and velocities == initial_velocities:
                    cycles.append(steps)
                    break

        return math.lcm(cycles[0], cycles[1], cycles[2])


if __name__ == '__main__':
    Solution().run()
