from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day22", 2023)

    def get_stable_bricks(self):
        bricks = []
        lowest_y = None

        for left, right in [row.split("~") for row in self.data]:
            start = [int(coord) for coord in left.split(",")]
            end = [int(coord) for coord in right.split(",")]
            brick = {
                "start": start,
                "end": end,
                "floor": min(start[2], end[2]),
                "height": abs(start[2] - end[2]),
                "supporting": [],
                "supported_by": []
            }
            bricks.append(brick)
            if lowest_y is None or lowest_y > brick["floor"]:
                lowest_y = brick["floor"]

        bricks = sorted(bricks, key=lambda b: b["floor"], reverse=True)

        stable_bricks = []
        while bricks:
            brick = bricks.pop()
            if brick["floor"] == lowest_y:
                stable_bricks.append(brick)
            else:
                supporting = []
                supporting_level = 0
                for stable_brick in stable_bricks:
                    if stable_brick["start"][0] <= brick["end"][0] and brick["start"][0] <= stable_brick["end"][0] and \
                            stable_brick["start"][1] <= brick["end"][1] and brick["start"][1] <= stable_brick["end"][1]:
                        top = stable_brick["floor"] + stable_brick["height"]
                        if top > supporting_level:
                            supporting_level = top
                            supporting = []
                        if top == supporting_level:
                            supporting.append(stable_brick)

                brick["supported_by"] = supporting
                brick["floor"] = supporting_level + 1
                stable_bricks.append(brick)

                for supporting_brick in supporting:
                    supporting_brick["supporting"].append(brick)

        return stable_bricks

    def part1(self) -> int:
        stable_bricks = self.get_stable_bricks()
        count = 0
        for stable_brick in stable_bricks:
            if len(stable_brick["supporting"]) > 0:
                if sum([1 for stable in stable_brick["supporting"] if len(stable["supported_by"]) > 1]) == len(stable_brick["supporting"]):
                    count += 1
            else:
                count += 1

        return count

    def part2(self) -> int:
        stable_bricks = self.get_stable_bricks()
        count = 0

        for stable_brick in stable_bricks:
            falling_bricks = [supporting for supporting in stable_brick["supporting"] if len(supporting["supported_by"]) == 1]
            fallen_bricks = []

            while falling_bricks:
                falling_brick = falling_bricks.pop()
                if falling_brick not in falling_bricks:
                    fallen_bricks.append(falling_brick)

                for supporting in falling_brick["supporting"]:
                    if all(any(supported is fb for fb in fallen_bricks) for supported in supporting["supported_by"]):
                        falling_bricks.append(supporting)

            count += len(fallen_bricks)

        return count


if __name__ == '__main__':
    Solution().run()
