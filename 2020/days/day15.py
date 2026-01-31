from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day15", 2020)

        self.nums = [int(x) for x in self.data[0].split(",")]

    def part1(self) -> int:
        last_seen = {}

        for i, num in enumerate(self.nums[:-1], start=1):
            last_seen[num] = i

        current = self.nums[-1]
        turn = len(self.nums)

        while turn < 2020:
            if current in last_seen:
                next_num = turn - last_seen[current]
            else:
                next_num = 0

            last_seen[current] = turn
            current = next_num
            turn += 1

        return current

    def part2(self) -> int:
        last_seen = {}

        for i, num in enumerate(self.nums[:-1], start=1):
            last_seen[num] = i

        current = self.nums[-1]
        turn = len(self.nums)

        while turn < 30_000_000:
            if current in last_seen:
                next_num = turn - last_seen[current]
            else:
                next_num = 0

            last_seen[current] = turn
            current = next_num
            turn += 1

        return current


if __name__ == '__main__':
    Solution().run()
