from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day21", 2020)

        self.foods: list[tuple[set[str], set[str]]] = []
        self.allergens_to_ingredients: dict[str, set[str]] = {}
        self.ingredient_counts: defaultdict[str, int] = defaultdict(int)

        for line in self.data:
            ingredients_part, allergens_part = line.split(" (contains ")
            ingredients = set(ingredients_part.split(" "))
            allergens = set(allergens_part[:-1].split(", "))
            self.foods.append((ingredients, allergens))

            for ingredient in ingredients:
                self.ingredient_counts[ingredient] += 1

            for allergen in allergens:
                if allergen not in self.allergens_to_ingredients:
                    self.allergens_to_ingredients[allergen] = ingredients.copy()
                else:
                    self.allergens_to_ingredients[allergen] &= ingredients

    def part1(self) -> int:
        possible_allergenic_ingredients = set()
        for ingredients in self.allergens_to_ingredients.values():
            possible_allergenic_ingredients |= ingredients

        non_allergenic_ingredients = set(self.ingredient_counts.keys()) - possible_allergenic_ingredients
        return sum(self.ingredient_counts[ingredient] for ingredient in non_allergenic_ingredients)

    def part2(self) -> str:
        confirmed_allergens: dict[str, str] = {}
        while len(confirmed_allergens) < len(self.allergens_to_ingredients):
            for allergen, ingredients in self.allergens_to_ingredients.items():
                ingredients -= set(confirmed_allergens.values())
                if len(ingredients) == 1:
                    confirmed_allergens[allergen] = ingredients.pop()

        return ",".join(confirmed_allergens[allergen] for allergen in sorted(confirmed_allergens.keys()))


if __name__ == '__main__':
    Solution().run()
