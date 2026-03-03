from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day25", 2018)

        self.points: list[list[int]] = []
        for line in self.data:
            self.points.append(list(map(int, line.split(","))))

        self.parent = list(range(len(self.points)))

    @staticmethod
    def manhattan_distance(p1: list[int], p2: list[int]) -> int:
        return sum(abs(a - b) for a, b in zip(p1, p2))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

    def part1(self) -> int:
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                if self.manhattan_distance(self.points[i], self.points[j]) <= 3:
                    self.union(i, j)

        constellations = set()
        for i in range(len(self.points)):
            constellations.add(self.find(i))

        return len(constellations)

    def part2(self) -> str:
        return ":)"


if __name__ == '__main__':
    Solution().run()
