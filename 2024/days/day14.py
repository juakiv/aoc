from typing import Tuple

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day14")

        self.robot_positions: list[Tuple[int, int]] = []
        self.robot_velocities: list[Tuple[int, int]] = []
        self.area_size = (101, 103)

        for line in self.data:
            position, velocity = line.split(" ")
            pos_x, pos_y = position.split("=")[1].split(",")
            vel_x, vel_y = velocity.split("=")[1].split(",")

            self.robot_positions.append((int(pos_x), int(pos_y)))
            self.robot_velocities.append((int(vel_x), int(vel_y)))

    def position_after_time(self, position: Tuple[int, int], velocity: Tuple[int, int], time: int) -> Tuple[int, int]:
        return (position[0] + velocity[0] * time) % self.area_size[0], (position[1] + velocity[1] * time) % self.area_size[1]

    def part1(self) -> int:
        robot_positions_after_time = [self.position_after_time(self.robot_positions[i], self.robot_velocities[i], 100) for i in range(len(self.robot_positions))]

        quadrants = [0, 0, 0, 0]
        middle = (self.area_size[0] // 2, self.area_size[1] // 2)

        for robot in robot_positions_after_time:
            if robot[0] < middle[0] and robot[1] < middle[1]:
                quadrants[0] += 1
            elif robot[0] < middle[0] and robot[1] > middle[1]:
                quadrants[1] += 1
            elif robot[0] > middle[0] and robot[1] < middle[1]:
                quadrants[2] += 1
            elif robot[0] > middle[0] and robot[1] > middle[1]:
                quadrants[3] += 1

        return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

    def print_area(self, robots: list[Tuple[int, int]]) -> None:
        area = [["." for _ in range(self.area_size[0])] for _ in range(self.area_size[1])]

        for robot in robots:
            area[robot[1]][robot[0]] = "#"

        for line in area:
            print("".join(line))

    def get_nearby_robots(self, positions: list[Tuple[int, int]]) -> int:
        nearby_robots = 0
        robot_set = set(positions)

        for y in range(self.area_size[1]):
            for x in range(self.area_size[0]):
                if (x, y) in robot_set and (x + 1, y) in robot_set:
                    nearby_robots += 1

        return nearby_robots

    def part2(self) -> int:
        seconds = 0

        for i in range(10000):
            robot_positions_after_time = [self.position_after_time(self.robot_positions[robot], self.robot_velocities[robot], i) for robot in range(len(self.robot_positions))]
            nearby_robots = self.get_nearby_robots(robot_positions_after_time)

            if nearby_robots > 100:
                seconds = i
                self.print_area(robot_positions_after_time)
                break

        return seconds

if __name__ == '__main__':
    Solution().run()
