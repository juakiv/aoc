from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07", 2022)

        self.sizes = defaultdict(int)

        path = []
        for command in self.data:
            if command == "$ ls":
                continue

            if command.startswith("$ cd"):
                dir_name = command.split(" ")[-1]
                if dir_name == "..":
                    path.pop()
                else:
                    path.append(dir_name)

            else:
                size, name = command.split(" ")
                if size.isdigit():
                    for i in range(len(path)):
                        dir_path = "/".join(path[:i + 1])
                        self.sizes[dir_path] += int(size)

    def part1(self) -> int:
        return sum(size for size in self.sizes.values() if size <= 100_000)

    def part2(self) -> int:
        total_space = 70_000_000
        needed_space = 30_000_000

        space_to_free = needed_space - (total_space - self.sizes["/"])

        candidates = [size for size in self.sizes.values() if size >= space_to_free]
        if candidates:
            return min(candidates)

        return 0


if __name__ == '__main__':
    Solution().run()
