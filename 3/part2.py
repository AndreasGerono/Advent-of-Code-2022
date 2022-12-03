import os


def score_for_elem(elem: str):
    if elem.isupper():
        return ord(elem) - 65 + 27
    return ord(elem) - 97 + 1


def main():
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    with open(input_path) as f:
        data = f.read().splitlines()
        sum = 0
        step = 3
        for i in range(0, len(data), step):
            unique_in_group = set(data[i])
            for elem in data[i:i+step]:
                unique_in_group &= set(elem)

            badge = list(unique_in_group)[0]
            sum += score_for_elem(badge)

        print(sum)


if __name__ == '__main__':
    main()
