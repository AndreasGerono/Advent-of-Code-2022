import os
import re
from pprint import pprint


def parse_stacks(drawing: str):
    START = 1
    DISTANCE = 4

    lines = drawing.splitlines()
    num_stacks = int(lines[-1].split('  ')[-1])
    stacks = [[] for x in range(num_stacks)]
    for line in lines[:-1]:
        for i in range(num_stacks):
            elem = line[START + i * DISTANCE]
            if elem != ' ':
                stacks[i].append(elem)

    return stacks


def parse_operation(operation: str):
    match = re.match(r'move (\d+) from (\d+) to (\d+)', operation)

    num = int(match[1])
    src = int(match[2]) - 1
    dst = int(match[3]) - 1

    return num, src, dst


def main():
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    with open(input_path) as f:
        data = f.read()
        drawing, rearrangement = data.split('\n\n')
        stacks = parse_stacks(drawing)
        for line in rearrangement.splitlines():
            num, src, dst = parse_operation(line)
            elems = stacks[src][:num]
            stacks[src] = stacks[src][num:]
            stacks[dst] = [*elems, *stacks[dst]]

        pprint(stacks, width=100)
        result = ''.join([x[0] for x in stacks])
        print(result)


if __name__ == '__main__':
    main()
