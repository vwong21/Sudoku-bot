import random

def is_valid(board, row, col, num):

    if num in board[row]:
        return False
    

    if num in [board[i][col] for i in range(9)]:
        return False


    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
                
    return True

def solve(board):

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  
                numbers = list(range(1, 10))
                random.shuffle(numbers) 
                
                for num in numbers:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board): 
                            return True
                        board[row][col] = 0  
                    
                return False  
    return True

def create_sudoku():

    board = [[0] * 9 for _ in range(9)] 
    solve(board)  
    return board

if __name__ == "__main__":
    for row in create_sudoku():
        print(row)
