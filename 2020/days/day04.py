from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day04", 2020, "\n\n")

        self.passports: list[dict[str, str]] = []
        for entry in self.data:
            fields = entry.replace("\n", " ").split()
            passport = {}
            for field in fields:
                key, value = field.split(":")
                passport[key] = value
            self.passports.append(passport)

    def part1(self) -> int:
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        valid_passport_count = 0

        for passport in self.passports:
            if required_fields.issubset(set(passport.keys())):
                valid_passport_count += 1

        return valid_passport_count

    def part2(self) -> int:
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
        valid_passport_count = 0

        for passport in self.passports:
            if not required_fields.issubset(set(passport.keys())):
                continue

            if not (1920 <= int(passport["byr"]) <= 2002):
                continue

            if not (2010 <= int(passport["iyr"]) <= 2020):
                continue

            if not (2020 <= int(passport["eyr"]) <= 2030):
                continue

            hgt = passport["hgt"]
            if hgt.endswith("cm"):
                height = int(hgt[:-2])
                if not (150 <= height <= 193):
                    continue
            elif hgt.endswith("in"):
                height = int(hgt[:-2])
                if not (59 <= height <= 76):
                    continue
            else:
                continue

            hcl = passport["hcl"]
            if not (hcl.startswith("#") and len(hcl) == 7 and all(c in "0123456789abcdef" for c in hcl[1:])):
                continue

            ecl = passport["ecl"]
            if ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                continue

            pid = passport["pid"]
            if not (len(pid) == 9 and pid.isdigit()):
                continue

            valid_passport_count += 1

        return valid_passport_count


if __name__ == '__main__':
    Solution().run()
