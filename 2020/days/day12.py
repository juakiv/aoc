from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day12", 2020)

        self.instructions: list[tuple[str, int]] = []
        for line in self.data:
            action = line[0]
            value = int(line[1:])
            self.instructions.append((action, value))

    def part1(self) -> int:
        x, y = 0, 0
        directions = ["east", "south", "west", "north"]
        facing = 0

        for instruction in self.instructions:
            action, value = instruction

            if action == "N":
                y += value
            elif action == "S":
                y -= value
            elif action == "E":
                x += value
            elif action == "W":
                x -= value
            elif action == "L":
                facing = (facing - value // 90) % 4
            elif action == "R":
                facing = (facing + value // 90) % 4
            elif action == "F":
                if directions[facing] == "north":
                    y += value
                elif directions[facing] == "south":
                    y -= value
                elif directions[facing] == "east":
                    x += value
                elif directions[facing] == "west":
                    x -= value

        return abs(x) + abs(y)

    def part2(self) -> int:
        ship_x, ship_y = 0, 0
        waypoint_x, waypoint_y = 10, 1

        for instruction in self.instructions:
            action, value = instruction

            if action == "N":
                waypoint_y += value
            elif action == "S":
                waypoint_y -= value
            elif action == "E":
                waypoint_x += value
            elif action == "W":
                waypoint_x -= value
            elif action in ["L", "R"]:
                if action == "R":
                    value = 360 - value
                for _ in range(value // 90):
                    waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            elif action == "F":
                ship_x += waypoint_x * value
                ship_y += waypoint_y * value

        return abs(ship_x) + abs(ship_y)


if __name__ == '__main__':
    Solution().run()
