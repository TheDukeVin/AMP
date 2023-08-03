#!/usr/bin/env python3

from itertools import cycle
import random
import copy
from dectree import DecisionTree
from multiprocessing import Pool

class colors:
    ENDC = '\u001b[0m'
    CYAN = '\u001b[36m'
    GREEN = '\u001b[36m'
    BOLD = '\u001b[37;1m'
    RVRS = '\u001b[7m'
    UNDR = '\u001b[4m'
    UNUNDER = '\u001b[24m'


class Piece():

    def __init__(self, n):
        self.color = n % 2 == 1
        self.size = (n>>1) % 2 == 1
        self.holey = (n>>2) % 2 == 1
        self.shape = (n>>3) % 2 == 1


    def __str__(self):
        # return str(int(self.color)) \
        #     +  str(int(self.size)) \
        #     +  str(int(self.holey)) \
        #     +  str(int(self.shape))
        return "{strtc}{height}{left}{hole}{right}{unundr}{endc}".format(
            strtc  = colors.CYAN if self.color else "",
            endc   = colors.ENDC if self.color else "",
            left   = "(" if self.shape else "[",
            right  = ")" if self.shape else "]",
            hole   = "*" if self.holey else " ",
            height = colors.UNDR if self.size  else "",
            unundr = colors.UNUNDER if self.size else "",
        )

class Space():

    def __init__(self, piece = None):
        self.contents = piece

    def play(self, piece):
        if self.contents is None:
            self.contents = piece
            return True
        else:
            return False


    def is_free(self):
        return self.contents is None

    def __str__(self):
        if self.contents is None:
            return "   "
        else:
            return str(self.contents)



class Board():
    def __init__(self, n):
        self.n = n
        self.board = [
            [Space() for i in range(n)]
            for i in range(n)
        ]

    def __str__(self):
        out = "     "
        for i in range(self.n):
            out += str(i) + (" " * 5)
        out += "\n"
        for (i,row) in enumerate(self.board):
            out += "  " + ("-" * (self.n * 6 + 1))
            out += "\n"
            out += chr(ord("A") + i) + " "
            for col in row:
                out += "| " + str(col) + " "
            out += "|\n"
        out += "  " + ( "-" * (self.n * 6 + 1))
        return out

    def at(self, row, col):
        if row >= self.n:
            return False
        elif col >= self.n:
            return False
        else:
            return self.board[row][col]


    def free_spaces(self):
        return [(i,j)
                for (i, row) in enumerate(self.board)
                for (j, space) in enumerate(row)
                if space.is_free()]

    def check_win(self, line):
        """
        returns true if every space in a fully-filled `line` has a piece some matching attribute
        """
        colors = set()
        sizes = set()
        holes = set()
        shapes = set()
        for space in line:
            if space is None or space.contents is None:
                # the line must be fully filled
                return False
            else:
                colors.add(space.contents.color)
                sizes.add(space.contents.size)
                holes.add(space.contents.holey)
                shapes.add(space.contents.shape)

        # check whether any attributes are unique
        win = False
        if len(colors) == 1:
            # print("colors matched", ",".join(str(space.contents.color) for space in line))
            win |= True
        if len(sizes) == 1:
            # print("sizes_matched", ",".join(str(space.contents.size) for space in line))
            win |= True
        if len(holes) == 1:
            # print("holeyness matched", ",".join(str(space.contents.holey) for space in line))
            win |= True
        if len(shapes) == 1:
            # print("shapes matched", ",".join(str(space.contents.holey) for space in line))
            win |= True
        return win

    def check_win_horizontals(self):
        """
        returns true if every piece in a (full) row has some matching attribute
        """
        for (i,row) in enumerate(self.board):
            if self.check_win(row):
                # print("  row", i, "won!", ",".join(str(s) for s in row))
                return True
        return False


    def check_win_verticals(self):
        """
        returns true if every piece in a (full) column has some matching attribute
        """
        for i in range(self.n):
            line = [self.board[j][i] for j in range(self.n)]
            if self.check_win(line):
                # print("col", i, "won", ",".join(str(s) for s in line))
                return True
        return False

    def check_win_diagonals(self):
        """
        returns true if four pieces have matching attributes along the major or minor diagonal
        """
        win = False
        win |= self.check_win([self.board[i][i]              for i in range(self.n)])
        # if win: print("the major diagonal won")
        win |= self.check_win([self.board[i][self.n - 1 - i] for i in range(self.n)])
        # if win: print("the minor diagonal won")
        return win

    def isWinCondition(self):
        """
        returns true if 4 in a row, column or diagonal of the same type occur on the board.
        """
        return self.check_win_horizontals() \
            or self.check_win_verticals() \
            or self.check_win_diagonals()

    def gameOver(self):
        """
        returns true if all pieces have been played
        """
        return all([all([space.contents is not None for space in row])
                    for row in self.board])

class GameState():
    def __init__(self, n):
        self.turn = 1
        self.board = Board(n)
        self.pieces = [Piece(i) for i in range(n ** 2)] # Warning this only works for size < 4

    def print_game_state(self):
        stringify_piece = \
            lambda piece: \
            "     " if piece is None \
            else " {} ".format(str(piece))

        piece_str_list = ["{2}{0}: {1}".format(str(i) + (" " if i < 10 else ""),
                                             stringify_piece(piece),
                                             "\n  " if i % 4 == 0 else "")
                          for (i, piece) in enumerate(self.pieces) ]

        pieces_str = "Pieces:" + "  ".join(piece_str_list)

        print(pieces_str)
        print("**")
        print()
        print(self.board)
        print()


    def piece_indices(self):
        return [i for (i,x) in enumerate(self.pieces)
                if x is not None]

    def free_spaces (self):
        return self.board.free_spaces()

    def pick(self, idx):
        if idx >= self.board.n ** 2: return None
        piece = self.pieces[idx]
        self.pieces[idx] = None
        return piece

    def at(self, row, col):
        return self.board.at(row,col)

class Player ():
    def __init__(self, ident, game):
        self.game = game
        self.ident = str(ident)

    def __str__(self):
        return str(self.ident)

    def pick(self):
        piece = None
        while piece is None:
            str_index = input("player " + str(self) + ", pick a piece: ")
            index = int(str_index.strip())
            piece = self.game.pick(index)

        return piece

    def play(self, piece):
        played = False
        while not played:
            location = input("player " + str(self) + ", pick a place: ")
            row = ord(location[0].lower()) - ord("a")
            col = int(location[1:])
            played = self.game.at(row,col).play(piece)
        return True


class RandomAgent(Player):

    def pick (self):
        piece_idx = random.choice(self.game.piece_indices())
        piece = self.game.pick(piece_idx)
        print("Player {} picked piece {}: {}".format(self.ident, piece_idx, piece))
        return piece

    def play (self, piece):
        (row,col) = random.choice(self.game.free_spaces())
        print("Player {} playing at ({},{})".format(self.ident, row, col))
        return self.game.at(row,col).play(piece)

class WinIfYouCanAgent(RandomAgent):

    def can_win_with(self,piece):
        """
        returns a space at which you can play `piece` and win the game
        """
        for (row,col) in self.game.free_spaces():
            temp_game = copy.deepcopy(self.game)
            temp_game.at(row,col).play(piece)
            if temp_game.board.isWinCondition():
                return (row,col)
        return None

    def play(self, piece):
        """
        if there's a spot to play that wins you the game, play there
        """
        space = self.can_win_with(piece)
        if space is not None:
            return self.game.at(*space).play(piece)
        return super().play(piece)


class DontLoseAgent(WinIfYouCanAgent):

    def can_lose_with(self, piece):
        return self.can_win_with(piece) is not None

    def pick(self):
        """
        if you can help it, don't pick a piece that will allow the other player to win
        """
        for (idx,piece) in enumerate(self.game.pieces):
            if piece is None or self.can_lose_with(piece):
                continue
            else:
                piece = self.game.pick(idx)
                print("Player {} picked piece {}: {}".format(self.ident, idx, piece))
                return piece

        return super().pick()


class TotalEnumAgent(DontLoseAgent):

    def pick(self):
        # print("building pick decision tree")
        dt = DecisionTree(self.game, None, True, 3)
        # print("done")
        idx = dt.determine_best_move()
        if idx is None:
            return super().pick()
        else:
            piece = self.game.pick(idx)
            print("Player {} picked piece {}: {}".format(self.ident, idx, piece))
            return piece

    def play(self, piece):
        # space = self.can_win_with(piece)
        # if space is not None:
        #     return self.game.at(*space).play(piece)
        dt = DecisionTree(self.game, piece, True, 3)
        space = dt.determine_best_move()
        if space is None:
            return super().play(piece)
        else:
            return self.game.at(*space).play(piece)
    
class GameDriver ():
    def __init__(self, n):
        self.game = GameState(n)
        self.players = cycle([Player(1, self.game), TotalEnumAgent(2, self.game)])

    def run(self):
        player = next(self.players)
        while not self.game.board.isWinCondition() and not self.game.board.gameOver():
            self.game.print_game_state()
            piece = player.pick()
            player = next(self.players)
            player.play(piece)

        print("Player", str(player), "won!")
        self.game.print_game_state()
        # print()
        print("Congrats player {}!".format(player))
        return player.ident


def do(x):
    return GameDriver(4).run()


def benchmark():
    results = []
    n = 100

    with Pool(15) as p:
        for winner in p.imap_unordered(do, range(n)):
            print(winner)
            results.append(winner)


    num_win1 = len([i for i in results if i == "1"])
    num_win2 = len([i for i in results if i == "2"])
    print("Player 1 won {}% of games".format((num_win1 / n) * 100))
    print("Player 2 won {}% of games".format((num_win2 / n) * 100))

def main():
    print("Welcome to Quarto.py!")
    GameDriver(4).run()




if __name__ == "__main__":
    main()
