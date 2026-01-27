from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day25", 2021)

    @staticmethod
    def move_cucumbers(map_: list[list[str]]) -> tuple[list[list[str]], bool]:
        rows, cols = len(map_), len(map_[0])
        moved = False

        new_map = [row.copy() for row in map_]
        for row in range(rows):
            for col in range(cols):
                if map_[row][col] == ">" and map_[row][(col + 1) % cols] == ".":
                    new_map[row][col] = "."
                    new_map[row][(col + 1) % cols] = ">"
                    moved = True
        map_ = new_map

        new_map = [row.copy() for row in map_]
        for row in range(rows):
            for col in range(cols):
                if map_[row][col] == "v" and map_[(row + 1) % rows][col] == ".":
                    new_map[row][col] = "."
                    new_map[(row + 1) % rows][col] = "v"
                    moved = True
        return new_map, moved

    def part1(self) -> int:
        total_steps = 0

        moved = True
        map_ = [list(line) for line in self.data]
        while moved:
            map_, moved = self.move_cucumbers(map_)
            total_steps += 1

        return total_steps

    def part2(self) -> str:
        return ":)"


if __name__ == '__main__':
    Solution().run()
