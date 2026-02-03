from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day24", 2020)
        self.directions = { "e": (1, 0), "w": (-1, 0), "ne": (0, 1), "nw": (-1, 1), "se": (1, -1), "sw": (0, -1) }

    def flip_tiles(self, instruction: str, black_tiles: set[tuple[int, int]]) -> set[tuple[int, int]]:
        x, y = 0, 0
        i = 0

        while i < len(instruction):
            if instruction[i] in ("e", "w"):
                direction = instruction[i]
                i += 1
            else:
                direction = instruction[i:i+2]
                i += 2

            dx, dy = self.directions[direction]
            x += dx
            y += dy

        if (x, y) in black_tiles:
            black_tiles.remove((x, y))
        else:
            black_tiles.add((x, y))

        return black_tiles

    def part1(self) -> int:
        black_tiles = set()

        for instruction in self.data:
            black_tiles = self.flip_tiles(instruction, black_tiles)

        return len(black_tiles)

    def part2(self) -> int:
        black_tiles = set()

        for instruction in self.data:
            black_tiles = self.flip_tiles(instruction, black_tiles)

        for _ in range(100):
            new_black_tiles = set()
            white_tile_neighbors = {}

            for x, y in black_tiles:
                black_neighbor_count = 0

                for dx, dy in self.directions.values():
                    neighbor = (x + dx, y + dy)

                    if neighbor in black_tiles:
                        black_neighbor_count += 1
                    else:
                        if neighbor not in white_tile_neighbors:
                            white_tile_neighbors[neighbor] = 0

                        white_tile_neighbors[neighbor] += 1

                if black_neighbor_count == 1 or black_neighbor_count == 2:
                    new_black_tiles.add((x, y))

            for tile, count in white_tile_neighbors.items():
                if count == 2:
                    new_black_tiles.add(tile)

            black_tiles = new_black_tiles

        return len(black_tiles)


if __name__ == '__main__':
    Solution().run()
