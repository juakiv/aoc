from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day12", 2021)

        self.cave_connections: dict[str, list[str]] = {}
        for line in self.data:
            a, b = line.split("-")
            if a not in self.cave_connections:
                self.cave_connections[a] = []
            if b not in self.cave_connections:
                self.cave_connections[b] = []
            self.cave_connections[a].append(b)
            self.cave_connections[b].append(a)

    def part1(self) -> int:
        total_paths = 0
        paths_to_explore = [("start", { "start" })]

        while paths_to_explore:
            current_cave, visited_small_caves = paths_to_explore.pop()

            for next_cave in self.cave_connections[current_cave]:
                if next_cave == "end":
                    total_paths += 1
                elif next_cave.islower() and next_cave in visited_small_caves:
                    continue
                else:
                    new_visited = visited_small_caves.copy()
                    if next_cave.islower():
                        new_visited.add(next_cave)
                    paths_to_explore.append((next_cave, new_visited))

        return total_paths

    def part2(self) -> int:
        total_paths = 0
        visited_small_caves = set()
        paths_to_explore = [("start", visited_small_caves, False)]

        while paths_to_explore:
            current_cave, visited_small_caves, has_visited_twice = paths_to_explore.pop()

            for next_cave in self.cave_connections[current_cave]:
                if next_cave == "end":
                    total_paths += 1
                elif next_cave == "start":
                    continue
                elif next_cave.islower() and next_cave in visited_small_caves:
                    if has_visited_twice:
                        continue
                    else:
                        paths_to_explore.append((next_cave, visited_small_caves.copy(), True))
                else:
                    new_visited = visited_small_caves.copy()
                    if next_cave.islower():
                        new_visited.add(next_cave)
                    paths_to_explore.append((next_cave, new_visited, has_visited_twice))


        return total_paths


if __name__ == '__main__':
    Solution().run()
