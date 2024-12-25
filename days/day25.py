from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day25")

        self.locks = []
        self.keys = []

        for i in range(0, len(self.data), 8):
            if self.data[i] == "#####":
                lock = []
                for j in range(5):
                    pin_count = 0
                    for k in range(6):
                        if self.data[i + 1 + k][j] == "#":
                            pin_count += 1

                    lock.append(pin_count)
                self.locks.append(lock)
            elif self.data[i] == ".....":
                key = []
                for j in range(5):
                    pin_count = 5
                    for k in range(6):
                        if self.data[i + 1 + k][j] == ".":
                            pin_count -= 1

                    key.append(pin_count)
                self.keys.append(key)

    def part1(self) -> int:
        working_keys = 0
        for key in self.keys:
            for lock in self.locks:
                is_working_pair = True
                for a, b in zip(key, lock):
                    if a + b > 5:
                        is_working_pair = False
                        break

                if is_working_pair:
                    working_keys += 1

        return working_keys


    def part2(self) -> int:
        return 0


if __name__ == '__main__':
    Solution().run()
