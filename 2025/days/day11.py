from collections import defaultdict
from functools import cache

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day11", 2025)

        self.servers = defaultdict(list)
        for line in self.data:
            server, connections = line.split(": ")
            self.servers[server] = connections.split(" ")

    @cache
    def paths(self, source: str, destination: str):
        return ((destination in self.servers[source])
                + sum(self.paths(next_server, destination) for next_server in self.servers[source]))

    def part1(self) -> int:
        return self.paths("you", "out")

    def part2(self) -> int:
        return (self.paths("svr", "dac") * self.paths("dac", "fft") * self.paths("fft", "out")
                + self.paths("svr", "fft") * self.paths("fft", "dac") * self.paths("dac", "out"))



if __name__ == '__main__':
    Solution().run()
