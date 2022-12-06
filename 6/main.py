import os


def found_unique_series(data: str, cnt: int):
    for i in range(len(data) - cnt):
        unique = set(data[i:i+cnt])
        if len(unique) == cnt:
            return i + cnt


def main():
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    with open(input_path) as f:
        data = f.read()
        for line in data.splitlines():
            pkt_start = found_unique_series(line, 4)
            msg_start = found_unique_series(line, 14)
            print(f'pkt marker, mgs marker: {pkt_start} {msg_start}')


if __name__ == '__main__':
    main()
