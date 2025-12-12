from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day12", 2025)

        self.presents: dict[int, tuple[int, list[list[str]]]] = {}
        self.instructions: list[tuple[tuple[int, int], list[int]]] = []

        counter = 0
        shape = []
        shape_count = 0
        for line in self.data:
            if "#" in line:
                shape.append(line)
                shape_count += line.count("#")

            if len(shape) == 3:
                self.presents[counter] = (shape_count, shape)
                shape = []
                counter += 1
                shape_count = 0

            if "x" in line:
                size, present_counts = line.split(": ")
                x, y = map(int, size.split("x"))
                present_counts = list(map(int, present_counts.split(" ")))
                self.instructions.append(((x, y), present_counts))

    def part1(self) -> int:
        total_solvable_regions = 0

        for instruction in self.instructions:
            area_size = instruction[0][0] * instruction[0][1]
            required_area = sum(pattern_size[0] * count for pattern_size, count in zip(self.presents.values(), instruction[1]))

            if required_area <= area_size and required_area * 1.2 < area_size:
                total_solvable_regions += 1

        return total_solvable_regions

    def part2(self) -> str:
        return ":)"


if __name__ == '__main__':
    Solution().run()
