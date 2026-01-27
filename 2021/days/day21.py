from collections import Counter
from functools import lru_cache
from itertools import product

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day21", 2021)

        self.player_positions = [int(line.split()[-1]) for line in self.data]

    def part1(self) -> int:
        dice_num = 0
        scores = [0, 0]
        positions = self.player_positions.copy()
        turn = 0

        while all(score < 1000 for score in scores):
            roll = sum(((dice_num + i) % 100) + 1 for i in range(3))
            dice_num += 3
            positions[turn] = (positions[turn] + roll - 1) % 10 + 1
            scores[turn] += positions[turn]
            turn = 1 - turn

        losing_score = min(scores)
        return losing_score * dice_num

    @lru_cache(maxsize=None)
    def wins(self, p1_pos, p2_pos, p1_score, p2_score, turn) -> tuple[int, int]:
        if p1_score >= 21:
            return 1, 0

        if p2_score >= 21:
            return 0, 1

        total_wins = (0, 0)
        roll_freq = Counter(sum(rolls) for rolls in product([1, 2, 3], repeat=3))
        for roll, freq in roll_freq.items():
            if turn == 0:
                new_p1_pos = (p1_pos + roll - 1) % 10 + 1
                new_p1_score = p1_score + new_p1_pos
                wins = self.wins(new_p1_pos, p2_pos, new_p1_score, p2_score, 1)
            else:
                new_p2_pos = (p2_pos + roll - 1) % 10 + 1
                new_p2_score = p2_score + new_p2_pos
                wins = self.wins(p1_pos, new_p2_pos, p1_score, new_p2_score, 0)

            total_wins = (total_wins[0] + wins[0] * freq, total_wins[1] + wins[1] * freq)

        return total_wins

    def part2(self) -> int:
        wins = self.wins(*self.player_positions, 0, 0, 0)
        return max(wins)


if __name__ == '__main__':
    Solution().run()
