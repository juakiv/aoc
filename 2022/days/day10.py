from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day10", 2022)

        self.instructions: list[tuple[str, int | None]] = []
        for line in self.data:
            instruction, *value = line.split()
            self.instructions.append((instruction, int(value[0]) if value else None))

    def part1(self) -> int:
        signal_strength = 0
        x = 1
        cycle = 0

        for instruction, value in self.instructions:
            cycle += 1
            if cycle == 20 or (cycle % 40 == 20 and cycle <= 220):
                signal_strength += cycle * x

            if instruction == "addx":
                cycle += 1
                if cycle == 20 or (cycle % 40 == 20 and cycle <= 220):
                    signal_strength += cycle * x
                x += value

        return signal_strength

    def part2(self) -> str:
        x = 1
        cycle = 0
        screen: list[str] = []

        for instruction, value in self.instructions:
            pixel_pos = cycle % 40
            cycle += 1
            if pixel_pos in (x - 1, x, x + 1):
                screen.append("#")
            else:
                screen.append(" ")

            if instruction == "addx":
                pixel_pos = cycle % 40
                cycle += 1
                if pixel_pos in (x - 1, x, x + 1):
                    screen.append("#")
                else:
                    screen.append(" ")
                x += value

        print()
        for row in range(6):
            print("".join(screen[row * 40:(row + 1) * 40]))
        print()

        return "See the printed output above."


if __name__ == '__main__':
    Solution().run()
