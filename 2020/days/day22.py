from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day22", 2020, "\n\n")

        self.player1: list[int] = [int(x) for x in self.data[0].split("\n")[1:]]
        self.player2: list[int] = [int(x) for x in self.data[1].split("\n")[1:]]

    @staticmethod
    def combat(player1: list[int], player2: list[int]) -> tuple[int, list[int]]:
        while player1 and player2:
            card1 = player1.pop(0)
            card2 = player2.pop(0)

            if card1 > card2:
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])

        return (1, player1) if player1 else (2, player2)

    def recursive_combat(self, player1: list[int], player2: list[int]) -> tuple[int, list[int]]:
        seen_states = set()

        while player1 and player2:
            state = (tuple(player1), tuple(player2))

            if state in seen_states:
                return 1, player1

            seen_states.add(state)

            card1 = player1.pop(0)
            card2 = player2.pop(0)

            if len(player1) >= card1 and len(player2) >= card2:
                winner, _ = self.recursive_combat(player1[:card1], player2[:card2])
            else:
                winner = 1 if card1 > card2 else 2

            if winner == 1:
                player1.extend([card1, card2])
            else:
                player2.extend([card2, card1])

        return (1, player1) if player1 else (2, player2)

    def part1(self) -> int:
        winner_score = 0
        winner, cards = self.combat(self.player1.copy(), self.player2.copy())

        for i, card in enumerate(reversed(cards), start=1):
            winner_score += i * card

        return winner_score

    def part2(self) -> int:
        winner_score = 0
        winner, cards = self.recursive_combat(self.player1.copy(), self.player2.copy())

        for i, card in enumerate(reversed(cards), start=1):
            winner_score += i * card

        return winner_score


if __name__ == '__main__':
    Solution().run()
