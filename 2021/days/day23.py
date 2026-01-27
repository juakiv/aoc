from functools import lru_cache
from heapq import heappop, heappush

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day23", 2021)

        self.rooms = [
            (self.data[2][3], self.data[3][3]),
            (self.data[2][5], self.data[3][5]),
            (self.data[2][7], self.data[3][7]),
            (self.data[2][9], self.data[3][9]),
        ]

        self.start_state = (('.',) * 11, tuple(self.rooms))

    @lru_cache(maxsize=None)
    def is_done(self, state) -> bool:
        hallway, rooms = state
        for i, room in enumerate(rooms):
            if any(amphipod != "ABCD"[i] for amphipod in room):
                return False
        return True

    @staticmethod
    def get_moves(state: tuple, room_depth: int = 2) -> list:
        hallway, rooms = state
        result = []

        room_positions = [2, 4, 6, 8]
        costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
        hall_positions = [0, 1, 3, 5, 7, 9, 10]

        for i, amphipod in enumerate(hallway):
            if amphipod == ".":
                continue

            r = "ABCD".index(amphipod)
            room = rooms[r]

            if any(p != "." and p != amphipod for p in room):
                continue

            step = 1 if room_positions[r] > i else -1
            for j in range(i + step, room_positions[r] + step, step):
                if hallway[j] != '.':
                    break
            else:
                for d in reversed(range(room_depth)):
                    if room[d] == '.':
                        dist = abs(i - room_positions[r]) + d + 1
                        cost = dist * costs[amphipod]

                        new_hall = list(hallway)
                        new_hall[i] = '.'
                        new_rooms = [list(x) for x in rooms]
                        new_rooms[r][d] = amphipod

                        result.append((cost, (tuple(new_hall), tuple(tuple(x) for x in new_rooms))))
                        break

        for r in range(4):
            room = rooms[r]

            if all(p == "." or p == room_positions[r] for p in room):
                continue

            for d in range(room_depth):
                if room[d] != ".":
                    amphipod = room[d]
                    break
            else:
                continue

            for h in hall_positions:
                step = 1 if h > room_positions[r] else -1
                for j in range(room_positions[r] + step, h + step, step):
                    if hallway[j] != ".":
                        break
                else:
                    dist = abs(h - room_positions[r]) + d + 1
                    cost = dist * costs[amphipod]

                    new_hall = list(hallway)
                    new_hall[h] = amphipod
                    new_rooms = [list(x) for x in rooms]
                    new_rooms[r][d] = "."

                    result.append((cost, (tuple(new_hall), tuple(tuple(x) for x in new_rooms))))

        return result

    def part1(self) -> int:
        queue = [(0, self.start_state)]
        seen = set()

        while queue:
            cost, state = heappop(queue)

            if state in seen:
                continue

            seen.add(state)

            if self.is_done(state):
                return cost

            for move_cost, new_state in self.get_moves(state, 2):
                heappush(queue, (cost + move_cost, new_state))

        return 0

    def part2(self) -> int:
        new_start_rooms = [
            (self.rooms[0][0], "D", "D", self.rooms[0][1]),
            (self.rooms[1][0], "C", "B", self.rooms[1][1]),
            (self.rooms[2][0], "B", "A", self.rooms[2][1]),
            (self.rooms[3][0], "A", "C", self.rooms[3][1]),
        ]
        new_start_state = (('.',) * 11, tuple(new_start_rooms))

        queue = [(0, new_start_state)]
        seen = set()

        while queue:
            cost, state = heappop(queue)

            if state in seen:
                continue

            seen.add(state)

            if self.is_done(state):
                return cost

            for move_cost, new_state in self.get_moves(state, 4):
                heappush(queue, (cost + move_cost, new_state))

        return 0


if __name__ == '__main__':
    Solution().run()
