from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day17", 2018)

        self.clay: set[tuple[int, int]] = set()
        for line in self.data:
            parts = line.split(", ")
            if parts[0][0] == "x":
                x = int(parts[0][2:])
                y1, y2 = map(int, parts[1][2:].split(".."))
                for y in range(y1, y2 + 1):
                    self.clay.add((x, y))
            else:
                y = int(parts[0][2:])
                x1, x2 = map(int, parts[1][2:].split(".."))
                for x in range(x1, x2 + 1):
                    self.clay.add((x, y))

        self.min_y = min(y for _, y in self.clay)
        self.max_y = max(y for _, y in self.clay)

    def simulate(self) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
        flowing = set()
        settled = set()
        visited_sources = set()

        stack = [(500, 0)]

        while stack:
            x, y = stack.pop()

            if (x, y) in visited_sources:
                continue

            visited_sources.add((x, y))

            while y <= self.max_y and (x, y) not in self.clay and (x, y) not in settled:
                flowing.add((x, y))
                y += 1

            if y > self.max_y:
                continue

            y -= 1

            while True:
                left = x
                right = x
                blocked_left = True
                blocked_right = True

                while True:
                    below = (left, y + 1)
                    if below not in self.clay and below not in settled:
                        blocked_left = False
                        break
                    if (left - 1, y) in self.clay:
                        break
                    left -= 1

                while True:
                    below = (right, y + 1)
                    if below not in self.clay and below not in settled:
                        blocked_right = False
                        break
                    if (right + 1, y) in self.clay:
                        break
                    right += 1

                if blocked_left and blocked_right:
                    for x2 in range(left, right + 1):
                        settled.add((x2, y))

                    y -= 1
                    if y < self.min_y:
                        break

                else:
                    for x2 in range(left, right + 1):
                        flowing.add((x2, y))

                    if not blocked_left:
                        stack.append((left, y))

                    if not blocked_right:
                        stack.append((right, y))

                    break

        return flowing, settled

    def part1(self) -> int:
        flowing, settled = self.simulate()
        return len({(x, y) for (x, y) in flowing | settled if self.min_y <= y <= self.max_y})

    def part2(self) -> int:
        _, settled = self.simulate()
        return len({(x, y) for (x, y) in settled if self.min_y <= y <= self.max_y})


if __name__ == '__main__':
    Solution().run()
