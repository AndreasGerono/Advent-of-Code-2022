import os


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y


class Rope:
    def __init__(self, segments, x, y) -> None:
        self.pos = Point(x, y)
        self.next = None
        self.index = 0
        self.positions = set((x, y))

        for _ in range(segments):
            self.add_segment(x, y)

    def add_segment(self, x, y):
        current = self
        cnt = 1
        while current.next is not None:
            current = current.next
            current.index = cnt
            cnt += 1

        current.next = Rope(0, x, y)

    def count_pos(self):
        all_positions = []
        current = self
        while current.next is not None:
            all_positions.append(current.positions)
            current = current.next

        positions = all_positions.pop(-1)
        # positions.add((25, 25))

        return len(positions)

    def step(self, dest: Point):
        prev_pos = self.pos

        if dest.x > self.pos.x:
            self.pos.x += 1
        elif dest.x < self.pos.x:
            self.pos.x -= 1
        if dest.y > self.pos.y:
            self.pos.y += 1
        elif dest.y < self.pos.y:
            self.pos.y -= 1

        if self.next is not None:
            if (abs(self.pos.y - self.next.pos.y) > 1 or
                    abs(self.pos.x - self.next.pos.x) > 1):
                self.next.step(prev_pos)

        self.positions.add((self.pos.x, self.pos.y))

    def __str__(self) -> str:
        index_points = []
        current = self
        while current is not None:
            index_points.append((current.index, current.pos))
            current = current.next

        grid_width = 50
        grid_height = 50

        index_points = index_points[::-1]

        grid_str = ''
        for y in range(grid_height):
            row_str = ''
            for x in range(grid_width):
                elem = '.'
                pos = Point(x, y)
                for index, point in index_points:
                    if pos == point:
                        elem = str(index)
                row_str = row_str + elem
            row_str += '\n'
            grid_str = grid_str + row_str

        return grid_str


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    rope = Rope(10, 25, 25)

    with open(input_path) as f:
        data = f.read()
        for line in data.splitlines():
            direction, steps = line.split()
            steps = int(steps)
            print(direction, steps)
            for step in range(steps):
                dest = rope.pos

                if direction == 'U':
                    dest.y -= 1
                if direction == 'D':
                    dest.y += 1
                if direction == 'L':
                    dest.x -= 1
                if direction == 'R':
                    dest.x += 1

                rope.step(dest)
            print(rope)
        print(rope.count_pos())


if __name__ == '__main__':
    main()
