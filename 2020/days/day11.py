from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day11", 2020)

        self.map: list[list[str]] = [list(line) for line in self.data]

    @staticmethod
    def simulate_seating(map_: list[list[str]], part2: bool = False) -> tuple[list[list[str]], bool]:
        rows = len(map_)
        cols = len(map_[0])
        new_map = [row.copy() for row in map_]

        for row in range(rows):
            for col in range(cols):
                seat = map_[row][col]
                if seat == ".":
                    continue

                occupied_count = 0
                for d_row, d_col in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    new_row, new_col = row + d_row, col + d_col
                    if part2:
                        while 0 <= new_row < rows and 0 <= new_col < cols:
                            if map_[new_row][new_col] == "#":
                                occupied_count += 1
                                break
                            elif map_[new_row][new_col] == "L":
                                break
                            new_row += d_row
                            new_col += d_col
                    else:
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            if map_[new_row][new_col] == "#":
                                occupied_count += 1

                minimum_occupied = 5 if part2 else 4
                if seat == "L" and occupied_count == 0:
                    new_map[row][col] = "#"
                elif seat == "#" and occupied_count >= minimum_occupied:
                    new_map[row][col] = "L"

        has_changed = new_map != map_

        return new_map, has_changed

    def part1(self) -> int:
        map_ = [row.copy() for row in self.map]

        while True:
            map_, changed = self.simulate_seating(map_)

            if not changed:
                break

        return sum(seat == "#" for row in map_ for seat in row)

    def part2(self) -> int:
        map_ = [row.copy() for row in self.map]

        while True:
            map_, changed = self.simulate_seating(map_, True)

            if not changed:
                break

        return sum(seat == "#" for row in map_ for seat in row)


if __name__ == '__main__':
    Solution().run()
