import os


class Monkey:
    modulo = 1

    def __init__(self, desc: str) -> None:
        self.parse(desc)

    def parse(self, desc: str) -> None:
        desc = desc.splitlines()
        self.num = int(desc[0][7:-1])
        self.items = [int(item) for item in desc[1][18:].split(', ')]
        self.operation_type = desc[2][23]
        self.operation_val = desc[2][25:]
        self.div_test = int(desc[3][21:])
        self.throw_to_if_true = int(desc[4][29:])
        self.throw_to_if_false = int(desc[5][30:])
        self.inspection_count = 0
        Monkey.modulo *= self.div_test

    def __str__(self) -> str:
        return f"Monkey {self.num} inspected items {self.inspection_count} \
times, items: {self.items}"

    def add(self, item: int):
        self.items.append(item)

    def inspect(self):
        result = []
        for item in self.items:
            result.append(self.throw(item))

        self.items = []

        return result

    def throw(self, item) -> int:
        target = 0
        worry_level = item
        if self.operation_val == 'old':
            operational_val = item
        else:
            operational_val = int(self.operation_val)

        if self.operation_type == '+':
            worry_level += operational_val
        elif self.operation_type == '*':
            worry_level *= operational_val

        worry_level %= Monkey.modulo

        if worry_level % self.div_test == 0:
            target = self.throw_to_if_true
        else:
            target = self.throw_to_if_false

        self.inspection_count += 1

        # print(self.num, target, item)
        return (target, worry_level)


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    monkeys = []

    with open(input_path) as f:
        data = f.read()
        monkeys_descs = data.split('\n\n')
        for monkey_desc in monkeys_descs:
            monkeys.append(Monkey(monkey_desc))

        for i in range(10000):
            if i % 10 == 0:
                print(i)
            for monkey in monkeys:
                result = monkey.inspect()
                for target, item in result:
                    monkeys[target].add(item)

        monkeys.sort(key=lambda x: x.inspection_count, reverse=True)
        for monkey in monkeys:
            print(monkey)

        monkey_business = monkeys[0].inspection_count * monkeys[1].inspection_count
        print(f"monkey_business: {monkey_business}")


if __name__ == '__main__':
    main()
