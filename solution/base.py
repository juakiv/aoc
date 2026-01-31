class SolutionBase:
    def __init__(self):
        self.is_test = False

    def load_data(self, file: str, year: int = 2024, split = "\n") -> list:
        if "test" in file:
            self.is_test = True

        with open(f"../../{year}/inputs/{file}.txt", 'r') as f:
            return [line.rstrip() for line in f.read().split(split)]

    def part1(self) -> int | str:
        raise NotImplementedError

    def part2(self) -> int | str:
        raise NotImplementedError

    def run(self):
        print(f"\033[{31 if self.is_test else 32}m\033[1m\033[4m--- RUNNING USING {"TEST" if self.is_test else "REAL"} INPUT ---\033[0m")
        print("\033[1mPart 1:\033[0m", self.part1())
        print("\033[1mPart 2:\033[0m", self.part2())