from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day04", 2021, "\n\n")

        self.numbers = [int(x) for x in self.data[0].split(",")]
        self.boards = []

        for board_data in self.data[1:]:
            board = []
            for line in board_data.split("\n"):
                row = [int(x) for x in line.split() if x]
                board.append(row)
            self.boards.append(board)

    def part1(self) -> int:
        for number in self.numbers:
            for board in self.boards:

                for i in range(5):
                    for j in range(5):
                        if board[i][j] == number:
                            board[i][j] = -1

                for i in range(5):
                    if all(board[i][j] == -1 for j in range(5)) or all(board[j][i] == -1 for j in range(5)):
                        unmarked_sum = sum(board[x][y] for x in range(5) for y in range(5) if board[x][y] != -1)
                        return unmarked_sum * number

        return 0

    def part2(self) -> int:
        completed_boards = set()
        for number in self.numbers:
            for b_index, board in enumerate(self.boards):

                if b_index in completed_boards:
                    continue

                for i in range(5):
                    for j in range(5):
                        if board[i][j] == number:
                            board[i][j] = -1

                for i in range(5):
                    if all(board[i][j] == -1 for j in range(5)) or all(board[j][i] == -1 for j in range(5)):
                        completed_boards.add(b_index)

                        if len(completed_boards) == len(self.boards):
                            unmarked_sum = sum(board[x][y] for x in range(5) for y in range(5) if board[x][y] != -1)
                            return unmarked_sum * number

        return 0


if __name__ == '__main__':
    Solution().run()
