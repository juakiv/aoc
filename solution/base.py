class SolutionBase:
    @staticmethod
    def load_data(file: str, year: int = 2024) -> list:
        with open(f"../../{year}/inputs/{file}.txt", 'r') as f:
            return [line.rstrip() for line in f.readlines()]

    def part1(self) -> int | str:
        raise NotImplementedError

    def part2(self) -> int | str:
        raise NotImplementedError

    def run(self):
        print("Part 1:", self.part1())
        print("Part 2:", self.part2())