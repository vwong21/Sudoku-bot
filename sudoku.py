import random
import math


def is_valid(board, row, col, num, size):
    """Check if placing 'num' in board[row][col] is valid."""
    if num in board[row]:  # Row check
        return False
    if num in [board[i][col] for i in range(size)]:  # Column check
        return False

    # Determine subgrid size dynamically
    box_size = int(math.sqrt(size))
    start_row, start_col = (row // box_size) * box_size, (col // box_size) * box_size

    for i in range(box_size):
        for j in range(box_size):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def solve_board(board, row, col, size):
    if row == size - 1 and col == size:
        return True
    if col == size:
        row += 1
        col = 0

    if board[row][col] != 0:
        return solve_board(board, row, col + 1, size)

    nums = list(range(1, size + 1))
    random.shuffle(nums)
    for num in nums:
        if is_valid(board, row, col, num, size):
            board[row][col] = num
            if solve_board(board, row, col + 1, size):
                return True
            board[row][col] = 0
    return False


def create_sudoku(size):
    if int(math.sqrt(size)) ** 2 != size:
        raise ValueError("Size must be a perfect square (4, 9, 16, ...)")
    board = [[0] * size for _ in range(size)]
    solve_board(board, 0, 0, size)
    return board


def remove_nums(board, size, num_holes=40):
    empty_board = [row[:] for row in board]
    count = 0
    while count < num_holes:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        if empty_board[row][col] != 0:
            empty_board[row][col] = 0
            count += 1
    return empty_board


if __name__ == "__main__":
    size = int(input("Enter grid size (4, 9, 16, ...): "))
    revealed = create_sudoku(size)
    puzzle = remove_nums(revealed, size, num_holes=42)
    print("Unsolved:")
    for row in puzzle:
        print(row)

    print()
    solved = solve_board(puzzle, 0, 0, size)
    print("Solved: ")

    for row in puzzle:
        print(row)
