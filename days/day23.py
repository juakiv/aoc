from itertools import combinations

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day23")

        self.connections = set()
        self.computers = set()
        for line in self.data:
            connection = line.split("-")
            self.connections.add((connection[0], connection[1]))
            self.connections.add((connection[1], connection[0]))
            self.computers.add(connection[0])
            self.computers.add(connection[1])

    def part1(self) -> int:
        connections_of_three = set()
        for conn1, conn2, conn3 in combinations(self.computers, 3):
            if not (conn1.startswith("t") or conn2.startswith("t") or conn3.startswith("t")):
                continue

            if (conn1, conn2) not in self.connections or (conn2, conn3) not in self.connections or (conn1, conn3) not in self.connections:
                continue

            connections_of_three.add((conn1, conn2, conn3))

        return len(connections_of_three)

    def part2(self) -> str:
        groups = []

        for computer in self.computers:
            ok = False
            for group in groups:
                if all((computer, computer_group) in self.connections for computer_group in group):
                    group.add(computer)
                    ok = True

            if not ok:
                group = set()
                group.add(computer)
                groups.append(group)

        last_group = groups.pop()
        for group in groups:
            if len(group) > len(last_group):
                last_group = group

        return ",".join(sorted(last_group))


if __name__ == '__main__':
    Solution().run()
