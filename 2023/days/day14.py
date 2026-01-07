from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day14", 2023)

        self.platform: list[list[str]] = [list(line) for line in self.data]

    @staticmethod
    def roll_rocks(platform: list[list[str]]) -> list[list[str]]:
        for y, row in enumerate(platform):
            for x, char in enumerate(row):
                if char == "O":
                    platform[y][x] = "."

                    roll_up_row = y - 1
                    while roll_up_row >= 0 and platform[roll_up_row][x] == ".":
                        roll_up_row -= 1

                    platform[roll_up_row + 1][x] = "O"

        return platform

    def cycle_platform(self, platform: list[list[str]]) -> list[list[str]]:
        for _ in range(4):
            platform = self.roll_rocks(platform)
            platform = [list(reversed(col)) for col in zip(*platform)]

        return platform

    def part1(self) -> int:
        platform = self.roll_rocks(self.platform.copy())
        return sum(row.count("O") * (len(platform) - row_num) for row_num, row in enumerate(platform))

    def part2(self) -> int:
        platform = self.platform.copy()
        seen_platforms_list = [tuple(tuple(row) for row in platform)]

        for i in range(1_000_000_000):
            platform = self.cycle_platform(platform)

            if tuple(tuple(row) for row in platform) in seen_platforms_list:
                first_seen_index = seen_platforms_list.index(tuple(tuple(row) for row in platform))
                cycle_length = i + 1 - first_seen_index
                platform = seen_platforms_list[(1_000_000_000 - first_seen_index) % cycle_length + first_seen_index]

                break

            seen_platforms_list.append(tuple(tuple(row) for row in platform))

        return sum(row.count("O") * (len(platform) - row_num) for row_num, row in enumerate(platform))


if __name__ == '__main__':
    Solution().run()
