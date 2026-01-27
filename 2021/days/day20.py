from copy import deepcopy

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day20", 2021, "\n\n")

        self.algorithm: list[str] = list(self.data[0])
        self.image: list[list[str]] = [list(line) for line in self.data[1].split("\n")]

        self.bg_pixel = "."

    def enhance(self, pixels: set[tuple[int, int]]) -> set[tuple[int, int]]:
        new_pixels = set()

        min_x = min(x for x, y in pixels)
        max_x = max(x for x, y in pixels)
        min_y = min(y for x, y in pixels)
        max_y = max(y for x, y in pixels)

        new_bg = self.algorithm[0] if self.bg_pixel == "." else self.algorithm[511]

        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                index = 0

                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        index <<= 1
                        new_x, new_y = x + dx, y + dy

                        bit = (new_x, new_y) in pixels
                        if self.bg_pixel == "#":
                            bit = not bit

                        if bit:
                            index |= 1

                if self.algorithm[index] != new_bg:
                    new_pixels.add((x, y))

        self.bg_pixel = new_bg

        return new_pixels

    def part1(self) -> int:
        lit_pixels = set()
        for y, row in enumerate(self.image):
            for x, pixel in enumerate(row):
                if pixel == "#":
                    lit_pixels.add((x, y))

        for _ in range(2):
            lit_pixels = self.enhance(lit_pixels)

        return len(lit_pixels)

    def part2(self) -> int:
        lit_pixels = set()
        for y, row in enumerate(self.image):
            for x, pixel in enumerate(row):
                if pixel == "#":
                    lit_pixels.add((x, y))

        for _ in range(50):
            lit_pixels = self.enhance(lit_pixels)

        return len(lit_pixels)


if __name__ == '__main__':
    Solution().run()
