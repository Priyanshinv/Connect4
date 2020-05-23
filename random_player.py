# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:31:19 2020

@author: Dell
"""


import random

ROW_SIZE = 6
COL_SIZE = 7

class RandomPlayer():
    def __init__(self, side=None):
        self.type = 'random'
        self.side = side
        
    def set_side(self, side):
        self.side = side
        
    def move(self, board):
        """ make a move
        """
        if board.game_over():
            return
        row, col = self._select_best_move(board)
        return board.move(row, col, self.side)
    
    def _select_best_move(self, board):
        possible_placements = []
        board_copy = board.board_copy()
        for i in range(0,ROW_SIZE):
            for j in range(0,COL_SIZE):
                if board_copy[i][j] == 0:
                    if i == 0:
                        if board_copy[i+1][j] != 0:
                            possible_placements.append((i,j))
                    elif i == ROW_SIZE-1:
                        if board_copy[i-1][j] == 0:
                            possible_placements.append((i,j))
                    else:
                        if board_copy[i-1][j] == 0 and board_copy[i+1][j] !=0:
                            possible_placements.append((i,j))
                    
        return random.choice(possible_placements)