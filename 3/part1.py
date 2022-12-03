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
        for elem in data:
            half_size = int(len(elem)/2)
            first_compartment = elem[0:half_size]
            second_compartment = elem[half_size:]
            common_element = list(set(first_compartment) & set(second_compartment))
            sum += score_for_elem(common_element[0])

        print(sum)


if __name__ == '__main__':
    main()
