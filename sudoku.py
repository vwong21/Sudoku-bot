import random


def create_sudoku():
    res = [[], [], [], [], [], [], [], [], []]
    add_to_cell(0, 0, res)

    return res


def add_to_cell(col, row, board):
    # new plan. Create exclusion list and replace line 15 if statement to that.
    if row > 8:
        return board
    num = random.choice([i for i in range(1, 10) if i not in board[row]])
    # num = random.randint(1, 9)
    for i in board:
        if i == []:
            continue
        if i[col-1] == num:
            # doesn't work. New plan see line 12
            return add_to_cell(col, row, board)

    board[row].append(num)
    if col >= 8:
        row += 1
        col = 0
        return add_to_cell(col, row, board)
    return add_to_cell(col+1, row, board)


if __name__ == "__main__":
    print(create_sudoku())
