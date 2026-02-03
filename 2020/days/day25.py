from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day25", 2020)

        self.door_public_key = int(self.data[0])
        self.card_public_key = int(self.data[1])

    @staticmethod
    def loop_size(public_key: int) -> int:
        value = 1
        loop_size = 0

        while value != public_key:
            value = (value * 7) % 20201227
            loop_size += 1

        return loop_size

    @staticmethod
    def encryption_key(subject_number: int, loop_size: int) -> int:
        value = 1

        for _ in range(loop_size):
            value = (value * subject_number) % 20201227

        return value

    def part1(self) -> int:
        loop_size = self.loop_size(self.card_public_key)
        encryption_key = self.encryption_key(self.door_public_key, loop_size)

        loop_size2 = self.loop_size(self.door_public_key)
        encryption_key2 = self.encryption_key(self.card_public_key, loop_size2)

        if encryption_key != encryption_key2:
            raise ValueError("Encryption keys do not match!")

        return encryption_key

    def part2(self) -> str:
        return ":)"


if __name__ == '__main__':
    Solution().run()
