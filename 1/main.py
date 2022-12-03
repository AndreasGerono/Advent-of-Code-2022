import os


def main():
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    with open(input_path) as f:
        data = f.read()
        data = data.split("\n\n")
        data = (elem.split('\n') for elem in data)

        elfs_calories = []
        for elf in data:
            elf_sum = 0
            for calories in elf:
                if calories:
                    elf_sum += int(calories)

            elfs_calories.append(elf_sum)

        # print(elfs_calories)
        print(max(elfs_calories))
        print(elfs_calories.index(max(elfs_calories)))

        max_sum = 0
        for i in range(3):
            max_val = max(elfs_calories)
            print(max_val)
            max_sum += max_val
            elfs_calories.remove(max_val)

        print(max_sum)


if __name__ == "__main__":
    main()
