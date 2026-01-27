from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day24", 2021)

        self.instructions: list[tuple[str, str | int, str | int]] = [line.split() for line in self.data]
        self.blocks = self.get_blocks()

    def get_blocks(self) -> list[tuple[int, int, int]]:
        blocks = []
        i = 0
        while i < len(self.instructions):
            if self.instructions[i][0] == "inp":
                block = self.instructions[i:i + 18]

                div_z = int(block[4][2])
                add_x = int(block[5][2])
                add_y = int(block[15][2])

                blocks.append((div_z, add_x, add_y))
                i += 18
            else:
                i += 1

        return blocks

    def part1(self) -> int:
        n = len(self.blocks)

        digits = [0] * n
        stack = []

        for i, (div_z, add_x, add_y) in enumerate(self.blocks):
            if div_z == 1:
                stack.append((i, add_y))
            else:
                j, prev_add_y = stack.pop()
                diff = prev_add_y + add_x

                if diff >= 0:
                    digits[j] = 9 - diff
                    digits[i] = 9
                else:
                    digits[j] = 9
                    digits[i] = 9 + diff

        return int("".join(map(str, digits)))

    def part2(self) -> int:
        n = len(self.blocks)

        digits = [0] * n
        stack = []

        for i, (div_z, add_x, add_y) in enumerate(self.blocks):
            if div_z == 1:
                stack.append((i, add_y))
            else:
                j, prev_add_y = stack.pop()
                diff = prev_add_y + add_x

                if diff >= 0:
                    digits[j] = 1
                    digits[i] = 1 + diff
                else:
                    digits[j] = 1 - diff
                    digits[i] = 1

        return int("".join(map(str, digits)))


if __name__ == '__main__':
    Solution().run()
