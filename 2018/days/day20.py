from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day20", 2018)

    def distances(self):
        regex = self.data[0].strip()

        graph = defaultdict(set)
        current_positions = {(0, 0)}
        stack = []

        directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0) }

        for char in regex:
            if char in directions:
                dx, dy = directions[char]
                new_positions = set()
                for x, y in current_positions:
                    new_x, new_y = x + dx, y + dy
                    graph[(x, y)].add((new_x, new_y))
                    graph[(new_x, new_y)].add((x, y))
                    new_positions.add((new_x, new_y))

                current_positions = new_positions

            elif char == "(":
                stack.append((set(current_positions), []))

            elif char == "|":
                start_positions, branch_positions = stack[-1]
                branch_positions.extend(current_positions)
                current_positions = set(start_positions)

            elif char == ")":
                start_positions, branch_positions = stack.pop()
                branch_positions.extend(current_positions)
                current_positions = set(branch_positions)

        queue = [(0, 0)]
        distances = {(0, 0): 0}

        while queue:
            x, y = queue.pop()
            for new_x, new_y in graph[(x, y)]:
                if (new_x, new_y) not in distances:
                    distances[(new_x, new_y)] = distances[(x, y)] + 1
                    queue.append((new_x, new_y))

        return distances

    def part1(self) -> int:
        return max(self.distances().values())

    def part2(self) -> int:
        return sum(1 for d in self.distances().values() if d >= 1000)


if __name__ == '__main__':
    Solution().run()
