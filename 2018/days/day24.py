import re

from solution.base import SolutionBase

class Group:
    def __init__(self, team, count, hp, weaknesses, immunities, damage, damage_type, initiative):
        self.team = team
        self.units = count
        self.hp = hp
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.damage = damage
        self.damage_type = damage_type
        self.initiative = initiative
        self.target = None

    @property
    def effective_power(self):
        return self.units * self.damage

    def calculate_damage_to(self, other):
        if self.damage_type in other.immunities:
            return 0
        damage = self.effective_power
        if self.damage_type in other.weaknesses:
            damage *= 2
        return damage

class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day24", 2018, "\n\n")

    def parse_groups(self, boost: int = 0):
        groups = []

        for block in self.data:
            lines = block.strip().split("\n")
            team = lines[0].replace(":", "")

            for line in lines[1:]:
                count, hp = map(int, re.findall(r"(\d+) units each with (\d+) hit points", line)[0])

                weaknesses = []
                immunities = []

                special = re.search(r"\((.*?)\)", line)
                if special:
                    parts = special.group(1).split("; ")

                    for part in parts:
                        if part.startswith("weak to "):
                            weaknesses = part[8:].split(", ")

                        elif part.startswith("immune to "):
                            immunities = part[10:].split(", ")

                damage, damage_type, initiative = re.findall(r"(\d+) (\w+) damage at initiative (\d+)", line)[0]
                damage = int(damage)
                initiative = int(initiative)

                damage += boost if team == "Immune System" else 0

                groups.append(Group(team, count, hp, weaknesses, immunities, damage, damage_type, initiative))

        return groups

    def run_simulation(self, boost):
        groups = self.parse_groups(boost)

        while True:
            teams_left = set(g.team for g in groups if g.units > 0)
            if len(teams_left) <= 1:
                break

            groups.sort(key=lambda g: (g.effective_power, g.initiative), reverse=True)
            chosen_targets = set()

            for group in groups:
                group.target = None
                if group.units <= 0:
                    continue

                enemies = [e for e in groups if e.team != group.team and e.units > 0 and e not in chosen_targets]
                if not enemies:
                    continue

                best_target = max(enemies, key=lambda e: (group.calculate_damage_to(e), e.effective_power, e.initiative))
                if group.calculate_damage_to(best_target) > 0:
                    group.target = best_target
                    chosen_targets.add(best_target)

            groups.sort(key=lambda g: g.initiative, reverse=True)
            total_killed = 0
            for group in groups:
                if group.units <= 0 or not group.target:
                    continue

                damage = group.calculate_damage_to(group.target)
                killed = min(group.target.units, damage // group.target.hp)
                group.target.units -= killed
                total_killed += killed

            if total_killed == 0:
                return "Draw", 0

            groups = [g for g in groups if g.units > 0]

        winner = groups[0].team if groups else "None"
        total_units = sum(g.units for g in groups)
        return winner, total_units

    def part1(self) -> int:
        winner, total_units = self.run_simulation(0)
        return total_units

    def part2(self) -> int:
        best_boost = 1

        while True:
            winner, total_units = self.run_simulation(best_boost)
            if winner == "Immune System":
                return total_units
            best_boost += 1


if __name__ == '__main__':
    Solution().run()
