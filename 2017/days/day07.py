import re
from collections import Counter

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07", 2017)

        self.nodes = {}
        self.cumulative_weights = {}

        for line in self.data:
            parts = re.findall(r"\w+", line)
            name = parts[0]
            weight = int(parts[1])
            children = parts[2:]

            self.nodes[name] = { "weight": weight, "children": children }

    def total_weight(self, name):
        if name in self.cumulative_weights:
            return self.cumulative_weights[name]

        node = self.nodes[name]
        total = node["weight"] + sum(self.total_weight(child) for child in node["children"])
        self.cumulative_weights[name] = total

        return total

    def find_imbalance(self, name, target_total):
        node = self.nodes[name]
        child_totals = {child: self.total_weight(child) for child in node["children"]}

        seen_weights = Counter(child_totals.values())

        if len(seen_weights) <= 1:
            actual_total = self.total_weight(name)
            adjustment = target_total - actual_total
            return node["weight"] + adjustment

        common_weight = seen_weights.most_common(1)[0][0]
        outlier_weight = seen_weights.most_common()[-1][0]

        outlier_child = next(child for child, total in child_totals.items() if total == outlier_weight)

        return self.find_imbalance(outlier_child, common_weight)

    def part1(self) -> str:
        all_names = set(self.nodes.keys())
        all_children = set()

        for node in self.nodes.values():
            all_children.update(node["children"])

        root = (all_names - all_children).pop()
        return root

    def part2(self) -> int:
        root = self.part1()

        node = self.nodes[root]
        child_totals = {child: self.total_weight(child) for child in node["children"]}
        seen_weights = Counter(child_totals.values())

        common_weight = seen_weights.most_common(1)[0][0]
        outlier_weight = seen_weights.most_common()[-1][0]
        outlier_child = next(child for child, total in child_totals.items() if total == outlier_weight)

        return self.find_imbalance(outlier_child, common_weight)


if __name__ == '__main__':
    Solution().run()
