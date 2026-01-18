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
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())