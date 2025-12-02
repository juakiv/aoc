from solution.base import SolutionBase
from itertools import batched


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02", 2025)[0]

        self.ranges: list[tuple[int, int]] = [(int(_range.split("-")[0]), int(_range.split("-")[1])) for _range in
                                              self.data.split(",")]

    def part1(self) -> int:
        invalid_ids: list[int] = []

        for _range in self.ranges:
            for i in range(_range[0], _range[1] + 1):
                str_id = str(i)
                id_len = len(str_id)
                if id_len % 2 == 0 and str_id[id_len // 2:] == str_id[:id_len // 2]:
                    invalid_ids.append(i)


        return sum(invalid_ids)

    def part2(self) -> int:
        invalid_ids: set[int] = set()

        for _range in self.ranges:
            for i in range(_range[0], _range[1] + 1):
                str_id = str(i)
                id_len = len(str_id)

                for part in range(1, id_len // 2 + 1):
                    if len(set(batched(str_id, part))) == 1:    # if all chunks are the same, it has repeating pattern
                        invalid_ids.add(i)                      # and thus is invalid
                        break

        return sum(invalid_ids)


if __name__ == '__main__':
    Solution().run()
