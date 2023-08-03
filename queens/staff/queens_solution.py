"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""
# python3 run_tests_local.py --verbosity 2 queens

def pretty_print(board: list) -> list[str]:
    """Represents the board as a string. 
        -Queens are represented with a Q
        -Empty squares are reprented with a .
        -The first character in the string is \n, and each line of the board ends with \n

        Args:
          board (list): Non-negative entries indicate a particular row for the column reprented by the index of the list
    
        Returns:
          A list of strings representing a human-readable version of the board

        Example
        -------
        >>>pretty_print([2, 0, 3, 1])
        "\n.Q..\n...Q\nQ...\n..Q.\n"
    """
    pretty_board = [["."]*len(board) for i in range(len(board))]
    for col_index, spot in enumerate(board): 
      if spot >=0 and spot <=len(board):
       pretty_board[spot][col_index]="Q"

    string_version="\n"
    for row in pretty_board:
       string_row=""
       for square in row:
          string_row+=square
       string_version+=string_row+"\n"
    return string_version

def no_collisions(board: list[int], current_col:int)->bool:
  '''Considers columns to thes left of the current column to check for row and diagonal conflicts in the board.
     Assumes all columns to the left of the current column have a non-negative integer ie a Queen has been placed

     Args:
      board (list): Non-negative entries indicate a particular row for the column reprented by the index of the list
      current_col (int): The current column being considered

     Returns:
       bool: False indicates two Queens attack the same square, otherwise True

     Examples
     --------
     >>>no_collisions([0, 6, 4, 7, 3, -1, -1, -1], 4)
     False

     >>>no_collisions([0, 6, 4, 7, 3, 6, -1, -1], 5)
     False

     >>>no_collisions([2, 4, 1, 7, 5, 3, 6, 0], 7)
     True
  '''
  for i in range(current_col):
    if board[i] == board[current_col]:
      return False
    if current_col - i == abs(board[current_col] - board[i]):
      return False
  return True

def eight_queens():
    board = [-1] * 8  #no queens in any column
    for i in range(8):
        board[0] = i
        for j in range(8):
            board[1] = j
            if not no_collisions(board, 1):
                continue
            for k in range(8):
                board[2] = k
                if not no_collisions(board, 2):
                    continue
                for l in range(8):
                    board[3] = l
                    if not no_collisions(board, 3):
                        continue
                    for m in range(8):
                        board[4] = m
                        if not no_collisions(board, 4):
                            continue
                        for o in range(8):
                            board[5] = o
                            if not no_collisions(board, 5):
                                continue
                            for p in range(8):
                                board[6] = p
                                if not no_collisions(board, 6):
                                    continue
                                for q in range(8):
                                    board[7] = q
                                    if no_collisions(board, 7):
                                        print (board)

def eight_queens_solutions(num_sol:int)->list[list[int]]:
  '''Generates num_sol solutions to the 8 queens problem.  
     If n is greater than the total number of solutions, returns all solutions.

      Args:
        num_sol (int): The desired number of solutions

      Returns:
         A list of num_sol solutions (or all solutions)
  '''
  n=8
  listOfBoards = []
  board = [-1] * n
  sol = 0
  for i in range(n):
    board[0] = i
    for j in range(n):
      board[1] = j
      if not no_collisions(board, 1):
        continue
      for k in range(n):
        board[2] = k
        if not no_collisions(board, 2):
          continue
        for l in range(n):
          board[3] = l
          if not no_collisions(board, 3):
            continue
          for m in range(n):
            board[4] = m
            if not no_collisions(board, 4):
              continue
            for o in range(n):
              board[5] = o
              if not no_collisions(board, 5):
                continue
              for p in range(n):
                board[6] = p
                if not no_collisions(board, 6):
                  continue
                for q in range(n):
                  board[7] = q
                  if no_collisions(board, 7):
                    if sol < num_sol:
                      listOfBoards.append(board[:])
                      sol += 1
                    else:
                      return listOfBoards
  return listOfBoards

def n_queens(board:list[int], current_col:int=0)->bool:
    if (current_col == len(board)): 
        return True
    else: 
        # for each potential row in the board
        for row in range(len(board)):
            board[current_col] = row #try the row
            if (no_collisions(board, current_col)):
                #move on to the next column 
                done = n_queens(board, current_col + 1) 
                if done:
                    print(board)
        return False

def n_queens_solutions(board_size:int, num_sol:int, solutions:list=[], board:list[int]=[], current_col:int=0)->bool:
  '''Finds mulitple solutions to the n-queens problem. If num_sol is greater than the total number of solutions, returns all solutions.

      Args:
        board_size (int): The size of the board
        num_sol (int): The desired number of solutions
        solutions (list): A list of all the solutions for an N-sized board
        board (list): The current board configuration which will be modified via successive recursive calls
        current_col (int): The current column being considered

      Returns:
        bool: True/False depending on whether a solution of size board_size has been found
  '''
  if len(board) == 0:
      board = [-1]*board_size

  if current_col == len(board): # Base Case: all columns considered,
      return True    #time to move on to the next row
  elif len(solutions) < num_sol: 
      for row in range(len(board)): # for each potential row in the board
          board[current_col] = row #try the row
          if no_collisions(board, current_col): # if the row works
              done = n_queens_solutions(board_size, num_sol, solutions, board, current_col + 1) #move on to the next column
              if done and len(solutions)<num_sol:
                  solutions.append(board[:]) # appends a copy of the current baord configuration

      return False

def n_queens_fill(full_solution:list[int], partial_solution:list[int], current_col:int=0)->bool:
  '''Generates a full solution to the n-Queens problem that is consistent with a given list of queen locations.
     If the given list of n-Queens locations cannot lead to a full solution, return None

     For example:
       - n_queens_fill([2, -1, -1, -1, -1, -1, -1, 0]) → [2, 4, 1, 7, 5, 3, 6, 0]
       - n_queens_fill([-1, 2, -1, -1]) → None

      Args:
        full_solution (list): a list that will be mutated to eventually include the full solution 
        partial_solution (list): A list of queen row positions, where nonnegative entries
                             for certain columns correspond to fixed queen row positions.
        current_col (int): a defualt parameter which indicates the current column being considered

      Returns
        a boolean 
  '''
  if current_col == len(full_solution): # Base Case: all columns considered
      return True 
  elif no_collisions(full_solution, current_col):
      for row in range(len(partial_solution)): # for each potential row in the board
          full_solution[current_col] = row #try the row

          if partial_solution[current_col] == -1 or row == partial_solution[current_col]:
              if no_collisions(full_solution, current_col): # if the row could work
                  done = n_queens_fill(full_solution, partial_solution, current_col + 1) #move on to the next column
                  if done:
                      return True
      return False
  else:
     print(full_solution, current_col)
     full_solution = [-1]*len(partial_solution)

if __name__ == "__main__":
    #incompleteSolution = [2, -1, -1, 7, 5, -1, -1, -1]
    #print(repr(pretty_print([7, 1, 3, 0, 6, 4, 2, 5])))
    #solutions=[]
    #print(n_queens_solutions(4, 1000, solutions))
    #print(solutions)
    #board=[-1] * 4
    #n_queens(board)
    #print(board)
    solution_board=[-1]*8
    partial_board=[2, -1, -1, -1, -1, -1, -1, 0]
    print(n_queens_fill(solution_board, partial_board))
    print(solution_board)
    #print(solution)