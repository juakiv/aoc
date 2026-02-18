from copy import deepcopy

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day07", 2018)

        self.rules: dict[str, set[str]] = {}
        for line in self.data:
            parts = line.split()
            self.rules[parts[7]] = self.rules.get(parts[7], set()) | {parts[1]}

            if parts[1] not in self.rules:
                self.rules[parts[1]] = set()

    def part1(self) -> str:
        instruction_order: str = ""
        rules = deepcopy(self.rules)

        while rules:
            next_instruction = sorted([key for key, value in rules.items() if not value])[0]
            instruction_order += next_instruction

            del rules[next_instruction]

            for rule in rules.values():
                rule.discard(next_instruction)

        return instruction_order

    def part2(self) -> int:
        total_time: int = 0
        rules = deepcopy(self.rules)

        worker_count = 2 if self.is_test else 5
        base_time = 0 if self.is_test else 60

        active_workers: dict[str, int] = {}

        while rules or active_workers:
            available_tasks = sorted([task for task, dependencies in rules.items() if not dependencies and task not in active_workers])

            for task in available_tasks:
                if len(active_workers) < worker_count:
                    duration = base_time + (ord(task) - ord("A") + 1)
                    active_workers[task] = duration
                    del rules[task]

            total_time += 1
            finished_now = []

            for task in list(active_workers.keys()):
                active_workers[task] -= 1
                if active_workers[task] == 0:
                    finished_now.append(task)

            for task in finished_now:
                del active_workers[task]
                for remaining_deps in rules.values():
                    remaining_deps.discard(task)

        return total_time


if __name__ == '__main__':
    Solution().run()
