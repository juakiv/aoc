from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day05", 2020)

        self.boarding_passes: list[str] = [line for line in self.data]

    @staticmethod
    def calculate_seat_number(boarding_pass: str) -> int:
        row_part = boarding_pass[:7]
        col_part = boarding_pass[7:]

        row_binary = row_part.replace("F", "0").replace("B", "1")
        col_binary = col_part.replace("L", "0").replace("R", "1")

        row = int(row_binary, 2)
        col = int(col_binary, 2)

        seat_id = row * 8 + col
        return seat_id

    def part1(self) -> int:
        max_seat_id = 0

        for boarding_pass in self.boarding_passes:
            seat_id = self.calculate_seat_number(boarding_pass)

            if seat_id > max_seat_id:
                max_seat_id = seat_id

        return max_seat_id

    def part2(self) -> int:
        seat_ids = set()
        for boarding_pass in self.boarding_passes:
            seat_id = self.calculate_seat_number(boarding_pass)
            seat_ids.add(seat_id)

        for seat_id in range(min(seat_ids), max(seat_ids)):
            if seat_id not in seat_ids:
                return seat_id

        return 0


if __name__ == '__main__':
    Solution().run()
