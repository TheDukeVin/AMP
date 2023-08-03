def no_collisions_4x4(board, column, row):
    """Determines whether a board has Queens which attack the same squares
        on a 4x4 chess board.

      Args:
        board (list): A list lists representing the placement of Queens
        column (int): The current column being considered
        row (int):  The current row being considered

      Returns:
        bool: True if there are no collisions, False if there is 1 or more collisions
    """
    n = 4

    #Column Check: Not needed because of how we generate queens

    #Row Check: No 2 queens on the same row
    for j in range(column):
        if board[row][j] == 1:
            return False

    k = 1   # / Diagonal Check 
    while row - k >= 0 and column - k >= 0:
        if board[row - k][column - k] == 1:
            return False
        k += 1

    k = 1  # \ Diagonal Check
    while row + k < n and column - k >= 0:
        if board[row + k][column - k] == 1:
            return False
        k += 1

    return True

def four_queens():
    """Uses backtracking to print all solutions to the 4-Queens problem.
    """
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0] ]

    #Place a queen on successive rows, one column at a time
    #beginning with leftmost column
    for r0 in range(4):
        board[r0][0] = 1
        for r1 in range(4):
            board[r1][1] = 1
            if no_collisions_4x4(board, 1, r1):
                for r2 in range(4):
                    board[r2][2] = 1
                    if no_collisions_4x4(board, 2, r2):
                        for r3 in range(4):
                            board[r3][3] = 1
                            if no_collisions_4x4(board, 3, r3):
                                print (board)
                            #remove the queen to prep for next placements    
                            board[r3][3] = 0
                    board[r2][2] = 0
            board[r1][1] = 0
        board[r0][0] = 0

if __name__ == "__main__":
   four_queens()