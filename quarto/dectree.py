#!/usr/bin/env python3

import math
import copy

class DecisionTree():

    def __init__(self, game, piece, your_turn, lookahead):
        self.game = game
        self.your_turn = your_turn
        self.piece = piece         # piece is none if the next game is a pick game
        self.next_states = None
        self.lookahead = lookahead
        self.win = self.game.board.isWinCondition() and self.your_turn
        # if self.win: print("            WIN")
        self.loss = self.game.board.isWinCondition() and not self.your_turn
        # if self.loss: print("            LOSE")
        if not self.win and not self.loss:
            if not self.game.board.gameOver() \
               and self.lookahead > 0:
                self.generate()

        if self.next_states is not None:
            must_lose = True
            for (_, child) in self.next_states:
                must_lose &= child.loss

            if must_lose:
                assert (not self.win)
                self.loss = True
                self.next_states = None


    def gen_pick_children(self):
        self.next_states = []
        for (idx, piece) in enumerate(self.game.pieces):
            if piece is None:
                continue
            else:
                # print("  "*(2-self.lookahead), "TEST STATE FOR PIECE {}: {}, your turn? {}".format(idx, piece, self.your_turn))
                new_state = copy.deepcopy(self.game)
                new_state.pick(idx)
                dt = DecisionTree(new_state,
                                  piece,
                                  not self.your_turn,
                                  self.lookahead - 1)
                self.next_states.append((idx,dt))

    def gen_play_children(self):
        self.next_states = []
        for (row, col) in self.game.free_spaces():
            # print("  "*(3-self.lookahead), "TEST STATE FOR SPACE", (row,col), "your turn?", self.your_turn)
            new_state = copy.deepcopy(self.game)
            new_state.at(row, col).play(self.piece)
            dt = DecisionTree(new_state,
                              None,
                              self.your_turn,
                              self.lookahead - 1)
            self.next_states.append(((row,col), dt))

    def generate(self):
        if self.piece is None:
            self.gen_pick_children()
        else:
            self.gen_play_children()

    def score(self):
        if self.loss:
            return -100000
        elif self.win:
            return 1 * ((self.lookahead + 1) * 100)
        elif self.lookahead == 0 or self.next_states is None:
            return 0
        else:
            total = 0
            for (_, dt) in self.next_states:
                s = dt.score()
                total += dt.score()
            return total

    def determine_best_move(self):
        goat_score = -math.inf
        goat = None
        if self.next_states is None:
            if self.loss:
                # print("cannot win, guessing randomly")
                return None
            else:
                raise ValueError("Tried recurse when there are no valid next states")
        for (move, child) in self.next_states:
            if child.loss: continue
            score = child.score()
            # print(move, "has score", score)
            if goat is None or score > goat_score:
                goat_score = score
                goat = move
        return goat
