from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day15", 2023)

        self.initialization_steps: list[str] = self.data[0].split(",")

    @staticmethod
    def hash_algorithm(input_data: str) -> int:
        current_value = 0

        for char in input_data:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256

        return current_value

    def part1(self) -> int:
        return sum(self.hash_algorithm(step) for step in self.initialization_steps)

    def part2(self) -> int:
        boxes = [[] for _ in range(256)]
        focal_lengths = {}

        for step in self.initialization_steps:
            if "=" in step:
                label, focal_length = step.split("=")
                box = self.hash_algorithm(label)

                focal_lengths[label] = int(focal_length)

                if label in boxes[box]:
                    boxes[box][boxes[box].index(label)] = label
                else:
                    boxes[box].append(label)

            if "-" in step:
                label = step[:-1]
                box = self.hash_algorithm(label)
                if label in boxes[box]:
                    boxes[box].remove(label)

        focusing_power = 0
        for i, box in enumerate(boxes):
            for slot, label in enumerate(box):
                focusing_power += (i + 1) * (slot + 1) * focal_lengths.get(label)

        return focusing_power


if __name__ == '__main__':
    Solution().run()
