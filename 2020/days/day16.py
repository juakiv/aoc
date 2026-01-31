from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day16", 2020, "\n\n")

        self.rules = {}
        for line in self.data[0].split("\n"):
            field, ranges = line.split(": ")
            range_parts = ranges.split(" or ")
            self.rules[field] = []
            for part in range_parts:
                start, end = map(int, part.split("-"))
                self.rules[field].append((start, end))
        self.your_ticket = self.data[1].split("\n")[1].split(",")
        self.nearby_tickets = [list(map(int, line.split(","))) for line in self.data[2].split("\n")[1:]]

    def part1(self) -> int:
        error_rate = 0

        for ticket in self.nearby_tickets:
            for value in ticket:
                value = int(value)
                valid = False

                for ranges in self.rules.values():
                    for start, end in ranges:
                        if start <= value <= end:
                            valid = True
                            break

                    if valid:
                        break

                if not valid:
                    error_rate += value

        return error_rate

    def part2(self) -> int:
        valid_tickets = []
        for ticket in self.nearby_tickets:
            ticket_valid = True
            for value in ticket:
                value = int(value)
                valid = False

                for ranges in self.rules.values():
                    for start, end in ranges:
                        if start <= value <= end:
                            valid = True
                            break

                    if valid:
                        break

                if not valid:
                    ticket_valid = False
                    break

            if ticket_valid:
                valid_tickets.append(ticket)

        possible_fields = {field: set(range(len(self.your_ticket))) for field in self.rules.keys()}
        for ticket in valid_tickets:
            for index, value in enumerate(ticket):
                value = int(value)
                for field, ranges in self.rules.items():
                    valid = False
                    for start, end in ranges:
                        if start <= value <= end:
                            valid = True
                            break
                    if not valid and index in possible_fields[field]:
                        possible_fields[field].remove(index)

        field_mapping = {}
        while len(possible_fields) > 0:
            for field, possibilities in list(possible_fields.items()):
                if len(possibilities) == 1:
                    index = possibilities.pop()
                    field_mapping[field] = index
                    del possible_fields[field]
                    for other_field in possible_fields.keys():
                        possible_fields[other_field].discard(index)
                    break

        result = 1
        for field, index in field_mapping.items():
            if field.startswith("departure"):
                result *= int(self.your_ticket[index])

        return result


if __name__ == '__main__':
    Solution().run()
