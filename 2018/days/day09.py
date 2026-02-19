import re
from collections import deque

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09", 2018)[0]
        self.num_players, self.last_marble = list(map(int, re.findall(r'\d+', self.data)))

    @staticmethod
    def play(num_players: int, last_marble: int) -> int:
        scores = [0] * num_players
        circle = deque([0])

        for marble in range(1, last_marble + 1):
            if marble % 23 == 0:
                circle.rotate(7)
                player_index = marble % num_players
                scores[player_index] += marble + circle.pop()
                circle.rotate(-1)
            else:
                circle.rotate(-1)
                circle.append(marble)

        return max(scores)

    def part1(self) -> int:
        return self.play(self.num_players, self.last_marble)

    def part2(self) -> int:
        return self.play(self.num_players, self.last_marble * 100)


if __name__ == '__main__':
    Solution().run()
