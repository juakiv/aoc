from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08", 2018)[0]
        self.nums: list[int] = [int(x) for x in self.data.split()]
        self.index = 0

    def process_node(self) -> tuple[int, int]:
        num_children = self.nums[self.index]
        num_metadata = self.nums[self.index + 1]
        self.index += 2

        total_metadata_sum = 0
        child_values = []

        for _ in range(num_children):
            metadata_sum, node_value = self.process_node()
            total_metadata_sum += metadata_sum
            child_values.append(node_value)

        node_metadata = []
        for _ in range(num_metadata):
            val = self.nums[self.index]
            node_metadata.append(val)
            total_metadata_sum += val
            self.index += 1

        if num_children == 0:
            node_value = sum(node_metadata)

        else:
            node_value = 0
            for idx in node_metadata:
                if 1 <= idx <= len(child_values):
                    node_value += child_values[idx - 1]

        return total_metadata_sum, node_value

    def part1(self) -> int:
        return self.process_node()[0]

    def part2(self) -> int:
        self.index = 0
        return self.process_node()[1]


if __name__ == '__main__':
    Solution().run()
