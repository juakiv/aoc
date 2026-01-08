from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data: list[list[str]] = self.load_data("day16", 2023)

    def solve_next_states(self, state: tuple[int, int, str]) -> list[tuple[int, int, str]]:
        direction_offsets = {
            "right": (1, 0),
            "down": (0, 1),
            "left": (-1, 0),
            "up": (0, -1),
        }
        x, y, direction = state
        dx, dy = direction_offsets[direction][0] + x , direction_offsets[direction][1] + y

        if 0 <= dy < len(self.data) and 0 <= dx < len(self.data[0]):
            next_tile = self.data[dy][dx]
            if next_tile == "." or (next_tile == "-" and direction in ["left", "right"]) or (next_tile == "|" and direction in ["up", "down"]):
                return [(dx, dy, direction)]
            elif next_tile == "|" and direction in ["left", "right"]:
                return [(dx, dy, "up"), (dx, dy, "down")]
            elif next_tile == "-" and direction in ["up", "down"]:
                return [(dx, dy, "left"), (dx, dy, "right")]
            elif next_tile == "/":
                if direction == "right":
                    return [(dx, dy, "up")]
                elif direction == "left":
                    return [(dx, dy, "down")]
                elif direction == "up":
                    return [(dx, dy, "right")]
                elif direction == "down":
                    return [(dx, dy, "left")]
            elif next_tile == "\\":
                if direction == "right":
                    return [(dx, dy, "down")]
                elif direction == "left":
                    return [(dx, dy, "up")]
                elif direction == "up":
                    return [(dx, dy, "left")]
                elif direction == "down":
                    return [(dx, dy, "right")]

        return []



    def energized_tiles(self, start: tuple[int, int, str]) -> set[tuple[int, int]]:
        seen: set = set()
        queue: list = [start]

        while queue:
            current = queue.pop(0)

            if current in seen:
                continue

            seen.add(current)

            for next_state in self.solve_next_states(current):
                queue.append(next_state)

        return set((x, y) for x, y, _ in seen)

    def part1(self) -> int:
        energized_tiles = self.energized_tiles((-1, 0, "right"))
        return len(energized_tiles) - 1

    def part2(self) -> int:
        max_energized_tiles = 0

        for y in range(len(self.data)):
            max_energized_tiles = max(
                max_energized_tiles,
                (len(self.energized_tiles((-1, y, "right"))) - 1),
                (len(self.energized_tiles((len(self.data[0]), y, "left"))) - 1)
            )

        for x in range(len(self.data[0])):
            max_energized_tiles = max(
                max_energized_tiles,
                (len(self.energized_tiles((x, -1, "down"))) - 1),
                (len(self.energized_tiles((x, len(self.data), "up"))) - 1)
            )

        return max_energized_tiles


if __name__ == '__main__':
    Solution().run()
