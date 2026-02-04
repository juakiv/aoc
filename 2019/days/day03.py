from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day03", 2019)

        self.wires: list[list[tuple[str, int]]] = []
        for line in self.data:
            wire = []
            for part in line.split(","):
                direction = part[0]
                length = int(part[1:])
                wire.append((direction, length))
            self.wires.append(wire)

    def solve_wires(self) -> dict[tuple[int, int], dict[int, int]]:
        taken_by_wires: dict[tuple[int, int], dict[int, int]] = defaultdict(lambda: defaultdict(int))
        for wire_index, wire in enumerate(self.wires):
            x, y = 0, 0
            steps = 0
            for direction, length in wire:
                for _ in range(length):
                    steps += 1
                    if direction == "R":
                        x += 1
                    elif direction == "L":
                        x -= 1
                    elif direction == "U":
                        y += 1
                    elif direction == "D":
                        y -= 1

                    if wire_index not in taken_by_wires[(x, y)]:
                        taken_by_wires[(x, y)][wire_index] = steps

        return taken_by_wires

    def part1(self) -> int:
        wires = self.solve_wires()
        return min(abs(x) + abs(y) for (x, y), wires in wires.items() if len(wires) > 1)

    def part2(self) -> int:
        wires = self.solve_wires()
        return min(sum(steps.values()) for steps in wires.values() if len(steps) > 1)


if __name__ == '__main__':
    Solution().run()
