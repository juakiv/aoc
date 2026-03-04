from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = int(self.load_data("day03", 2017)[0])

    def part1(self) -> int:
        i = 1

        while i ** 2 < self.data:
            i += 2

        pivot = i ** 2 - (i - 1) // 2
        return (i - 1) // 2 + abs(pivot - self.data)

    def part2(self) -> int:
        grid = { (0, 0): 1 }

        x, y = 0, 0
        dir_x, dir_y = 1, 0
        step_limit = 1
        steps_taken = 0
        turns_now = 0

        while True:
            x += dir_x
            y += dir_y
            steps_taken += 1

            total = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0: continue
                    total += grid.get((x + i, y + j), 0)

            if total > self.data:
                return total

            grid[(x, y)] = total
            if steps_taken == step_limit:
                steps_taken = 0
                dir_x, dir_y = -dir_y, dir_x

                turns_now += 1
                if turns_now == 2:
                    turns_now = 0
                    step_limit += 1


if __name__ == '__main__':
    Solution().run()
