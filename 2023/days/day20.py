import math

from solution.base import SolutionBase

class Solution(SolutionBase):
    def __init__(self):
        super().__init__()
        self.data = self.load_data("day20", 2023)

        self.modules = {}

    def reset(self):
        for line in self.data:
            module_name, module_connections = line.split(" -> ")
            module = {
                "name": module_name[1:] if module_name != "broadcaster" else "broadcaster",
                "type": "flipflop" if "%" in module_name else "conjunction" if module_name != "broadcaster" else "broadcaster",
                "destinations": module_connections.split(", "),
                "memory": False if "%" in module_name else {}
            }
            self.modules[module["name"]] = module

        for name, module in self.modules.items():
            for destination in module["destinations"]:
                if destination in self.modules and self.modules[destination]["type"] == "conjunction":
                    self.modules[destination]["memory"][name] = "low"

    def part1(self) -> int:
        self.reset()

        low_pulse_count = 0
        high_pulse_count = 0

        for _ in range(1000):
            low_pulse_count += 1
            queue = [("broadcaster", destination, "low") for destination in self.modules["broadcaster"]["destinations"]]

            while queue:
                source, destination, pulse = queue.pop(0)

                if pulse == "low":
                    low_pulse_count += 1
                else:
                    high_pulse_count += 1

                if destination not in self.modules:
                    continue

                current_module = self.modules[destination]
                if current_module["type"] == "flipflop":
                    if pulse == "low":
                        current_module["memory"] = not current_module["memory"]
                        next_pulse = "high" if current_module["memory"] else "low"
                        for next_destination in current_module["destinations"]:
                            queue.append((current_module["name"], next_destination, next_pulse))

                else:
                    current_module["memory"][source] = pulse
                    next_pulse = "low" if all(pulse == "high" for pulse in current_module["memory"].values()) else "high"
                    for next_destination in current_module["destinations"]:
                        queue.append((current_module["name"], next_destination, next_pulse))

        return low_pulse_count * high_pulse_count

    def part2(self) -> int:
        self.reset()

        final = [module_name for module_name, module in self.modules.items() if "rx" in module["destinations"]]
        second_final = set(module_name for module_name, module in self.modules.items() if final[0] in module["destinations"])

        cycle_lengths = []

        for i in range(10_000):
            queue = [("broadcaster", destination, "low") for destination in self.modules["broadcaster"]["destinations"]]
            while queue:
                source, destination, pulse = queue.pop(0)

                if destination not in self.modules:
                    continue

                current_module = self.modules[destination]
                if current_module["type"] == "flipflop":
                    if pulse == "low":
                        current_module["memory"] = not current_module["memory"]
                        next_pulse = "high" if current_module["memory"] else "low"
                        for next_destination in current_module["destinations"]:
                            queue.append((current_module["name"], next_destination, next_pulse))

                else:
                    current_module["memory"][source] = pulse
                    next_pulse = "low" if all(pulse == "high" for pulse in current_module["memory"].values()) else "high"

                    if current_module["name"] in second_final and next_pulse == "high":
                        cycle_lengths.append(i + 1)
                        second_final.remove(current_module["name"])

                    for next_destination in current_module["destinations"]:
                        queue.append((current_module["name"], next_destination, next_pulse))

            if not second_final:
                break

        return math.lcm(*cycle_lengths)


if __name__ == '__main__':
    Solution().run()
