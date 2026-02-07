class IntcodeComputer:
    def __init__(self, nums: list[int], input_values: list[int] | None = None):
        self.memory = { i: v for i, v in enumerate(nums) }
        self.input_values = input_values or []
        self.i = 0
        self.relative_base = 0
        self.outputs = []
        self.halted = False
        self.waiting = False

    def read(self, addr: int) -> int:
        return self.memory.get(addr, 0)

    def write(self, addr: int, value: int):
        self.memory[addr] = value

    def param(self, offset: int, mode: int) -> int:
        if mode == 0:
            return self.read(self.read(self.i + offset))
        elif mode == 1:
            return self.read(self.i + offset)
        elif mode == 2:
            return self.read(self.relative_base + self.read(self.i + offset))
        else:
            raise ValueError(f"Unknown mode {mode}")

    def address(self, offset: int, mode: int) -> int:
        if mode == 0:
            return self.read(self.i + offset)
        elif mode == 2:
            return self.relative_base + self.read(self.i + offset)
        else:
            raise ValueError("Invalid address mode")

    def run(self):
        self.waiting = False

        while True:
            instruction = self.read(self.i)
            opcode = instruction % 100
            mode1 = (instruction // 100) % 10
            mode2 = (instruction // 1000) % 10
            mode3 = (instruction // 10000) % 10

            if opcode == 99:
                self.halted = True
                return self.outputs

            elif opcode == 1:
                self.write(self.address(3, mode3), self.param(1, mode1) + self.param(2, mode2))
                self.i += 4

            elif opcode == 2:
                self.write(self.address(3, mode3), self.param(1, mode1) * self.param(2, mode2))
                self.i += 4

            elif opcode == 3:
                if not self.input_values:
                    self.waiting = True
                    return self.outputs

                self.write(self.address(1, mode1), self.input_values.pop(0))
                self.i += 2

            elif opcode == 4:
                self.outputs.append(self.param(1, mode1))
                self.i += 2
                return self.outputs

            elif opcode == 5:
                self.i = self.param(2, mode2) if self.param(1, mode1) != 0 else self.i + 3

            elif opcode == 6:
                self.i = self.param(2, mode2) if self.param(1, mode1) == 0 else self.i + 3

            elif opcode == 7:
                self.write(self.address(3, mode3), 1 if self.param(1, mode1) < self.param(2, mode2) else 0)
                self.i += 4

            elif opcode == 8:
                self.write(self.address(3, mode3), 1 if self.param(1, mode1) == self.param(2, mode2) else 0)
                self.i += 4

            elif opcode == 9:
                self.relative_base += self.param(1, mode1)
                self.i += 2

            else:
                raise ValueError(f"Unknown opcode {opcode}")

    def run_full(self):
        while not self.halted and not self.waiting:
            self.run()
        return self.outputs