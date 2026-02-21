from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day12", 2018, "\n\n")

        self.initial_state: str = self.data[0].split(": ")[1]
        self.rules: dict[str, str] = {}
        for line in self.data[1].split("\n"):
            pattern, result = line.split(" => ")
            self.rules[pattern] = result

    def simulate_generation(self, state: str, index: int):
        state = "...." + state + "...."
        index += 4

        new_state = ""
        for i in range(2, len(state) - 2):
            pattern = state[i - 2:i + 3]
            new_state += self.rules.get(pattern, ".")

        index -= 2
        return new_state, index

    def part1(self) -> int:
        total = 0
        state = self.initial_state
        index = 0

        for generation in range(20):
            state, index = self.simulate_generation(state, index)

        for i, pot in enumerate(state):
            if pot == "#":
                total += (i - index)

        return total

    def part2(self) -> int:
        # it stabilizes after a while, so we can extrapolate the result instead of waiting an eternity
        state = self.initial_state
        index = 0

        previous_total = 0
        previous_difference = 0
        stable_count = 0

        for generation in range(1, 2000):
            state, index = self.simulate_generation(state, index)

            total = 0
            for i, pot in enumerate(state):
                if pot == "#":
                    total += (i - index)

            gen_difference = total - previous_total

            if gen_difference == previous_difference:
                stable_count += 1
                if stable_count > 100: # it has likely stabilized when at lest 100 generations have same total increase
                    remaining = 50_000_000_000 - generation
                    return total + remaining * gen_difference
            else:
                stable_count = 0

            previous_total = total
            previous_difference = gen_difference

        return 0


if __name__ == '__main__':
    Solution().run()
