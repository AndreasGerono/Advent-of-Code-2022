import os


def set_from_section(start_end: str):
    start = int(start_end.split('-')[0])
    end = int(start_end.split('-')[1]) + 1
    return set(range(start, end))


def part_one(data):
    sum = 0
    for pair in data:
        sections = pair.split(',')

        first_section = set_from_section(sections[0])
        second_section = set_from_section(sections[1])
        longer_list_len = max(len(first_section), len(second_section))
        joined_len = len(first_section | second_section)

        if (joined_len == longer_list_len):
            sum += 1

    print("Part one: ", sum)


def part_two(data):
    sum = 0
    for pair in data:
        sections = pair.split(',')

        first_section = set_from_section(sections[0])
        second_section = set_from_section(sections[1])
        sum_len = len(first_section) + len(second_section)
        joined_len = len(first_section | second_section)

        if (joined_len != sum_len):
            sum += 1

    print("Part two: ", sum)


def main():
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    with open(input_path) as f:
        data = f.read().splitlines()
        part_one(data)
        part_two(data)

if __name__ == '__main__':
    main()
