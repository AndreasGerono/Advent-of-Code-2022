import os


def evaluate_tree_position(x, y, tree_map):
    tree = tree_map[x][y]

    visable_up = True
    visable_down = True
    visable_left = True
    visable_right = True

    score_up = 0
    score_down = 0
    score_left = 0
    score_right = 0

    # check up
    for i in reversed(range(0, x)):
        score_up += 1
        if tree <= tree_map[i][y]:
            visable_up = False
            break

    # check down
    for i in range(x + 1, len(tree_map)):
        score_down += 1
        if tree <= tree_map[i][y]:
            visable_down = False
            break

    # check left
    for j in reversed(range(0, y)):
        score_left += 1
        if tree <= tree_map[x][j]:
            visable_left = False
            break

    # check right
    for j in range(y + 1, len(tree_map[0])):
        score_right += 1
        if tree <= tree_map[x][j]:
            visable_right = False
            break

    visable = visable_left or visable_right or visable_down or visable_up
    score = score_left * score_right * score_up * score_down

    return visable, score


def main():
    input_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'input.txt')

    with open(input_path) as f:
        data = f.read()
        tree_map = data.splitlines()
        tree_map = [[int(tree) for tree in trees] for trees in tree_map]
        row_len = len(tree_map[0])
        col_len = len(tree_map)
        visable_fronts = row_len * 2
        visable_sides = 2 * (col_len - 2)
        visable = visable_sides + visable_fronts
        tree_scores = []
        for x in range(1, col_len - 1):
            for y in range(1, row_len - 1):
                is_visable, score = evaluate_tree_position(x, y, tree_map)
                tree_scores.append(score)
                if is_visable:
                    visable += 1

        print(visable)
        print(max(tree_scores))


if __name__ == '__main__':
    main()
