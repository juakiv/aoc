from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07_test", 2025)

    def part1(self) -> int:
        beam_splits_count = 0
        beams: set[int] = { self.data[0].index("S") }

        for line in self.data[1:]:
            next_beams: set[int] = set()

            for beam in beams:
                if line[beam] == "^":
                    beam_splits_count += 1
                    next_beams.add(beam - 1)
                    next_beams.add(beam + 1)
                else:
                    next_beams.add(beam)
            beams = next_beams

        return beam_splits_count

    def part2(self) -> int:
        beams: dict[tuple[int, int], int] = defaultdict(int)
        beams[(self.data[0].index("S"), 0)] = 1

        for line in self.data[1:]:
            next_beams: dict[tuple[int, int], int] = defaultdict(int)

            for beam in beams:
                x, y = beam
                count = beams[beam]

                if line[x] == "^":
                    next_beams[(x - 1, y + 1)] += count
                    next_beams[(x + 1, y + 1)] += count
                else:
                    next_beams[(x, y + 1)] += count
            beams = next_beams

        return sum(beams.values())


if __name__ == '__main__':
    Solution().run()
