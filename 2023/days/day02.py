from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day02", 2023)

        self.games: dict[int, list[dict[str, int]]] = {}
        for line in self.data:
            game, subsets = line.split(": ")
            game_id = int(game.replace("Game ", ""))
            self.games[game_id] = []

            for subset in subsets.split("; "):
                parts = subset.split(", ")
                subset_dict = {}
                for part in parts:
                    count, color = part.split(" ")
                    subset_dict[color] = int(count)

                self.games[game_id].append(subset_dict)

    def part1(self) -> int:
        valid_game_id_sum: int = 0

        for game_id, subsets in self.games.items():
            is_valid_game = True

            for subset in subsets:
                red_cubes = subset.get("red", 0)
                green_cubes = subset.get("green", 0)
                blue_cubes = subset.get("blue", 0)

                if red_cubes > 12 or green_cubes > 13 or blue_cubes > 14:
                    is_valid_game = False
                    break

            if is_valid_game:
                valid_game_id_sum += game_id

        return valid_game_id_sum

    def part2(self) -> int:
        total_game_power: int = 0

        for subsets in self.games.values():
            min_red_cubes: int = 0
            min_green_cubes: int = 0
            min_blue_cubes: int = 0

            for subset in subsets:
                red_cubes = subset.get("red", 0)
                green_cubes = subset.get("green", 0)
                blue_cubes = subset.get("blue", 0)

                min_red_cubes = max(min_red_cubes, red_cubes)
                min_green_cubes = max(min_green_cubes, green_cubes)
                min_blue_cubes = max(min_blue_cubes, blue_cubes)

            total_game_power += min_red_cubes * min_green_cubes * min_blue_cubes

        return total_game_power


if __name__ == '__main__':
    Solution().run()
