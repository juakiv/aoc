from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day04", 2017)

        self.passphrases: list[list[str]] = [words.split() for words in self.data]

    def part1(self) -> int:
        valid_passphrases = 0

        for passphrase in self.passphrases:
            if len(set(passphrase)) == len(passphrase):
                valid_passphrases += 1

        return valid_passphrases

    def part2(self) -> int:
        valid_passphrases = 0

        for passphrase in self.passphrases:
            sorted_passphrase = ["".join(sorted(word)) for word in passphrase]
            if len(set(sorted_passphrase)) == len(passphrase):
                valid_passphrases += 1

        return valid_passphrases


if __name__ == '__main__':
    Solution().run()
