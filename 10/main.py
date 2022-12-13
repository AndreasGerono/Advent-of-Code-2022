import os


class CPU:
    def __init__(self) -> None:
        self.register = 1
        self.cycles = 0
        self.sum_20 = 0
        self.display = ['.' for i in range(40)]

    def nop(self) -> None:
        self.__cycle()

    def add(self, x: int) -> None:
        self.__cycle()
        self.__cycle()
        self.register += x

    def __cycle(self):
        self.cycles += 1

        sprite = self.build_sprite()
        self.update_display(sprite)

        # start at 20 and every 20
        if (self.cycles + 20) % 40 == 0:
            val = (self.register * self.cycles)
            self.sum_20 += val

    def print_display(self):
        disp_str = ''
        for elem in self.display:
            disp_str = disp_str + elem

        print(f'CRT after cycle {self.cycles:03}: {disp_str}')

    def update_display(self, sprite):
        pos = (self.cycles - 1) % 40
        self.display[pos] = sprite[pos]

        if (self.cycles - 40) % 40 == 0:
            self.print_display()
            self.display = ['.' for i in range(40)]

    def build_sprite(self):
        sprite = []
        for i in range(1, 40 + 1):
            if self.register <= i < self.register + 3:
                sprite.append('#')
            else:
                sprite.append('.')

        return sprite


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    cpu = CPU()

    with open(input_path) as f:
        data = f.read()
        for line in data.splitlines():
            if line == 'noop':
                cpu.nop()
            else:
                inst, val = line.split(' ')
                val = int(val)
                cpu.add(val)

        print(cpu.sum_20)


if __name__ == '__main__':
    main()

"""
...............###......................
...............###......................
"""
