import math
import re

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08", 2023, "\n\n")

        self.instructions: list[str] = self.data[0]
        self.maps: dict[str, list[str]] = {}

        for map_ in self.data[1].split("\n"):
            start_node, left_node, right_node, _ = re.split(r"[\W]+", map_)
            self.maps[start_node] = [left_node, right_node]

    def part1(self) -> int:
        steps = 0
        current_position = "AAA"

        while current_position != "ZZZ":
            left_node, right_node = self.maps[current_position]
            next_instruction = self.instructions[steps % len(self.instructions)]

            if next_instruction == "L":
                current_position = left_node
            else:
                current_position = right_node

            steps += 1

        return steps

    def part2(self) -> int:
        starting_nodes = list(filter(lambda x: x[2] == "A", self.maps.keys()))
        steps = []

        for start in starting_nodes:
            steps_to_end = 0
            current_position = start

            while current_position[2] != "Z":
                left_node, right_node = self.maps[current_position]
                next_instruction = self.instructions[steps_to_end % len(self.instructions)]

                if next_instruction == "L":
                    current_position = left_node
                else:
                    current_position = right_node

                steps_to_end += 1

            steps.append(steps_to_end)

        return math.lcm(*steps)


if __name__ == '__main__':
    Solution().run()
