from collections import deque
from heapq import heappush, heappop

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day18", 2019)

        self.map: dict[tuple[int, int], str] = {}
        self.keys: dict[str, tuple[int, int]] = {}
        self.doors: dict[str, tuple[int, int]] = {}
        self.start: tuple[int, int] = (0, 0)

        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                self.map[(x, y)] = char
                if char == "@":
                    self.start = (x, y)
                elif char.islower():
                    self.keys[char] = (x, y)
                elif char.isupper():
                    self.doors[char] = (x, y)

    @staticmethod
    def get_reachable_targets(start_pos: tuple[int, int], grid: dict[tuple[int, int], str]) -> dict[str, tuple[int, frozenset[str]]]:
        targets = {}
        queue = deque([(start_pos, 0, frozenset())])
        visited = { start_pos }

        while queue:
            (current_x, current_y), distance, doors = queue.popleft()

            character = grid.get((current_x, current_y), "#")
            if character != "#" and (current_x, current_y) != start_pos:
                if character.islower():
                    targets[character] = (distance, doors)

                elif character.isupper():
                    doors = doors | frozenset([character.lower()])

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = current_x + dx, current_y + dy
                if (nx, ny) in grid and grid[(nx, ny)] != '#' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), distance + 1, doors))

        return targets

    def part1(self) -> int:
        graph = {"@": self.get_reachable_targets(self.start, self.map)}
        for key, pos in self.keys.items():
            graph[key] = self.get_reachable_targets(pos, self.map)

        queue = [(0, "@", frozenset())]
        visited = {}

        while queue:
            dist, curr, inventory = heappop(queue)

            if len(inventory) == len(self.keys):
                return dist

            state = (curr, inventory)
            if state in visited and visited[state] <= dist:
                continue

            visited[state] = dist

            for next_key, (d_reach, d_needed) in graph[curr].items():
                if next_key in inventory:
                    continue

                if d_needed.issubset(inventory):
                    new_inventory = inventory | frozenset([next_key])
                    new_dist = dist + d_reach

                    new_state = (next_key, new_inventory)
                    if new_dist < visited.get(new_state, float("inf")):
                        heappush(queue, (new_dist, next_key, new_inventory))

        return -1

    def part2(self) -> int:
        map_ = self.map.copy()
        original_x, original_y = self.start

        map_[(original_x - 1, original_y - 1)] = "0"
        map_[(original_x, original_y - 1)] = "#"
        map_[(original_x + 1, original_y - 1)] = "1"
        map_[(original_x - 1, original_y)] = "#"
        map_[(original_x, original_y)] = "#"
        map_[(original_x + 1, original_y)] = "#"
        map_[(original_x - 1, original_y + 1)] = "2"
        map_[(original_x, original_y + 1)] = "#"
        map_[(original_x + 1, original_y + 1)] = "3"
        starts = {v: k for k, v in map_.items() if v.isdigit()}
        keys = {char: pos for pos, char in map_.items() if char.islower()}

        graph = {}
        for r_id, pos in starts.items():
            graph[r_id] = self.get_reachable_targets(pos, map_)
        for key, pos in keys.items():
            graph[key] = self.get_reachable_targets(pos, map_)

        initial_pos = tuple(sorted(starts.keys()))
        queue = [(0, initial_pos, frozenset())]
        visited = {}

        while queue:
            distance, positions, inventory = heappop(queue)

            if len(inventory) == len(keys):
                return distance

            state = (positions, inventory)
            if visited.get(state, float("inf")) <= distance:
                continue

            visited[state] = distance

            for i, current_loc in enumerate(positions):
                for next_key, (distance_reach, distance_needed) in graph[current_loc].items():
                    if next_key not in inventory and distance_needed.issubset(inventory):
                        new_inv = inventory | frozenset([next_key])
                        new_positions = list(positions)
                        new_positions[i] = next_key
                        heappush(queue, (distance + distance_reach, tuple(new_positions), new_inv))

        return -1


if __name__ == '__main__':
    Solution().run()
