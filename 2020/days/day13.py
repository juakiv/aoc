from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day13", 2020)

        self.estimated_departure = int(self.data[0])
        self.bus_ids = [int(x) for x in self.data[1].split(",") if x != "x"]

    def part1(self) -> int:
        earliest = None

        for bus_id in self.bus_ids:
            departure_time = (self.estimated_departure // bus_id + 1) * bus_id
            if earliest is None or departure_time < earliest[0]:
                earliest = (departure_time, bus_id)

        return (earliest[0] - self.estimated_departure) * earliest[1]

    def part2(self) -> int:
        bus_ids_offsets = [(int(bus_id), offset) for offset, bus_id in enumerate(self.data[1].split(",")) if bus_id != "x"]
        timestamp = 0
        step = 1

        for bus_id, offset in bus_ids_offsets:
            while (timestamp + offset) % bus_id != 0:
                timestamp += step
            step *= bus_id

        return timestamp


if __name__ == '__main__':
    Solution().run()
