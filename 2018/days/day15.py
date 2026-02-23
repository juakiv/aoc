from collections import deque

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day15", 2018)

    @staticmethod
    def resolve_units(grid: list[list[str]], elf_attack: int):
        units = []
        unit_id = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] in ("G", "E"):
                    units.append({ "id": unit_id, "type": grid[row][col], "row": row, "col": col, "hp": 200, "attack": elf_attack if grid[row][col] == "E" else 3, "alive": True })
                    unit_id += 1

        return units

    @staticmethod
    def has_adjacent_enemy(unit, enemies):
        for enemy in enemies:
            if abs(enemy["row"] - unit["row"]) + abs(enemy["col"] - unit["col"]) == 1:
                return True

        return False

    @staticmethod
    def move_unit(unit, enemies, grid, height, width):
        delta_directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        targets = set()

        for enemy in enemies:
            for delta_row, delta_col in delta_directions:
                row = enemy["row"] + delta_row
                col = enemy["col"] + delta_col
                if 0 <= row < height and 0 <= col < width and grid[row][col] == ".":
                    targets.add((row, col))

        if not targets:
            return

        start = (unit["row"], unit["col"])
        queue = deque([(start, 0)])
        visited = { start }

        parents = {}

        min_dist = None
        reachable = []

        while queue:
            (row, col), dist = queue.popleft()

            if min_dist is not None and dist > min_dist:
                break

            if (row, col) in targets:
                min_dist = dist
                reachable.append((row, col))
                continue

            for delta_row, delta_col in delta_directions:
                new_row, new_col = row + delta_row, col + delta_col
                if 0 <= new_row < height and 0 <= new_col < width and (new_row, new_col) not in visited and grid[new_row][new_col] == ".":
                    visited.add((new_row, new_col))
                    parents[(new_row, new_col)] = (row, col)
                    queue.append(((new_row, new_col), dist + 1))

        if not reachable:
            return

        chosen_target = sorted(reachable)[0]
        while parents.get(chosen_target) != start:
            chosen_target = parents[chosen_target]

        grid[unit["row"]][unit["col"]] = "."
        unit["row"], unit["col"] = chosen_target
        grid[unit["row"]][unit["col"]] = unit["type"]

    @staticmethod
    def select_attack_target(unit, enemies):
        adjacent = [enemy for enemy in enemies if abs(enemy["row"] - unit["row"]) + abs(enemy["col"] - unit["col"]) == 1]

        if not adjacent:
            return None

        adjacent.sort(key=lambda e: (e["hp"], e["row"], e["col"]))
        return adjacent[0]

    def simulate(self, elf_attack: int, stop_on_elf_death: bool) -> int:
        grid = [list(row) for row in self.data]
        height = len(grid)
        width = len(grid[0])

        units = self.resolve_units(grid, elf_attack)

        rounds_completed = 0

        while True:
            units.sort(key=lambda unit_: (unit_["row"], unit_["col"]))

            for unit in units:
                if not unit["alive"]:
                    continue

                enemies = [unit_ for unit_ in units if unit_["alive"] and unit_["type"] != unit["type"]]
                if not enemies:
                    total_hp = sum(unit_["hp"] for unit_ in units if unit_["alive"])
                    return rounds_completed * total_hp

                if not self.has_adjacent_enemy(unit, enemies):
                    self.move_unit(unit, enemies, grid, height, width)

                target = self.select_attack_target(unit, enemies)
                if target:
                    target["hp"] -= unit["attack"]
                    if target["hp"] <= 0:
                        if stop_on_elf_death and target["type"] == "E":
                            return -1
                        target["alive"] = False
                        grid[target["row"]][target["col"]] = "."

            rounds_completed += 1

    def part1(self) -> int:
        return self.simulate(3, False)

    def part2(self) -> int:
        attack = 4
        while True:
            result = self.simulate(attack, True)
            if result != -1:
                return result
            attack += 1


if __name__ == '__main__':
    Solution().run()
