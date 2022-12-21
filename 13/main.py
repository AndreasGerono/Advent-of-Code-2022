import os
from pprint import pprint
import json
from functools import cmp_to_key


def compare_packets(packet1, packet2):
    pkt1_len = len(packet1)
    pkt2_len = len(packet2)

    max_len = max(pkt1_len, pkt2_len)

    result = 0

    for i in range(max_len):
        if i >= pkt1_len:
            return 1
        elif i >= pkt2_len:
            return -1

        elem1 = packet1[i]
        elem2 = packet2[i]

        if isinstance(elem1, list) and isinstance(elem2, list):
            result = compare_packets(elem1, elem2)
        elif isinstance(elem1, list) and isinstance(elem2, int):
            result = compare_packets(elem1, [elem2])
        elif isinstance(elem1, int) and isinstance(elem2, list):
            result = compare_packets([elem1], elem2)
        elif elem2 > elem1:
            result = 1
        elif elem2 < elem1:
            result = -1

        if result != 0:
            return result

    return result


def cmp_list():
    pass


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    with open(input_path) as f:
        data = f.read()
        pairs = data.split('\n\n')
        pairs.append('[[2]]\n[[6]]')
        result = 0
        all_packets = []
        for i, pair in enumerate(pairs):
            packet1, packet2 = pair.split('\n')
            packet1 = json.loads(packet1)
            packet2 = json.loads(packet2)
            all_packets.append(packet1)
            all_packets.append(packet2)

            if compare_packets(packet1, packet2) == 1:
                result += i + 1

        print(result)
        all_packets.sort(key=cmp_to_key(compare_packets), reverse=True)
        first_key = all_packets.index([[2]]) + 1
        second_key = all_packets.index([[6]]) + 1
        print(first_key * second_key)


if __name__ == '__main__':
    main()
