from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day17", 2021)[0]

        self.target = {}
        parts = self.data.replace("target area: ", "").split(", ")
        for part in parts:
            axis, ranges = part.split("=")
            start, end = map(int, ranges.split(".."))
            self.target[axis] = (start, end)

    def run_step(self, position: tuple[int, int], velocity: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
        x, y = position
        vx, vy = velocity

        x += vx
        y += vy

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        return (x, y), (vx, vy)

    def part1(self) -> int:
        highest_y = 0

        for initial_vx in range(1, self.target["x"][1] + 1):
            for initial_vy in range(self.target["y"][0], abs(self.target["y"][0]) + 1):
                position = (0, 0)
                velocity = (initial_vx, initial_vy)
                current_highest_y = 0

                while position[0] <= self.target["x"][1] and position[1] >= self.target["y"][0]:
                    position, velocity = self.run_step(position, velocity)
                    current_highest_y = max(current_highest_y, position[1])

                    if (self.target["x"][0] <= position[0] <= self.target["x"][1] and
                        self.target["y"][0] <= position[1] <= self.target["y"][1]):
                        highest_y = max(highest_y, current_highest_y)
                        break

        return highest_y

    def part2(self) -> int:
        valid_initial_velocities = set()

        for initial_vx in range(1, self.target["x"][1] + 1):
            for initial_vy in range(self.target["y"][0], abs(self.target["y"][0]) + 1):
                position = (0, 0)
                velocity = (initial_vx, initial_vy)

                while position[0] <= self.target["x"][1] and position[1] >= self.target["y"][0]:
                    position, velocity = self.run_step(position, velocity)

                    if (self.target["x"][0] <= position[0] <= self.target["x"][1] and
                        self.target["y"][0] <= position[1] <= self.target["y"][1]):
                        valid_initial_velocities.add((initial_vx, initial_vy))
                        break

        return len(valid_initial_velocities)


if __name__ == '__main__':
    Solution().run()
