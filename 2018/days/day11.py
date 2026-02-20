from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day11", 2018)
        self.serial_number = int(self.data[0])

    def power_level(self, x: int, y: int) -> int:
        rack_id = x + 10
        power = (rack_id * y + self.serial_number) * rack_id
        hundreds_digit = (power // 100) % 10
        return hundreds_digit - 5

    def grid(self) -> list[list[int]]:
        grid = [[0] * 301 for _ in range(301)]
        for y in range(1, 301):
            row_sum = 0
            for x in range(1, 301):
                row_sum += self.power_level(x, y)
                grid[y][x] = row_sum + grid[y - 1][x]
        return grid

    @staticmethod
    def max_power(grid: list[list[int]], sizes: list[int]) -> str:
        max_power = -float('inf')
        best_coord = ""

        for size in sizes:
            for y in range(1, 300 - size + 2):
                for x in range(1, 300 - size + 2):
                    current_sum = (
                            grid[y + size - 1][x + size - 1] -
                            grid[y - 1][x + size - 1] -
                            grid[y + size - 1][x - 1] +
                            grid[y - 1][x - 1]
                    )

                    if current_sum > max_power:
                        max_power = current_sum
                        best_coord = f"{x},{y}" if size == 3 and len(sizes) == 1 else f"{x},{y},{size}"

        return best_coord

    def part1(self) -> str:
        grid = self.grid()
        return self.max_power(grid, [3])

    def part2(self) -> str:
        grid = self.grid()
        return self.max_power(grid, list(range(1, 301)))


if __name__ == '__main__':
    Solution().run()
