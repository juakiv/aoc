from solution.base import SolutionBase
from solution.extras.intcode_computer import IntcodeComputer


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day17", 2019)
        self.nums: list[int] = [int(x) for x in self.data[0].split(",")]

    @staticmethod
    def format_map(input_: list[int]) -> tuple[list[list[str]], str, tuple[int, int]]:
        output: list[list[str]] = [[]]
        robot_dir = ""
        robot_position = (0, 0)

        for x in input_:
            if x == 10:
                output.append([])
            else:
                output[-1].append(chr(x))

                if chr(x) in "^>v<":
                    robot_dir = chr(x)
                    robot_position = (len(output[-1]) - 1, len(output) - 1)

        output = [x for x in output if x]
        return output, robot_dir, robot_position

    def part1(self) -> int:
        computer = IntcodeComputer(self.nums).run_full()
        output, _, _ = self.format_map(computer)

        intersections = set()

        for y in range(1, len(output) - 1):
            for x in range(1, len(output[y]) - 1):
                if output[y][x] == "#" and output[y - 1][x] == "#" and output[y + 1][x] == "#" and output[y][x - 1] == "#" and output[y][x + 1] == "#":
                    intersections.add((x, y))

        alignment_parameters = [x * y for x, y in intersections]
        return sum(alignment_parameters)

    def compress_path(self, remaining_path: str, patterns: list[str]) -> list[str] | None:
        if not remaining_path:
            return patterns

        if len(patterns) == 3:
            return None

        path_list = remaining_path.split(",")
        for i in range(1, len(path_list)):
            candidate = ",".join(path_list[:i])
            if len(candidate) > 20:
                break

            next_path = remaining_path.replace(candidate, "").strip(",")
            while ",," in next_path:
                next_path = next_path.replace(",,", ",")

            res = self.compress_path(next_path, patterns + [candidate])
            if res:
                return res
        return None

    def part2(self) -> int:
        nums = self.nums.copy()
        nums[0] = 2

        computer = IntcodeComputer(nums).run_full()
        output_map, robot_direction, (robot_x, robot_y) = self.format_map(computer)

        scaffolds = { (x, y) for y, row in enumerate(output_map) for x, col in enumerate(row) if col == "#" }
        directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
        dx, dy = directions[robot_direction]

        full_path = []
        while True:
            steps = 0

            while (robot_x + dx, robot_y + dy) in scaffolds:
                robot_x += dx
                robot_y += dy
                steps += 1
            if steps > 0:
                full_path.append(str(steps))

            if (robot_x + dy, robot_y - dx) in scaffolds:
                full_path.append("L")
                dx, dy = dy, -dx

            elif (robot_x - dy, robot_y + dx) in scaffolds:
                full_path.append("R")
                dx, dy = -dy, dx

            else:
                break

        path_str = ",".join(full_path)

        a, b, c = self.compress_path(path_str, [])
        main_routine = path_str.replace(a, "A").replace(b, "B").replace(c, "C")
        final_input_str = "\n".join([main_routine, a, b, c, "n"]) + "\n"
        final_input_ascii = [ord(char) for char in final_input_str]

        bot = IntcodeComputer(nums, final_input_ascii).run_full()
        return bot[-1]

if __name__ == '__main__':
    Solution().run()
