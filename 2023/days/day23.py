from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day23", 2023)

        self.starting_point = (self.data[0].index("."), 0)
        self.ending_point = (self.data[-1].index("."), len(self.data) - 1)

    def part1(self) -> int:
        queue = [(self.starting_point, set())]
        paths = []

        while queue:
            (x, y), path = queue.pop()

            if (x, y) == self.ending_point:
                paths.append(len(path))
                continue


            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if self.data[y][x] == "v":
                directions = [(0, 1)]
            elif self.data[y][x] == "^":
                directions = [(0, -1)]
            elif self.data[y][x] == "<":
                directions = [(-1, 0)]
            elif self.data[y][x] == ">":
                directions = [(1, 0)]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(self.data[0]) and 0 <= new_y < len(self.data):
                    if self.data[new_y][new_x] == "#":
                        continue

                    if (new_x, new_y) not in path:
                        new_path = set(path)
                        new_path.add((new_x, new_y))
                        queue.append(((new_x, new_y), new_path))

        return max(paths)

    def get_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        neighbors = []
        for delta_x, delta_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x + delta_x
            new_y = y + delta_y

            if 0 <= new_x < len(self.data[0]) and 0 <= new_y < len(self.data) and self.data[new_y][new_x] != "#":
                neighbors.append((new_x, new_y))

        return neighbors

    def part2(self) -> int:
        # find junctions
        junction_positions = set()

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "#":
                    continue

                valid_neighbors = self.get_neighbors(x, y)

                if len(valid_neighbors) != 2:
                    junction_positions.add((x, y))

        junction_positions.add(self.starting_point)
        junction_positions.add(self.ending_point)

        # compress graph
        compressed_graph = defaultdict(list)

        for junction_x, junction_y in junction_positions:
            for neighbor_x, neighbor_y in self.get_neighbors(junction_x, junction_y):
                current_x = neighbor_x
                current_y = neighbor_y
                previous_position = (junction_x, junction_y)
                path_length = 1

                while (current_x, current_y) not in junction_positions:
                    next_positions = [position for position in self.get_neighbors(current_x, current_y) if position != previous_position]
                    next_x, next_y = next_positions[0]

                    previous_position = (current_x, current_y)
                    current_x, current_y = next_x, next_y
                    path_length += 1

                compressed_graph[(junction_x, junction_y)].append(((current_x, current_y), path_length))

        # traverse compressed graph to find longest path
        queue = [(self.starting_point, 0, {self.starting_point})]
        longest_path = 0

        while queue:
            current_position, current_length, path = queue.pop()

            if current_position == self.ending_point:
                longest_path = max(longest_path, current_length)
                continue

            for neighbor_position, edge_length in compressed_graph[current_position]:
                if neighbor_position not in path:
                    new_path = set(path)
                    new_path.add(neighbor_position)
                    queue.append((neighbor_position, current_length + edge_length, new_path))

        return longest_path



if __name__ == '__main__':
    Solution().run()
