from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day18", 2018)

        self.map: dict[tuple[int, int], str] = {}
        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                self.map[(x, y)] = char

    @staticmethod
    def get_adjacent_tiles(x: int, y: int, map_: dict[tuple[int, int], str]) -> list[str]:
        adjacent_tiles: list[str] = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                adjacent_tiles.append(map_.get((x + dx, y + dy)))

        return adjacent_tiles

    def simulate(self, map_: dict[tuple[int, int], str]) -> dict[tuple[int, int], str]:
        new_map = map_.copy()

        for (x, y), tile in map_.items():
            adjacent_tiles = self.get_adjacent_tiles(x, y, map_)

            if tile == "." and adjacent_tiles.count("|") >= 3:
                new_map[(x, y)] = "|"
            elif tile == "|" and adjacent_tiles.count("#") >= 3:
                new_map[(x, y)] = "#"
            elif tile == "#" and not (adjacent_tiles.count("#") >= 1 and adjacent_tiles.count("|") >= 1):
                new_map[(x, y)] = "."

        return new_map

    def part1(self) -> int:
        map_ = self.map

        for _ in range(10):
            map_ = self.simulate(map_)

        return sum(1 for tile in map_.values() if tile == "|") * sum(1 for tile in map_.values() if tile == "#")

    def part2(self) -> int:
        map_ = self.map
        seen = {}

        for minute in range(1_000_000_000):
            map_ = self.simulate(map_)
            map_tuple = tuple(sorted(map_.items()))

            if map_tuple in seen:
                cycle_start = seen[map_tuple]
                cycle_length = minute - cycle_start

                remaining_minutes = (1_000_000_000 - minute - 1) % cycle_length
                for _ in range(remaining_minutes):
                    map_ = self.simulate(map_)
                break

            seen[map_tuple] = minute

        return sum(1 for tile in map_.values() if tile == "|") * sum(1 for tile in map_.values() if tile == "#")


if __name__ == '__main__':
    Solution().run()
