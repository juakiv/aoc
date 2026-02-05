from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08", 2019)

        self.nums: list[int] = [int(x) for x in self.data[0]]
        self.layers: list[list[int]] = []
        for i in range(0, len(self.nums), 25 * 6):
            self.layers.append(self.nums[i:i + 25 * 6])

    def part1(self) -> int:
        fewest_zeroes = float("inf")
        result = 0
        for layer in self.layers:
            zeroes = layer.count(0)

            if zeroes < fewest_zeroes:
                fewest_zeroes = zeroes
                result = layer.count(1) * layer.count(2)

        return result

    def part2(self) -> str:
        image = [2] * (25 * 6)

        for layer in self.layers:
            for i in range(len(image)):
                if image[i] == 2:
                    image[i] = layer[i]

        for i in range(6):
            for j in range(25):
                print(" " if image[i * 25 + j] == 0 else "#", end="")
            print()

        return "See print above. :)"


if __name__ == '__main__':
    Solution().run()
