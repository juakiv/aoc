from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day23", 2020)[0]

        self.cups = [int(c) for c in self.data]

    @staticmethod
    def play(cups: list[int], total_cups: int, moves: int) -> list[int]:
        max_label = total_cups
        next_cup = [0] * (total_cups + 1)

        for a, b in zip(cups, cups[1:]):
            next_cup[a] = b

        if total_cups > len(cups):
            next_cup[cups[-1]] = max(cups) + 1
            for label in range(max(cups) + 1, total_cups):
                next_cup[label] = label + 1
            next_cup[total_cups] = cups[0]

        else:
            next_cup[cups[-1]] = cups[0]

        current = cups[0]
        for _ in range(moves):
            picked1 = next_cup[current]
            picked2 = next_cup[picked1]
            picked3 = next_cup[picked2]

            next_cup[current] = next_cup[picked3]
            dest = current - 1 or max_label

            while dest == picked1 or dest == picked2 or dest == picked3:
                dest -= 1
                if dest == 0:
                    dest = max_label

            next_cup[picked3] = next_cup[dest]
            next_cup[dest] = picked1

            current = next_cup[current]

        return next_cup

    def part1(self) -> int:
        next_cup = self.play(self.cups, len(self.cups), 100)

        result = []
        current = next_cup[1]

        while current != 1:
            result.append(str(current))
            current = next_cup[current]

        return int("".join(result))

    def part2(self) -> int:
        next_cup = self.play(self.cups, 1_000_000, 10_000_000)

        cup1 = next_cup[1]
        cup2 = next_cup[cup1]

        return cup1 * cup2


if __name__ == '__main__':
    Solution().run()
