from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day04", 2019)

        self.range_start, self.range_end = map(int, self.data[0].split("-"))

    def passwords_in_range(self, part2: bool = False) -> list[int]:
        passwords = []

        for password in range(self.range_start, self.range_end + 1):
            str_password = str(password)

            if all(str_password[i] <= str_password[i + 1] for i in range(len(str_password) - 1)):

                if part2:
                    digit_counts = {digit: str_password.count(digit) for digit in set(str_password)}
                    if any(count == 2 for count in digit_counts.values()):
                        passwords.append(password)

                else:
                    if any(str_password.count(digit * 2) >= 1 for digit in set(str_password)):
                        passwords.append(password)

        return passwords

    def part1(self) -> int:
        return len(self.passwords_in_range())

    def part2(self) -> int:
        return len(self.passwords_in_range(True))


if __name__ == '__main__':
    Solution().run()
