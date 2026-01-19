import re
from functools import lru_cache

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day19", 2022)

        self.costs = []
        for line in self.data:
            costs = re.findall(r"(\d+)", line)
            self.costs.append(list(map(int, costs)))

    @staticmethod
    def max_geodes(blueprint: list[int], max_time: int = 24) -> int:
        blueprint_id, ore_cost, clay_cost, obsidian_ore_cost, obsidian_clay_cost, geode_ore_cost, geode_obsidian_cost = blueprint
        max_ore_cost = max(ore_cost, clay_cost, obsidian_ore_cost, geode_ore_cost)

        @lru_cache(None)
        def dfs(time: int, ore: int, clay: int, obsidian: int, ore_robots: int, clay_robots: int, obsidian_robots: int, geode_robots: int) -> int:
            if time == 0:
                return 0

            ore = min(ore, time * max_ore_cost - ore_robots * (time - 1))
            clay = min(clay, time * obsidian_clay_cost - clay_robots * (time - 1))
            obsidian = min(obsidian, time * geode_obsidian_cost - obsidian_robots * (time - 1))

            result = 0

            # build geode rboot
            if ore >= geode_ore_cost and obsidian >= geode_obsidian_cost:
                return geode_robots + dfs(
                    time - 1,
                    ore - geode_ore_cost + ore_robots,
                    clay + clay_robots,
                    obsidian - geode_obsidian_cost + obsidian_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots,
                    geode_robots + 1
                )

            # build obsidian robot
            if ore >= obsidian_ore_cost and clay >= obsidian_clay_cost and obsidian_robots < geode_obsidian_cost:
                result = max(result, geode_robots + dfs(
                    time - 1,
                    ore - obsidian_ore_cost + ore_robots,
                    clay - obsidian_clay_cost + clay_robots,
                    obsidian + obsidian_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots + 1,
                    geode_robots
                ))

            # build clay robot
            if ore >= clay_cost and clay_robots < obsidian_clay_cost:
                result = max(result, geode_robots + dfs(
                    time - 1,
                    ore - clay_cost + ore_robots,
                    clay + clay_robots,
                    obsidian + obsidian_robots,
                    ore_robots,
                    clay_robots + 1,
                    obsidian_robots,
                    geode_robots
                ))

            # build ore robot
            if ore >= ore_cost and ore_robots < max_ore_cost:
                result = max(result, geode_robots + dfs(
                    time - 1,
                    ore - ore_cost + ore_robots,
                    clay + clay_robots,
                    obsidian + obsidian_robots,
                    ore_robots + 1,
                    clay_robots,
                    obsidian_robots,
                    geode_robots
                ))

            # build nothing
            result = max(result, geode_robots + dfs(
                time - 1,
                ore + ore_robots,
                clay + clay_robots,
                obsidian + obsidian_robots,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots
            ))

            return result

        return dfs(max_time, 0, 0, 0, 1, 0, 0, 0)

    def part1(self) -> int:
        quality_level = 0

        for blueprint in self.costs:
            max_geodes = self.max_geodes(blueprint)
            quality_level += blueprint[0] * max_geodes

        return quality_level

    def part2(self) -> int:
        return self.max_geodes(self.costs[0], 32) * self.max_geodes(self.costs[1], 32) * self.max_geodes(self.costs[2], 32)


if __name__ == '__main__':
    Solution().run()
