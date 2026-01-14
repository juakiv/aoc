from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day09", 2022)

        self.instructions: list[tuple[str, int]] = []
        for line in self.data:
            direction, steps = line.split()
            self.instructions.append((direction, int(steps)))

    def part1(self) -> int:
        tail_visited: set[tuple[int, int]] = {(0, 0)}
        head_pos = (0, 0)
        tail_pos = (0, 0)

        direction_offsets = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1),
        }

        for direction, steps in self.instructions:
            for _ in range(steps):
                head_pos = (head_pos[0] + direction_offsets[direction][0], head_pos[1] + direction_offsets[direction][1])

                tail_distance_x = head_pos[0] - tail_pos[0]
                tail_distance_y = head_pos[1] - tail_pos[1]

                if abs(tail_distance_x) > 1 or abs(tail_distance_y) > 1:
                    if tail_distance_x != 0:
                        tail_pos = (tail_pos[0] + (1 if tail_distance_x > 0 else -1), tail_pos[1])
                    if tail_distance_y != 0:
                        tail_pos = (tail_pos[0], tail_pos[1] + (1 if tail_distance_y > 0 else -1))

                tail_visited.add(tail_pos)

        return len(tail_visited)

    def part2(self) -> int:
        tail_visited: set[tuple[int, int]] = {(0, 0)}
        knot_positions = [(0, 0) for _ in range(10)]
        direction_offsets = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, 1),
            "D": (0, -1),
        }

        for direction, steps in self.instructions:
            for _ in range(steps):
                knot_positions[0] = (knot_positions[0][0] + direction_offsets[direction][0], knot_positions[0][1] + direction_offsets[direction][1])

                for i in range(1, 10):
                    head_pos = knot_positions[i - 1]
                    tail_pos = knot_positions[i]

                    tail_distance_x = head_pos[0] - tail_pos[0]
                    tail_distance_y = head_pos[1] - tail_pos[1]

                    if abs(tail_distance_x) > 1 or abs(tail_distance_y) > 1:
                        if tail_distance_x != 0:
                            tail_pos = (tail_pos[0] + (1 if tail_distance_x > 0 else -1), tail_pos[1])
                        if tail_distance_y != 0:
                            tail_pos = (tail_pos[0], tail_pos[1] + (1 if tail_distance_y > 0 else -1))

                    knot_positions[i] = tail_pos

                tail_visited.add(knot_positions[9])
        return len(tail_visited)


if __name__ == '__main__':
    Solution().run()
