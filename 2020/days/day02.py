from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02", 2020)

        self.passwords: list[tuple[int, int, str, str]] = []
        for line in self.data:
            rules, password = line.split(": ")
            range_part, letter = rules.split(" ")
            min_count, max_count = map(int, range_part.split("-"))
            self.passwords.append((min_count, max_count, letter, password))

    def part1(self) -> int:
        valid_passwords = 0

        for password in self.passwords:
            min_count, max_count, letter, pwd = password
            letter_count = pwd.count(letter)
            if min_count <= letter_count <= max_count:
                valid_passwords += 1

        return valid_passwords

    def part2(self) -> int:
        valid_passwords = 0

        for password in self.passwords:
            pos1, pos2, letter, pwd = password
            first_position_matches = pwd[pos1 - 1] == letter
            second_position_matches = pwd[pos2 - 1] == letter

            if first_position_matches ^ second_position_matches:
                valid_passwords += 1

        return valid_passwords


if __name__ == '__main__':
    Solution().run()
