import random


def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(0, 9)]:
        return False
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def make_board(board, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0

    if board[row][col] != 0:
        return make_board(board, row, col + 1)

    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if make_board(board, row, col + 1):
                return True
            board[row][col] = 0
    return False


def create_sudoku():
    board = [[0] * 9 for _ in range(9)]
    make_board(board, 0, 0)
    return board


def remove_nums(board, num_holes=40):
    empty_board = [row[:] for row in board]
    count = 0
    while count < num_holes:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if empty_board[row][col] != 0:
            empty_board[row][col] = 0
            count += 1
    return empty_board


def solve_board(puzzle, row, col):
    if row == 8 and col == 9:
        return True
    if col == 9:
        row += 1
        col = 0

    if puzzle[row][col] != 0:
        return solve_board(puzzle, row, col + 1)

    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num
            if solve_board(puzzle, row, col + 1):
                return True
            puzzle[row][col] = 0
    return False


if __name__ == "__main__":
    reveal = create_sudoku()
    puzzle = remove_nums(reveal, num_holes=42)
    print("Unsolved:")
    for row in puzzle:
        print(row)

    solved = solve_board(puzzle, 0, 0)
    print("Solved: ")

    for row in puzzle:
        print(row)
