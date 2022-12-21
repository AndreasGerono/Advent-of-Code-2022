import os


class Cave:
    def __init__(self, scan) -> None:
        self.middle_x = 500
        self.rocks = set()
        self.sand = set()
        self.parse(scan)

    def parse(self, scan):
        for line in scan:
            traces = line.split(' -> ')

            for i in range(len(traces)-1):
                start_x, start_y = traces[i].split(',')
                end_x, end_y = traces[i + 1].split(',')

                start_x, start_y = int(start_x), int(start_y)
                end_x, end_y = int(end_x), int(end_y)

                new_start_x = min(start_x, end_x)
                new_end_x = max(start_x, end_x)

                for x in range(new_start_x, new_end_x + 1):
                    self.rocks.add((x, start_y))

                new_start_y = min(start_y, end_y)
                new_end_y = max(start_y, end_y)

                for y in range(new_start_y, new_end_y + 1):
                    self.rocks.add((start_x, y))

    def draw(self):
        min_x = min(self.rocks, key=lambda x: x[0])[0]
        max_x = max(self.rocks, key=lambda x: x[0])[0]

        min_x = min(min_x, min(self.sand, key=lambda x: x[0])[0])
        max_x = max(max_x, max(self.sand, key=lambda x: x[0])[0])

        min_y = 0
        max_y = max(self.rocks, key=lambda x: x[1])[1] + 2

        picture = ''
        for y in range(min_y, max_y + 1):
            row = ''
            for x in range(min_x, max_x + 1):
                if y == max_y:
                    row += '#'
                elif (x, y) in self.rocks:
                    row += '#'
                elif (x, y) in self.sand:
                    row += 'o'
                else:
                    row += '.'

            picture += row + '\n'

        print(picture)

    def add_grain(self):
        max_y = max(self.rocks, key=lambda x: x[1])[1]
        floor = max_y + 2

        x, y = 500, 0

        while True:
            next_y = y + 1
            if (x, next_y) not in self.rocks and (x, next_y) not in self.sand and next_y < floor:  # noqa 501
                y = next_y
            elif (x - 1, next_y) not in self.rocks and (x - 1, next_y) not in self.sand and next_y < floor: # noqa 501
                y = next_y
                x -= 1
            elif (x + 1, next_y) not in self.rocks and (x + 1, next_y) not in self.sand and next_y < floor: # noqa 501
                y = next_y
                x += 1
            else:
                break

        self.sand.add((x, y))
        # self.draw()
        if y == 0:
            return False
        return True

    def fill_with_sand(self):
        while True:
            if not self.add_grain():
                break


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    with open(input_path) as f:
        data = f.read().splitlines()
        cave = Cave(data)
        cave.fill_with_sand()
        cave.draw()
        print(len(cave.sand))


if __name__ == '__main__':
    main()
