from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day14", 2018)[0]

        self.target = int(self.data)

    def part1(self) -> int:
        recipes = [3, 7]
        elf1 = 0
        elf2 = 1

        while len(recipes) < self.target + 10:
            current_sum = recipes[elf1] + recipes[elf2]

            if current_sum >= 10:
                recipes.append(current_sum // 10)
            recipes.append(current_sum % 10)

            elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
            elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

        result_digits = recipes[self.target:self.target + 10]
        return int("".join(str(digit) for digit in result_digits))

    def part2(self) -> int:
        target = [int(d) for d in str(self.target)]
        target_len = len(target)

        recipes = [3, 7]
        elf1 = 0
        elf2 = 1

        while True:
            current_sum = recipes[elf1] + recipes[elf2]

            if current_sum >= 10:
                new_digits = [1, current_sum % 10]
            else:
                new_digits = [current_sum]

            for digit in new_digits:
                recipes.append(digit)

                if len(recipes) >= target_len:
                    if recipes[-target_len:] == target:
                        return len(recipes) - target_len

            elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
            elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)


if __name__ == '__main__':
    Solution().run()
