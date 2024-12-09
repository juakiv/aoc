from typing import Tuple

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09")[0]

        self.uncompressed: list[str] = []
        self.file_starts: list[int] = []
        file_id = 0
        for i in range(len(self.data)):
            if i % 2 == 0:
                self.file_starts.append(len(self.uncompressed))
                for _ in range(int(self.data[i])):
                    self.uncompressed.append(file_id)
                file_id += 1
            else:
                for _ in range(int(self.data[i])):
                    self.uncompressed.append(".")

        self.total_files = file_id

    def part1(self) -> int:
        uncompressed_list = self.uncompressed.copy()

        while "." in uncompressed_list:
            uncompressed_list[uncompressed_list.index(".")] = uncompressed_list.pop()

        return sum([int(x) * i for i, x in enumerate(uncompressed_list)])

    @staticmethod
    def find_first_fitting_gap(uncompressed_list: list[str], file_length: int) -> int | None:
        for i in range(len(uncompressed_list)):
            if uncompressed_list[i] == ".":
                gap_length = 1
                while i + gap_length < len(uncompressed_list) and uncompressed_list[i + gap_length] == ".":
                    gap_length += 1
                if gap_length >= file_length:
                    return i
        return None

    def part2(self) -> int:
        uncompressed_list = self.uncompressed.copy()

        while self.file_starts:
            file_start = self.file_starts.pop()
            file_id = uncompressed_list[file_start]
            file_end = file_start
            while file_end + 1 < len(uncompressed_list) and uncompressed_list[file_end + 1] == file_id:
                file_end += 1

            file_length = file_end - file_start + 1

            first_fitting_gap = self.find_first_fitting_gap(uncompressed_list, file_length)
            if first_fitting_gap is None:
                continue
            elif first_fitting_gap < file_start:
                for i in range(file_length):
                    uncompressed_list[first_fitting_gap + i] = file_id
                    uncompressed_list[file_start + i] = "."

        return sum([int(x) * i for i, x in enumerate(uncompressed_list) if x != "."])


if __name__ == '__main__':
    Solution().run()
