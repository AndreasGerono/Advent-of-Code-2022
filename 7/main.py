import os


class DirectoryTree:
    def __init__(self, name, prev) -> None:
        self.name = name
        self.files = dict()
        self.dirs = dict()
        self.previous = prev

    def add_file(self, name, size):
        if name not in self.files:
            self.files[name] = size

    def add_dir(self, name):
        if name not in self.dirs:
            self.dirs[name] = (DirectoryTree(name, self))

    def go_to_dir(self, name):
        if name == '..':
            return self.previous
        if name == '/':
            base_dir = self
            while base_dir.previous is not None:
                base_dir = base_dir.previous
            return base_dir

        return self.dirs[name]

    def my_size(self, result):
        sum = 0
        for _, size in self.files.items():
            sum += size

        for _, dir in self.dirs.items():
            sum += dir.my_size(result)

        result.append((self.name, sum))
        return sum


DISK_SPACE = 70000000
NEEDED_SPACE = 30000000


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    dir_tree = DirectoryTree('/', None)

    with open(input_path) as f:
        data = f.read()
        for line in data.splitlines():
            if line.startswith('$'):
                cmd = line.replace('$ ', '')
                if cmd == 'ls':
                    pass
                elif 'cd' in cmd:
                    dir_name = cmd.replace('cd ', '')
                    dir_tree = dir_tree.go_to_dir(dir_name)

            else:
                if line.startswith('dir'):
                    name = line.replace('dir ', '')
                    dir_tree.add_dir(name)
                else:
                    size, name = line.split(' ')
                    size = int(size)
                    dir_tree.add_file(name, size)

        dirs_spaces = []
        total_space = dir_tree.go_to_dir('/').my_size(dirs_spaces)
        free_space = DISK_SPACE - total_space
        need_to_free = NEEDED_SPACE - free_space

        sum_space = 0
        for name, size in dirs_spaces:
            if size <= 100000:
                sum_space += size

        valid_to_delete = [(name, size)
                           for name, size in dirs_spaces if size >= need_to_free]
        min_to_delete = min(valid_to_delete, key=lambda x: x[1])

        print('total size =', total_space)
        print('total size of at most 100000 =', sum_space)
        print('free space size =', free_space)
        print(f'space needed for update = {NEEDED_SPACE}, need to free up {need_to_free}')
        print(f'smallest dir to delete is `{min_to_delete[0]}` with size = {min_to_delete[1]}')


if __name__ == '__main__':
    main()
