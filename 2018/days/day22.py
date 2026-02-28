from heapq import heappop, heappush

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day22", 2018)

        self.depth = int(self.data[0].split(": ")[1])
        coords = self.data[1].split(": ")[1].split(",")
        self.target = (int(coords[0]), int(coords[1]))

    def erosion_map(self, max_x, max_y):
        grid = [[0] * (max_x + 1) for _ in range(max_y + 1)]
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if (x == 0 and y == 0) or (x == self.target[0] and y == self.target[1]):
                    geo = 0
                elif y == 0:
                    geo = x * 16807
                elif x == 0:
                    geo = y * 48271
                else:
                    geo = grid[y - 1][x] * grid[y][x - 1]
                grid[y][x] = (geo + self.depth) % 20183
        return [[(e % 3) for e in row] for row in grid]

    def part1(self) -> int:
        target_x, target_y = self.target
        risk_map = self.erosion_map(target_x, target_y)
        return sum(sum(row) for row in risk_map)

    def part2(self) -> int:
        no_tool = 0
        torch = 1
        gear = 2

        tools = { 0: [torch, gear], 1: [gear, no_tool], 2: [torch, no_tool] }

        target_x, target_y = self.target
        max_x, max_y = target_x + 100, target_y + 100
        risk_map = self.erosion_map(max_x, max_y)

        queue = [(0, 0, 0, torch)]
        visited = {}

        while queue:
            minutes, x, y, tool = heappop(queue)

            state = (x, y, tool)
            if visited.get(state, float("inf")) <= minutes:
                continue

            visited[state] = minutes

            if x == target_x and y == target_y:
                if tool == torch:
                    return minutes
                else:
                    heappush(queue, (minutes + 7, x, y, torch))
                    continue

            for next_tool in tools[risk_map[y][x]]:
                if next_tool != tool:
                    heappush(queue, (minutes + 7, x, y, next_tool))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x <= max_x and 0 <= new_y <= max_y:
                    if tool in tools[risk_map[new_y][new_x]]:
                        heappush(queue, (minutes + 1, new_x, new_y, tool))

        return -1


if __name__ == '__main__':
    Solution().run()
