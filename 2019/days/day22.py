from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day22", 2019)

    def part1(self) -> int:
        card_position = 2019
        stack_size = 10007

        for instruction in self.data:
            if instruction == "deal into new stack":
                card_position = (stack_size - 1) - card_position
            elif instruction.startswith("cut"):
                num = int(instruction.split()[1])
                card_position = (card_position - num) % stack_size
            elif instruction.startswith("deal with increment"):
                num = int(instruction.split()[-1])
                card_position = (card_position * num) % stack_size

        return card_position

    @staticmethod
    def combine_linear(a1: int, b1: int, a2: int, b2: int, stack_size: int) -> tuple[int, int]:
        return (a1 * a2) % stack_size, (b1 * a2 + b2) % stack_size

    def part2(self) -> int:
        card_position = 2020
        total_cards = 119315717514047
        repetitions = 101741582076661

        slope, intercept = 1, 0

        for instruction in reversed(self.data):
            if instruction == "deal into new stack":
                slope, intercept = self.combine_linear(slope, intercept, -1, total_cards - 1, total_cards)
            elif instruction.startswith("cut"):
                num = int(instruction.split()[-1])
                slope, intercept = self.combine_linear(slope, intercept, 1, num, total_cards)
            elif instruction.startswith("deal with increment"):
                num = int(instruction.split()[-1])
                inverse_num = pow(num, -1, total_cards)
                slope, intercept = self.combine_linear(slope, intercept, inverse_num, 0, total_cards)

        final_slope = pow(slope, repetitions, total_cards)
        final_intercept = (intercept * (final_slope - 1) * pow(slope - 1, -1, total_cards)) % total_cards

        return (final_slope * card_position + final_intercept) % total_cards


if __name__ == '__main__':
    Solution().run()
