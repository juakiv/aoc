from collections import Counter, defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day14", 2021, "\n\n")

        self.template = self.data[0]
        self.rules = {}
        for line in self.data[1].split("\n"):
            pair, insert = line.split(" -> ")
            self.rules[pair] = insert

    def pair_insertion(self, template: str) -> str:
        result = []

        for i in range(len(template) - 1):
            pair = template[i:i + 2]
            result.append(template[i])

            if pair in self.rules:
                result.append(self.rules[pair])

        result.append(template[-1])
        return "".join(result)

    def part1(self) -> int:
        polymer = self.template
        for _ in range(10):
            polymer = self.pair_insertion(polymer)

        counts = Counter(polymer)
        return max(counts.values()) - min(counts.values())

    def part2(self) -> int:
        pair_counts = defaultdict(int)
        for i in range(len(self.template) - 1):
            pair = self.template[i:i + 2]
            pair_counts[pair] += 1

        for _ in range(40):
            new_pair_counts = defaultdict(int)
            for pair, count in pair_counts.items():
                if pair in self.rules:
                    insert = self.rules[pair]
                    new_pair_counts[pair[0] + insert] += count
                    new_pair_counts[insert + pair[1]] += count
                else:
                    new_pair_counts[pair] += count
            pair_counts = new_pair_counts

        char_counts = defaultdict(int)
        for pair, count in pair_counts.items():
            char_counts[pair[0]] += count
            char_counts[pair[1]] += count

        char_counts[self.template[0]] += 1
        char_counts[self.template[-1]] += 1
        for char in char_counts:
            char_counts[char] //= 2

        return max(char_counts.values()) - min(char_counts.values())


if __name__ == '__main__':
    Solution().run()
