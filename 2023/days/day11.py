from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day11", 2023)

        self.empty_rows = set(range(len(self.data)))
        self.empty_cols = set(range(len(self.data[0])))
        self.galaxy_positions = set()

        for i, row in enumerate(self.data):
            for j, cell in enumerate(row):
                if cell == '#':
                    self.galaxy_positions.add((i, j))
                    if i in self.empty_rows:
                        self.empty_rows.remove(i)
                    if j in self.empty_cols:
                        self.empty_cols.remove(j)

    def calculate_distances(self, size_factor: int) -> int:
        distances_between_galaxies = {}

        for galaxy1_x, galaxy1_y in self.galaxy_positions:
            for galaxy2_x, galaxy2_y in self.galaxy_positions:
                if (galaxy1_x, galaxy1_y) != (galaxy2_x, galaxy2_y) and \
                        ((galaxy2_x, galaxy2_y), (galaxy1_x, galaxy1_y)) not in distances_between_galaxies:
                    distance = abs(galaxy1_x - galaxy2_x) + abs(galaxy1_y - galaxy2_y)

                    empty_rows_between = [row for row in range(*sorted([galaxy1_x, galaxy2_x])) if
                                          row in self.empty_rows]
                    empty_cols_between = [col for col in range(*sorted([galaxy1_y, galaxy2_y])) if
                                          col in self.empty_cols]

                    distances_between_galaxies[((galaxy1_x, galaxy1_y), (galaxy2_x, galaxy2_y))] = distance + size_factor * (
                            len(empty_rows_between) + len(empty_cols_between))

        return sum(distances_between_galaxies.values())

    def part1(self) -> int:
        return self.calculate_distances(1)

    def part2(self) -> int:
        return self.calculate_distances(999_999)


if __name__ == '__main__':
    Solution().run()
