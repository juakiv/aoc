from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08", 2021)

        self.segments: list[tuple[list[str], list[str]]] = []
        for line in self.data:
            patterns, output = line.split(" | ")
            patterns = patterns.split()
            output = output.split()
            self.segments.append((patterns, output))

    def part1(self) -> int:
        times = 0
        for _, output in self.segments:
            for digit in output:
                if len(digit) in (2, 3, 4, 7):
                    times += 1
        return times

    def part2(self) -> int:
        total = 0

        for patterns, outputs in self.segments:
            patterns = [set(p) for p in patterns]
            output = [set(o) for o in outputs]

            digits = {
                1: next(p for p in patterns if len(p) == 2),
                4: next(p for p in patterns if len(p) == 4),
                7: next(p for p in patterns if len(p) == 3),
                8: next(p for p in patterns if len(p) == 7)
            }


            six_length = [p for p in patterns if len(p) == 6]
            digits[9] = next(p for p in six_length if digits[4] <= p)
            digits[0] = next(p for p in six_length if digits[1] <= p != digits[9])
            digits[6] = next(p for p in six_length if p not in (digits[0], digits[9]))

            five_length = [p for p in patterns if len(p) == 5]
            digits[3] = next(p for p in five_length if digits[1] <= p)
            digits[5] = next(p for p in five_length if p <= digits[6] != digits[3])
            digits[2] = next(p for p in five_length if p not in (digits[3], digits[5]))

            digit_map = {frozenset(v): k for k, v in digits.items()}

            value = 0
            for o in output:
                value = value * 10 + digit_map[frozenset(o)]

            total += value

        return total


if __name__ == '__main__':
    Solution().run()
