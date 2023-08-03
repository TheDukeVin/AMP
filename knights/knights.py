

def generateKnightMoveGraph(board_labels):
    '''Returns a graph for all valid knight moves on a given board'''
    valid_moves = {}
    potential_moves=[(-2, 1),(-1, 2),(1, 2),(2, 1),(2, -1), (1, -2),(-2, -1), (-1, -2)]

    for row, r in enumerate(board_labels):
        for col in range(len(board_labels[0])):
            spot = board_labels[row][col]
            valid_moves[spot] = []
            for move in potential_moves:
                new_row = row + move[0]
                if new_row >=0 and new_row<len(board_labels):
                    new_col = col + move[1]
                    if new_col>=0 and new_col<len(board_labels[0]):
                        valid_spot=board_labels[new_row][new_col]
                        valid_moves[spot].append(valid_spot)

    print(valid_moves)

if __name__ == "__main__":
    start = [
        ["W","-","W"],
        ["-","-","-"],
        ["B","-","B"]
       ]
    target = [
        ["B","-","B"],
        ["-","-","-"],
        ["W","-","W"]
       ]
    board_labels=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
       ]
    generateKnightMoveGraph(board_labels)
