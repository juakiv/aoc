from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day13", 2018)

    def simulate(self, find_last: bool) -> str:
        grid = [list(line) for line in self.data]
        carts = []

        directions = {"^": 0, ">": 1, "v": 2, "<": 3}
        delta_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for y, row in enumerate(grid):
            for x, char in enumerate(row):
                if char in directions:
                    carts.append([y, x, directions[char], 0, True])
                    grid[y][x] = "|" if char in "^v" else "-"

        while True:
            carts.sort()

            active_carts = [c for c in carts if c[4]]
            if find_last and len(active_carts) <= 1:
                return f"{active_carts[0][1]},{active_carts[0][0]}"

            for i in range(len(carts)):
                if not carts[i][4]:
                    continue

                y, x, direction, state, _ = carts[i]
                dy, dx = delta_directions[direction]
                new_y, new_x = y + dy, x + dx

                collision_index = -1
                for j in range(len(carts)):
                    if i != j and carts[j][4] and carts[j][0] == new_y and carts[j][1] == new_x:
                        collision_index = j
                        break

                if collision_index != -1:
                    if not find_last:
                        return f"{new_x},{new_y}"

                    carts[i][4] = False
                    carts[collision_index][4] = False
                    continue

                carts[i][0], carts[i][1] = new_y, new_x
                track = grid[new_y][new_x]

                if track == "/":
                    carts[i][2] = {0: 1, 1: 0, 2: 3, 3: 2}[carts[i][2]]
                elif track == "\\":
                    carts[i][2] = {0: 3, 3: 0, 1: 2, 2: 1}[carts[i][2]]
                elif track == "+":
                    if state == 0:
                        carts[i][2] = (carts[i][2] - 1) % 4
                    elif state == 2:
                        carts[i][2] = (carts[i][2] + 1) % 4
                    carts[i][3] = (state + 1) % 3

            if find_last: # remove crashed carts
                carts = [cart for cart in carts if cart[4]]

    def part1(self) -> str:
        return self.simulate(False)

    def part2(self) -> str:
        return self.simulate(True)


if __name__ == '__main__':
    Solution().run()
