import math
from itertools import combinations

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day08", 2025)

        self.boxes: list[tuple[int, ...]] = [tuple(map(int, line.split(","))) for line in self.data]
        self.pairs = sorted(combinations(self.boxes, 2), key=lambda x: math.dist(x[0], x[1]))

    def part1(self) -> int:
        circuits: list[set[tuple[int, ...]]] = []

        for i, pair in enumerate(self.pairs):
            if i >= 1000:
                break

            circuit_1, circuit_2= None, None

            for circuit in circuits:
                if pair[0] in circuit:
                    circuit_1 = circuit
                if pair[1] in circuit:
                    circuit_2 = circuit

            # skip if boxes are already in same circuit
            if circuit_1 is not None and circuit_1 == circuit_2:
                continue

            # merge circuits if both boxes are in different circuits
            if circuit_1 and circuit_2:
                circuit_1.update(circuit_2)
                circuits.remove(circuit_2)
            elif circuit_1:
                circuit_1.add(pair[1]) # add second box to first circuit if only first box is in a circuit
            elif circuit_2:
                circuit_2.add(pair[0]) # do the opposite
            else:
                circuits.append(set(pair)) # create new circuit if neither box is in a circuit

        connected_circuits = [circuit for circuit in circuits if len(circuit) > 1]
        for box in self.boxes:
            if box not in connected_circuits:
                circuits.append({ box })

        sorted_circuits_by_size = sorted([len(circuit) for circuit in circuits], reverse=True)
        return sorted_circuits_by_size[0] * sorted_circuits_by_size[1] * sorted_circuits_by_size[2]

    def part2(self) -> int:
        circuits: list[set[tuple[int, ...]]] = []
        final_circuit_mult = 0

        for i, pair in enumerate(self.pairs):

            circuit_1, circuit_2 = None, None

            for circuit in circuits:
                if pair[0] in circuit:
                    circuit_1 = circuit
                if pair[1] in circuit:
                    circuit_2 = circuit

            if circuit_1 is not None and circuit_1 == circuit_2:
                continue

            if circuit_1 and circuit_2:
                circuit_1.update(circuit_2)
                circuits.remove(circuit_2)
            elif circuit_1:
                circuit_1.add(pair[1])
            elif circuit_2:
                circuit_2.add(pair[0])
            else:
                circuits.append(set(pair))

            final_circuit_mult = pair[0][0] * pair[1][0]

        return final_circuit_mult


if __name__ == '__main__':
    Solution().run()
