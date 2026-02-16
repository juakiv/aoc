import re
from collections import defaultdict, Counter

from solution.base import SolutionBase


class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = sorted(self.load_data("day04", 2018))

        self.sleep_stats = defaultdict(list)

        current_guard = None
        sleep_start = 0

        for line in self.data:
            minute = int(re.search(r':(\d+)]', line).group(1))

            if "begins shift" in line:
                current_guard = int(re.search(r'#(\d+)', line).group(1))

            elif "falls asleep" in line:
                sleep_start = minute

            elif "wakes up" in line:
                for m in range(sleep_start, minute):
                    self.sleep_stats[current_guard].append(m)

    def part1(self) -> int:
        sleepless_guard = max(self.sleep_stats, key=lambda k: len(self.sleep_stats[k]))

        minutes_counts = Counter(self.sleep_stats[sleepless_guard])
        most_frequent_minute = minutes_counts.most_common(1)[0][0]

        return sleepless_guard * most_frequent_minute

    def part2(self) -> int:
        best_guard = None
        best_minute = None
        max_sleep = 0

        for guard, minutes in self.sleep_stats.items():
            if not minutes:
                continue

            minute, count = Counter(minutes).most_common(1)[0]

            if count > max_sleep:
                max_sleep = count
                best_guard = guard
                best_minute = minute

        return best_guard * best_minute


if __name__ == '__main__':
    Solution().run()
