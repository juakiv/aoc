from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day10", 2021)

        self.tags = { "(": ")", "[": "]", "{": "}", "<": ">" }

    def part1(self) -> int:
        total_syntax_error_score = 0
        syntax_error_scores = { ")": 3, "]": 57, "}": 1197, ">": 25137 }

        for line in self.data:
            stack = []
            for char in line:
                if char in self.tags:
                    stack.append(char)
                else:
                    if not stack:
                        total_syntax_error_score += syntax_error_scores.get(char, 0)
                        break
                    if self.tags[stack.pop()] != char:
                        total_syntax_error_score += syntax_error_scores.get(char, 0)
                        break

        return total_syntax_error_score

    def part2(self) -> int:
        completion_scores = { ")": 1, "]": 2, "}": 3, ">": 4 }

        incomplete_line_scores = []
        for line in self.data:
            stack = []
            corrupted = False
            for char in line:
                if char in self.tags:
                    stack.append(char)
                else:
                    if not stack:
                        corrupted = True
                        break
                    if self.tags[stack.pop()] != char:
                        corrupted = True
                        break

            if not corrupted and stack:
                score = 0
                while stack:
                    closing_char = self.tags[stack.pop()]
                    score = score * 5 + completion_scores[closing_char]
                incomplete_line_scores.append(score)

        return sorted(incomplete_line_scores)[len(incomplete_line_scores) // 2]


if __name__ == '__main__':
    Solution().run()
