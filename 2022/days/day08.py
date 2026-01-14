from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08", 2022)

        self.grid: list[list[int]] = [[int(height) for height in line] for line in self.data]

    def part1(self) -> int:
        visible_trees = 0

        rows = len(self.grid)
        cols = len(self.grid[0])

        edges_length = (rows * 2) + ((cols - 2) * 2)
        visible_trees += edges_length

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                height = self.grid[r][c]
                left_visible = all(self.grid[r][cc] < height for cc in range(c))
                right_visible = all(self.grid[r][cc] < height for cc in range(c + 1, cols))
                up_visible = all(self.grid[rr][c] < height for rr in range(r))
                down_visible = all(self.grid[rr][c] < height for rr in range(r + 1, rows))

                if left_visible or right_visible or up_visible or down_visible:
                    visible_trees += 1

        return visible_trees

    def part2(self) -> int:
        max_scenic_score = 0

        rows = len(self.grid)
        cols = len(self.grid[0])

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                height = self.grid[row][col]

                left_distance = 0
                for c in range(col - 1, -1, -1):
                    left_distance += 1
                    if self.grid[row][c] >= height:
                        break

                right_distance = 0
                for c in range(col + 1, cols):
                    right_distance += 1
                    if self.grid[row][c] >= height:
                        break

                up_distance = 0
                for r in range(row - 1, -1, -1):
                    up_distance += 1
                    if self.grid[r][col] >= height:
                        break

                down_distance = 0
                for r in range(row + 1, rows):
                    down_distance += 1
                    if self.grid[r][col] >= height:
                        break

                scenic_score = left_distance * right_distance * up_distance * down_distance
                max_scenic_score = max(max_scenic_score, scenic_score)

        return max_scenic_score


if __name__ == '__main__':
    Solution().run()
