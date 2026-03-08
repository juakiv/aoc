from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09", 2017)[0]

    @staticmethod
    def parse_stream(stream: str) -> tuple[int, int]:
        score = 0
        garbage_count = 0

        depth = 0
        garbage = False
        skip_next = False

        for char in stream:
            if skip_next:
                skip_next = False
                continue

            if garbage:
                if char == ">":
                    garbage = False

                elif char == "!":
                    skip_next = True

                else:
                    garbage_count += 1

                continue

            if char == "{":
                depth += 1

            elif char == "}":
                score += depth
                depth -= 1

            elif char == "<":
                garbage = True

        return score, garbage_count

    def part1(self) -> int:
        score, _ = self.parse_stream(self.data)
        return score

    def part2(self) -> int:
        _, garbage_count = self.parse_stream(self.data)
        return garbage_count


if __name__ == '__main__':
    Solution().run()
