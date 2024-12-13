from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day13")

        self.prizes: list[dict[str, int]] = []

        for x in range(0, len(self.data), 4):
            _, button_a_x, _, button_a_y = self.data[x].replace(", ", "+").split("+")
            _, button_b_x, _, button_b_y = self.data[x + 1].replace(", ", "+").split("+")
            _, prize_x, _, prize_y = self.data[x + 2].replace(", ", "=").split("=")

            self.prizes.append({
                "prize_x": int(prize_x),
                "prize_y": int(prize_y),
                "button_a_x": int(button_a_x),
                "button_a_y": int(button_a_y),
                "button_b_x": int(button_b_x),
                "button_b_y": int(button_b_y)
            })

    @staticmethod
    def calculate_token_requirement(prize: dict[str, int], part: int) -> int:
        prize_x, prize_y, button_a_x, button_a_y, button_b_x, button_b_y = prize.values()

        if part == 2:
            prize_x += 10000000000000
            prize_y += 10000000000000

        button_a_presses = (prize_x * button_b_y - prize_y * button_b_x) // (
                button_b_y * button_a_x - button_b_x * button_a_y)
        button_b_presses = (prize_x * button_a_y - prize_y * button_a_x) // (
                button_a_y * button_b_x - button_b_y * button_a_x)

        if button_a_x * button_a_presses + button_b_x * button_b_presses == prize_x and \
                button_a_y * button_a_presses + button_b_y * button_b_presses == prize_y:
            return 3 * int(button_a_presses) + int(button_b_presses)
        else:
            return 0

    def part1(self) -> int:
        return sum(self.calculate_token_requirement(prize, 1) for prize in self.prizes)

    def part2(self) -> int:
        return sum(self.calculate_token_requirement(prize, 2) for prize in self.prizes)


if __name__ == '__main__':
    Solution().run()
