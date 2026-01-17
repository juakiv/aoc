from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day14", 2022)

        self.stones: set[tuple[int, int]] = set()
        for line in self.data:
            points = [tuple(map(int, point.split(","))) for point in line.split(" -> ")]
            for i in range(len(points) - 1):
                x1, y1 = points[i]
                x2, y2 = points[i + 1]

                if x1 == x2:
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        self.stones.add((x1, y))
                elif y1 == y2:
                    for x in range(min(x1, x2), max(x1, x2) + 1):
                        self.stones.add((x, y1))

    def simulate_sand(self, part2: bool = False) -> int:
        sand = set()
        source = (500, 0)
        count = 0
        abyss_level = max(y for _, y in self.stones)

        while True:
            x, y = source

            if part2 and source in sand:
                return count

            while True:
                if part2 and y + 1 == abyss_level + 2:
                    sand.add((x, y))
                    count += 1
                    break

                if not part2 and y > abyss_level:
                    return count

                if (x, y + 1) not in self.stones and (x, y + 1) not in sand:
                    y += 1
                elif (x - 1, y + 1) not in self.stones and (x - 1, y + 1) not in sand:
                    x -= 1
                    y += 1
                elif (x + 1, y + 1) not in self.stones and (x + 1, y + 1) not in sand:
                    x += 1
                    y += 1
                else:
                    sand.add((x, y))
                    count += 1
                    break

    def part1(self) -> int:
        return self.simulate_sand()


    def part2(self) -> int:
        return self.simulate_sand(True)


if __name__ == '__main__':
    Solution().run()
