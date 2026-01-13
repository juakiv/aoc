import random
from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day25", 2023)

        self.nodes = set()
        self.edges = []
        for line in self.data:
            left, right = line.split(":")
            a = left.strip()

            for b in right.split():
                self.edges.append((a, b))
                self.nodes.add(a)
                self.nodes.add(b)

    @staticmethod
    def karger(nodes, edges):
        parent = { node: node for node in nodes }
        size = { node: 1 for node in nodes }

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        remaining = len(nodes)
        while remaining > 2:
            node1, node2 = random.choice(edges)

            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                continue

            parent[root1] = root2
            size[root1] += size[root2]
            remaining -= 1

        cut_edges = 0
        for node1, node2 in edges:
            if find(node1) != find(node2):
                cut_edges += 1

        groups = defaultdict(int)
        for node in nodes:
            groups[find(node)] += 1

        return cut_edges, list(groups.values())

    def part1(self) -> int:
        group_sizes = -1
        for _ in range(500): # try until we find a cut of size 3
            cut_size, groups = self.karger(list(self.nodes), list(self.edges))
            if cut_size == 3:
                group_sizes = groups[0] * groups[1]
                break

        return group_sizes

    def part2(self) -> str:
        return ":)"


if __name__ == '__main__':
    Solution().run()
