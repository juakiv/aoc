from functools import lru_cache

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day16", 2022)

        self.valves = {}
        for line in self.data:
            parts = line.split("; ")
            valve_info = parts[0].split(" has flow rate=")
            valve_name = valve_info[0].split("Valve ")[1]
            flow_rate = int(valve_info[1])
            leads_to = parts[1].replace("tunnels lead to valves ", "").replace("tunnel leads to valve ", "").split(", ")
            self.valves[valve_name] = {
                "flow_rate": flow_rate,
                "leads_to": leads_to
            }

        self.distances = {}
        for valve in self.valves:
            self.distances[valve] = self.bfs(valve)

        self.useful_valves = {v for v in self.valves if self.valves[v]["flow_rate"] > 0}

    def bfs(self, start: str) -> dict:
        queue = [(start, 0)]
        visited = {start: 0}
        while queue:
            current, distance = queue.pop(0)
            for neighbor in self.valves[current]["leads_to"]:
                if neighbor not in visited:
                    visited[neighbor] = distance + 1
                    queue.append((neighbor, distance + 1))
        return visited

    def dfs(self, start: str, time_left: int, mask: int, pressure: int, bests: dict) -> None:
        bests[mask] = max(bests.get(mask, 0), pressure)

        for valve in self.useful_valves:
            bit = 1 << list(self.useful_valves).index(valve)
            if mask & bit:
                continue

            distance = self.distances[start][valve]
            time = time_left - distance - 1
            if time <= 0:
                continue

            self.dfs(
                valve,
                time,
                mask | bit,
                pressure + self.valves[valve]["flow_rate"] * time,
                bests
            )

    def part1(self) -> int:
        bests = {}
        self.dfs("AA", 30, 0, 0, bests)
        return max(bests.values())

    def part2(self) -> int:
        best = {}
        self.dfs("AA", 26, 0, 0, best)

        most_pressure = 0
        items = list(best.items())

        for m1, v1 in items:
            for m2, v2 in items:
                if m1 & m2 == 0:
                    most_pressure = max(most_pressure, v1 + v2)

        return most_pressure


if __name__ == '__main__':
    Solution().run()
