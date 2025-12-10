from collections import deque

import scipy

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day10", 2025)

        self.machines = []

        for line in self.data:
            machine_components = line.split(" ")
            lights = [True if x == "#" else False for x in machine_components[0][1:-1]]
            buttons = [[int(button_num) for button_num in button[1:-1].split(",")] for button in machine_components[1:-1]]
            joltages = [int(x) for x in machine_components[-1][1:-1].split(",")]

            self.machines.append([lights, buttons, joltages])

    @staticmethod
    def part1_bfs(lights, buttons) -> int | None:
        target_state = tuple(lights)
        current_state = tuple(False for _ in lights)

        queue = deque([current_state])
        visited = { current_state: 0 }

        while queue:
            current_state = queue.popleft()
            times_pressed = visited[current_state] + 1

            for button in buttons:
                next_state = tuple(not current_state[i] if i in button else current_state[i] for i in range(len(lights)))
                if next_state not in visited:
                    if next_state == target_state:
                        return times_pressed
                    visited[next_state] = times_pressed
                    queue.append(next_state)
        return None

    def part1(self) -> int:
        total_button_presses = 0

        for machine in self.machines:
            total_button_presses += self.part1_bfs(machine[0], machine[1])

        return total_button_presses

    def part2(self) -> int:
        total_button_presses = 0

        for machine in self.machines:
            buttons = [[int(i in button) for i in range(len(machine[0]))] for button in machine[1]]
            total_button_presses += int(scipy.optimize.linprog(c=[1] * len(buttons), A_eq=list(map(list, zip(*buttons))), b_eq=machine[2], integrality=1).fun)

        return total_button_presses


if __name__ == '__main__':
    Solution().run()
