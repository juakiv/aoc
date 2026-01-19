from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day17", 2022)[0]

        self.jets = list(self.data.strip())
        self.rock_shapes = [
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            [(0, 0), (1, 0), (0, 1), (1, 1)]
        ]

    def simulate_rocks(self, num_rocks: int) -> int:
        tunnel = set()
        col_heights = [0] * 7

        highest_y = -1
        jet_index = 0
        added_height = 0

        seen = {}

        rock_index = 0
        while rock_index < num_rocks:
            shape = self.rock_shapes[rock_index % 5]
            rock_x = 2
            rock_y = highest_y + 4

            while True:
                jet = self.jets[jet_index % len(self.jets)]
                jet_index += 1

                dx = 1 if jet == '>' else -1
                if all(0 <= rock_x + dx + sx < 7 and (rock_x + dx + sx, rock_y + sy) not in tunnel for sx, sy in shape):
                    rock_x += dx

                if all(rock_y + sy - 1 >= 0 and (rock_x + sx, rock_y + sy - 1) not in tunnel for sx, sy in shape):
                    rock_y -= 1
                else:
                    for sx, sy in shape:
                        x = rock_x + sx
                        y = rock_y + sy
                        tunnel.add((x, y))
                        col_heights[x] = max(col_heights[x], y + 1)
                        highest_y = max(highest_y, y)
                    break

            # detect cycles
            top = max(col_heights)
            profile = tuple(top - h for h in col_heights)
            state = (rock_index % 5, jet_index % len(self.jets), profile)

            if state in seen:
                prev_rock, prev_height = seen[state]
                cycle_len = rock_index - prev_rock
                cycle_height = highest_y - prev_height

                remaining = num_rocks - rock_index - 1
                cycles = remaining // cycle_len

                if cycles > 0:
                    rock_index += cycles * cycle_len
                    added_height += cycles * cycle_height
            else:
                seen[state] = (rock_index, highest_y)

            rock_index += 1

        return highest_y + added_height + 1

    def part1(self) -> int:
        return self.simulate_rocks(2022)

    def part2(self) -> int:
        return self.simulate_rocks(1_000_000_000_000)


if __name__ == '__main__':
    Solution().run()
