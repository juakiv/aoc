from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02", 2022)

        self.rounds: list[list[str]] = [line.split() for line in self.data]

    @staticmethod
    def calculate_round_score(opponent: str, me: str) -> int:
        total_score = 0
        match (opponent, me):
            case ("A", "X") | ("B", "Y") | ("C", "Z"):
                total_score += 3
            case ("A", "Y") | ("B", "Z") | ("C", "X"):
                total_score += 6
            case _:
                total_score += 0

        total_score += {"X": 1, "Y": 2, "Z": 3}[me]

        return total_score

    def part1(self) -> int:
        total_score = 0

        for round_ in self.rounds:
            opponent, me = round_
            total_score += self.calculate_round_score(opponent, me)

        return total_score

    def part2(self) -> int:
        total_score = 0

        opponent_map = {"A": 0, "B": 1, "C": 2}
        outcome_map = {"X": -1, "Y": 0, "Z": 1}

        for round_ in self.rounds:
            opponent, expected_result = round_
            me = (opponent_map[opponent] + outcome_map[expected_result]) % 3

            total_score += self.calculate_round_score(opponent, ["X", "Y", "Z"][me])

        return total_score


if __name__ == '__main__':
    Solution().run()
