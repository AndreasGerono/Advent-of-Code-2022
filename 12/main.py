import os
import math


class Cell:
    def __init__(self, y, x, w) -> None:
        self.y = y
        self.x = x
        self.w = w

    def __str__(self) -> str:
        return f'(y: {self.y} x: {self.x} w: {self.w})'

    def __repr__(self) -> str:
        return self.__str__()


class Grid:
    def __init__(self, lines) -> None:
        self.lines = lines
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)
        self.height = len(lines)
        self.width = len(lines[0])
        self.low_points = []
        self.grid = []

    def get_cell(self, y, x):
        return self.grid[y][x]

    def parse(self):
        for j, line in enumerate(self.lines):
            row = []
            for i, ele in enumerate(line):
                if ele == 'S':
                    ele = 'a'
                    self.start_pos = (j, i)
                elif ele == 'E':
                    ele = 'z'
                    self.end_pos = (j, i)

                w = ord(ele) - 96
                row.append(Cell(j, i, w))

                if w == 1:
                    self.low_points.append(Cell(j, i, w))

            self.grid.append(row)

    def get_path(self, cell):
        x = cell.x
        y = cell.y

        path = []
        if x + 1 < self.width and self.grid[y][x+1].w - cell.w <= 1:
            path.append(self.grid[y][x+1])
        if x - 1 >= 0 and self.grid[y][x-1].w - cell.w <= 1:
            path.append(self.grid[y][x-1])
        if y + 1 < self.height and self.grid[y + 1][x].w - cell.w <= 1:
            path.append(self.grid[y+1][x])
        if y - 1 >= 0 and self.grid[y - 1][x].w - cell.w <= 1:
            path.append(self.grid[y-1][x])

        return path

    def dijkstra(self, start):
        distances = dict()
        distances[start] = 0

        frontier = [start]
        while frontier:
            new_frontier = []
            for cell in frontier:
                for next in self.get_path(cell):
                    if distances.get(next) is not None:
                        continue
                    distances[next] = distances[cell] + 1
                    new_frontier.append(next)

            frontier = new_frontier

        self.distances = distances


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    with open(input_path) as f:
        lines = f.read().splitlines()
        grid = Grid(lines)
        grid.parse()
        y, x = grid.end_pos
        result = []
        for cell in grid.low_points:
            grid.dijkstra(cell)
            result.append(grid.distances.get(grid.get_cell(y, x), math.inf))

        print(len(grid.low_points))
        print(min(result))


if __name__ == '__main__':
    main()
