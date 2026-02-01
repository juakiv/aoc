import math
from collections import defaultdict

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day20", 2020, "\n\n")

        self.pieces: dict[int, list[list[str]]] = {}
        for piece in self.data:
            lines = piece.split("\n")
            piece_id = int(lines[0].split()[1][:-1])
            self.pieces[piece_id] = [list(line) for line in lines[1:]]

    def part1(self) -> int:
        edge_map: dict[str, set[int]] = defaultdict(set)

        for tile_id, tile in self.pieces.items():
            top = "".join(tile[0])
            bottom = "".join(tile[-1])
            left = "".join(row[0] for row in tile)
            right = "".join(row[-1] for row in tile)

            for edge in (top, bottom, left, right):
                edge_map[edge].add(tile_id)
                edge_map[edge[::-1]].add(tile_id)

        neighbors: dict[int, set[int]] = defaultdict(set)

        for tiles in edge_map.values():
            if len(tiles) > 1:
                for tile in tiles:
                    neighbors[tile].update(tiles - { tile })

        total = 1
        for tile_id, adj in neighbors.items():
            if len(adj) == 2:
                total *= tile_id

        return total

    def part2(self) -> int:
        all_orientations: dict[int, list[list[list[str]]]] = {}

        # all tile orientations
        for tile_id, tile in self.pieces.items():
            variants = []

            current = tile
            for _ in range(4):
                variants.append(current)
                flipped = [row[::-1] for row in current]
                variants.append(flipped)
                current = [list(row) for row in zip(*current[::-1])]

            all_orientations[tile_id] = variants

        size = int(math.sqrt(len(self.pieces)))
        placed = [[None for _ in range(size)] for _ in range(size)]
        placed_ids = [[None for _ in range(size)] for _ in range(size)]
        used: set[int] = set()

        # backtracking to place tiles
        stack = [(0, 0, iter(all_orientations.items()))]
        while stack:
            row, col, iterator = stack[-1]

            if row == size:
                break

            try:
                tile_id, variants = next(iterator)
            except StopIteration:
                stack.pop()
                if stack:
                    placed_row, placed_col, _ = stack[-1]
                    used.remove(placed_ids[placed_row][placed_col])
                    placed[placed_row][placed_col] = None
                    placed_ids[placed_row][placed_col] = None
                continue

            if tile_id in used:
                continue

            for tile in variants:
                fits = True

                top = "".join(tile[0])
                left = "".join(row[0] for row in tile)

                if row > 0:
                    above = placed[row - 1][col]
                    if "".join(above[-1]) != top:
                        fits = False

                if fits and col > 0:
                    left_tile = placed[row][col - 1]
                    if "".join(row[-1] for row in left_tile) != left:
                        fits = False

                if fits:
                    placed[row][col] = tile
                    placed_ids[row][col] = tile_id
                    used.add(tile_id)

                    nr, nc = row, col + 1
                    if nc == size:
                        nr += 1
                        nc = 0

                    stack.append((nr, nc, iter(all_orientations.items())))
                    break
            else:
                continue

        # combine placed tiles into full image, stripping borders
        image: list[list[str]] = []
        for row in placed:
            stripped_row = []
            for tile in row:
                stripped = [r[1:-1] for r in tile[1:-1]]
                stripped_row.append(stripped)

            for i in range(len(stripped_row[0])):
                combined = []
                for t in stripped_row:
                    combined.extend(t[i])
                image.append(combined)

        # search for sea monsters
        monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
        monster_cells = []
        for row in range(len(monster)):
            for col in range(len(monster[0])):
                if monster[row][col] == "#":
                    monster_cells.append((row, col))

        # all image orientations
        images = []
        current = image
        for _ in range(4):
            images.append(current)
            flipped = [row[::-1] for row in current]
            images.append(flipped)
            current = [list(row) for row in zip(*current[::-1])]

        # find monsters in any orientation
        for img in images:
            found = 0

            for row in range(len(img) - len(monster)):
                for col in range(len(img[0]) - len(monster[0])):
                    ok = True
                    for dr, dc in monster_cells:
                        if img[row + dr][col + dc] != "#":
                            ok = False
                            break
                    if ok:
                        found += 1

            if found:
                total_hash = sum(row.count("#") for row in img)
                return total_hash - found * len(monster_cells)

        return 0


if __name__ == '__main__':
    Solution().run()
