class IntcodeComputer:
    def __init__(self, nums: list[int], input_values: list[int]):
        self.nums = nums
        self.input_values = input_values or []
        self.i = 0
        self.outputs = []
        self.halted = False
        self.waiting = False

    def run(self):
        self.waiting = False

        while True:
            instruction = self.nums[self.i]
            opcode = instruction % 100
            mode1 = (instruction // 100) % 10
            mode2 = (instruction // 1000) % 10

            if opcode == 99:
                self.halted = True
                return self.outputs

            if opcode == 1:
                a = self.nums[self.nums[self.i + 1]] if mode1 == 0 else self.nums[self.i + 1]
                b = self.nums[self.nums[self.i + 2]] if mode2 == 0 else self.nums[self.i + 2]
                self.nums[self.nums[self.i + 3]] = a + b
                self.i += 4

            elif opcode == 2:
                a = self.nums[self.nums[self.i + 1]] if mode1 == 0 else self.nums[self.i + 1]
                b = self.nums[self.nums[self.i + 2]] if mode2 == 0 else self.nums[self.i + 2]
                self.nums[self.nums[self.i + 3]] = a * b
                self.i += 4

            elif opcode == 3:
                if not self.input_values:
                    self.waiting = True
                    return self.outputs
                self.nums[self.nums[self.i + 1]] = self.input_values.pop(0)
                self.i += 2

            elif opcode == 4:
                value = self.nums[self.nums[self.i + 1]] if mode1 == 0 else self.nums[self.i + 1]
                self.outputs.append(value)
                self.i += 2
                return self.outputs

            elif opcode == 5:
                a = self.nums[self.nums[self.i + 1]] if mode1 == 0 else self.nums[self.i + 1]
                b = self.nums[self.nums[self.i + 2]] if mode2 == 0 else self.nums[self.i + 2]
                self.i = b if a != 0 else self.i + 3

            elif opcode == 6:
                a = self.nums[self.nums[self.i + 1]] if mode1 == 0 else self.nums[self.i + 1]
                b = self.nums[self.nums[self.i + 2]] if mode2 == 0 else self.nums[self.i + 2]
                self.i = b if a == 0 else self.i + 3

            elif opcode == 7:
                a = self.nums[self.nums[self.i + 1]] if mode1 == 0 else self.nums[self.i + 1]
                b = self.nums[self.nums[self.i + 2]] if mode2 == 0 else self.nums[self.i + 2]
                self.nums[self.nums[self.i + 3]] = 1 if a < b else 0
                self.i += 4

            elif opcode == 8:
                a = self.nums[self.nums[self.i + 1]] if mode1 == 0 else self.nums[self.i + 1]
                b = self.nums[self.nums[self.i + 2]] if mode2 == 0 else self.nums[self.i + 2]
                self.nums[self.nums[self.i + 3]] = 1 if a == b else 0
                self.i += 4

    def run_full(self):
        while not self.halted:
            self.run()
        return self.outputs
