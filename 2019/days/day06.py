from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day06", 2019)

        self.orbits: dict[str, str] = {}
        for line in self.data:
            center, orbiter = line.split(")")
            self.orbits[orbiter] = center

    def part1(self) -> int:
        total_orbits = 0

        for orbiter in self.orbits:
            current = orbiter
            while current in self.orbits:
                current = self.orbits[current]
                total_orbits += 1

        return total_orbits

    def part2(self) -> int:
        you_path, san_path = [], []
        current_you, current_san = self.orbits["YOU"], self.orbits["SAN"]
        while current_you in self.orbits:
            you_path.append(current_you)
            current_you = self.orbits[current_you]

        while current_san in self.orbits:
            san_path.append(current_san)
            current_san = self.orbits[current_san]

        common_ancestor = next(node for node in you_path if node in san_path)
        return you_path.index(common_ancestor) + san_path.index(common_ancestor)


if __name__ == '__main__':
    Solution().run()
