import os

# WIN   6
# DRAW  3
# LOSE  0

# ROCK     X
# PAPER    Y
# SCISSORS Z

# ROCK VS ROCK              1 + 3 = 4 -> A X
# ROCK VS PAPER             2 + 6 = 8 -> A Y
# ROCK VS SCISSORS          3 + 0 = 3 -> A Z

# PAPER VS ROCK             1 + 0 = 1 -> B X
# PAPER VS PAPER            2 + 3 = 5 -> B Y
# PAPER VS SCISSORS         3 + 6 = 9 -> B Z

# SCISSORS VS ROCK          1 + 6 = 7 -> C X
# SCISSORS VS PAPER         2 + 0 = 2 -> C Y
# SCISSORS VS SCISSORS      3 + 3 = 6 -> C Z

SCORE_MAPPING = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,

    'B X': 1,
    'B Y': 5,
    'B Z': 9,

    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

# Round 2

# X LOSE
# ROCK     SCISSORS         A X -> A Z
# PAPER    ROCK             B X -> B X
# SCISSORS PAPER            C X -> C Y

# Y DRAW
# ROCK ROCK                 A Y -> A X
# PAPER PAPER               B Y -> B Y
# ROCK ROCK                 C Y -> C Z

# Z WIN
# ROCK     PAPER            A Z -> A Y
# PAPER    SCISSORS         B Z -> B Z
# SCISSORS ROCK             C Z -> C X

SHAPE_MAPPING = {
    'A X': 'A Z',
    'B X': 'B X',
    'C X': 'C Y',

    'A Y': 'A X',
    'B Y': 'B Y',
    'C Y': 'C Z',

    'A Z': 'A Y',
    'B Z': 'B Z',
    'C Z': 'C X',
}


def main():
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    with open(input_path) as f:
        sum = 0
        for line in f.read().splitlines():
            new_shape = SHAPE_MAPPING.get(line)
            sum += SCORE_MAPPING.get(new_shape)

        print(sum)


if __name__ == "__main__":
    main()
