from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07", 2020)

        self.rules: dict[str, dict[str, int]] = {}
        for line in self.data:
            bag, contents = line.split(" bags contain ")
            content_rules = {}

            if contents != "no other bags.":
                for content in contents.split(", "):
                    parts = content.split(" ")
                    count = int(parts[0])
                    color = " ".join(parts[1:3])
                    content_rules[color] = count

            self.rules[bag] = content_rules

    def part1(self) -> int:
        count = 0

        for bag in self.rules:
            if bag == "shiny gold":
                continue

            queue = [bag]
            seen = set()

            while queue:
                current = queue.pop()

                if current == "shiny gold":
                    count += 1
                    break

                seen.add(current)

                for content in self.rules[current]:
                    if content not in seen:
                        queue.append(content)

        return count

    def part2(self) -> int:
        total_bags = 0

        queue = [("shiny gold", 1)]
        while queue:
            current_bag, multiplier = queue.pop()

            for content_bag, count in self.rules[current_bag].items():
                total_bags += count * multiplier
                queue.append((content_bag, count * multiplier))

        return total_bags


if __name__ == '__main__':
    Solution().run()
