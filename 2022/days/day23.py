from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day23", 2022)

        self.elves = set()
        for r, row in enumerate(self.data):
            for c, val in enumerate(row):
                if val == '#':
                    self.elves.add((r, c))

    @staticmethod
    def simulate_elf_movements(elves: set, round_: int) -> tuple[set, set]:
        # movement direction and checks (tile where elf moves and diagonals around it)
        directions = [
            ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),
            ((1, 0), [(1, -1), (1, 0), (1, 1)]),
            ((0, -1), [(-1, -1), (0, -1), (1, -1)]),
            ((0, 1), [(-1, 1), (0, 1), (1, 1)])
        ]

        neighbors = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)]

        proposals = {}
        moved_elves = set()

        for r, c in elves:
            if all((r + dr, c + dc) not in elves for dr, dc in neighbors):
                continue

            for i in range(4):
                move, checks = directions[(round_ + i) % 4]
                if all((r + dr, c + dc) not in elves for dr, dc in checks):
                    nr, nc = r + move[0], c + move[1]
                    proposals.setdefault((nr, nc), []).append((r, c))
                    break

        for target, sources in proposals.items():
            if len(sources) == 1:
                elves.remove(sources[0])
                elves.add(target)
                moved_elves.add(target)

        return elves, moved_elves

    def part1(self) -> int:
        elves = self.elves.copy()

        for round_ in range(10):
            elves, _ = self.simulate_elf_movements(elves, round_)

        min_r = min(r for r, c in elves)
        max_r = max(r for r, c in elves)
        min_c = min(c for r, c in elves)
        max_c = max(c for r, c in elves)

        return (max_r - min_r + 1) * (max_c - min_c + 1) - len(elves)

    def part2(self) -> int:
        elves = self.elves.copy()
        round_num = 0

        while True:
            elves, moved_elves = self.simulate_elf_movements(elves, round_num)
            round_num += 1

            if not moved_elves:
                break

        return round_num


if __name__ == '__main__':
    Solution().run()
