from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day19", 2021, "\n\n")

        self.scanners = []
        for scanner in self.data:
            beacons = []
            for line in scanner.split("\n")[1:]:
                beacons.append(tuple(map(int, line.split(","))))
            self.scanners.append(beacons)

        self.scanner_positions = [(0, 0, 0)]

    @staticmethod
    def get_rotations(point: tuple[int, int, int]) -> list[tuple[int, int, int]]:
        x, y, z = point
        return [
            ( x,  y,  z), ( x, -y, -z), ( x,  z, -y), ( x, -z,  y),
            (-x,  y, -z), (-x, -y,  z), (-x,  z,  y), (-x, -z, -y),
            ( y,  x, -z), ( y, -x,  z), ( y,  z,  x), ( y, -z, -x),
            (-y,  x,  z), (-y, -x, -z), (-y,  z, -x), (-y, -z,  x),
            ( z,  x,  y), ( z, -x, -y), ( z,  y, -x), ( z, -y,  x),
            (-z,  x, -y), (-z, -x,  y), (-z,  y,  x), (-z, -y, -x),
        ]

    def align(self, known, unknown) -> tuple[list[tuple[int, int, int]] | None, tuple[int, int, int] | None]:
        for i in range(24):
            rotated = [self.get_rotations(point)[i] for point in unknown]
            offsets = defaultdict(int)

            for known_x, known_y, known_z in known:
                for rotated_x, rotated_y, rotated_z in rotated:
                    offset = (known_x - rotated_x, known_y - rotated_y, known_z - rotated_z)
                    offsets[offset] += 1

                    if offsets[offset] >= 12:
                        aligned = [(ux + offset[0], uy + offset[1], uz + offset[2]) for ux, uy, uz in rotated]
                        return aligned, offset

        return None, None

    def part1(self) -> int:
        resolved_scanners = set(self.scanners[0])
        unresolved_scanners = self.scanners[1:]

        while unresolved_scanners:
            for i in range(len(unresolved_scanners)-1, -1, -1):
                aligned, position = self.align(resolved_scanners, unresolved_scanners[i])

                if aligned:
                    resolved_scanners.update(aligned)
                    unresolved_scanners.pop(i)
                    self.scanner_positions.append(position) # for part 2
                    break

        return len(resolved_scanners)

    def part2(self) -> int:
        max_distance = 0

        for i in range(len(self.scanner_positions)):
            for j in range(i + 1, len(self.scanner_positions)):
                x1, y1, z1 = self.scanner_positions[i]
                x2, y2, z2 = self.scanner_positions[j]
                distance = abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
                if distance > max_distance:
                    max_distance = distance

        return max_distance


if __name__ == '__main__':
    Solution().run()
