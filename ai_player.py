# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:09:51 2020

@author: Dell
"""


# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:31:19 2020

@author: Dell
"""

import random
import math
from board import Board

ROW_SIZE = 6
COL_SIZE = 7

evalArr = [[3, 4, 5, 7, 5, 4, 3], 
        [4, 6, 8, 10, 8, 6, 4],
        [5, 8, 11, 13, 11, 8, 5], 
        [5, 8, 11, 13, 11, 8, 5],
        [4, 6, 8, 10, 8, 6, 4],
        [3, 4, 5, 7, 5, 4, 3]]
class AIPlayer():
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
        row, col, value = self._minimax(board, 5, -math.inf, math.inf, True)
        print(value)
        return board.move(row, col, self.side)
    
    def _calcScore(self,board,piece):
        board_copy = board.board_copy()
        utility = 138
        sum = 0
        for r in range(0,ROW_SIZE):
            for c in range(0,COL_SIZE):
                if board_copy[r][c] == piece:
                    sum=sum+evalArr[r][c]
                if board_copy[r][c] == (3-piece):
                    sum=sum-evalArr[r][c]
        return utility+sum
        
    
    def _winning_move(self,board, piece):
        board_copy = board.board_copy()
        for c in range(0,7):
            for r in range(0,2):
                if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r+1][c] and board_copy[r][c] == board_copy[r+2][c] and board_copy[r][c] == board_copy[r+3][c]:
                    return True
        for c in range(0,3):
            for r in range(0,6):
                if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r][c+1] and board_copy[r][c] == board_copy[r][c+2] and board_copy[r][c] == board_copy[r][c+3]:
                    return True
        for c in range(0,3):
            for r in range(0,2):
                if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r+1][c+1] and board_copy[r][c] == board_copy[r+2][c+2] and board_copy[r][c] == board_copy[r+3][c+3]:
                    return True
        for c in range(0,3):
            for r in range(3,ROW_SIZE):
                if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r-1][c+1] and board_copy[r][c] == board_copy[r-2][c+2] and board_copy[r][c] == board_copy[r-3][c+3]:
                    return True
        return False

    def _count_consecutives(self,board,number,piece):
        board_copy = board.board_copy()
        opp = 3 - piece
        count = 0
        if number == 4:
            for c in range(0,7):
                for r in range(0,2):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r+1][c] and board_copy[r][c] == board_copy[r+2][c] and board_copy[r][c] == board_copy[r+3][c]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r+1][c] and board_copy[r][c] == board_copy[r+2][c] and board_copy[r][c] == board_copy[r+3][c]:
                        count=count-1
            for c in range(0,3):
                for r in range(0,6):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r][c+1] and board_copy[r][c] == board_copy[r][c+2] and board_copy[r][c] == board_copy[r][c+3]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r][c+1] and board_copy[r][c] == board_copy[r][c+2] and board_copy[r][c] == board_copy[r][c+3]:
                        count=count-1
            for c in range(0,3):
                for r in range(0,2):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r+1][c+1] and board_copy[r][c] == board_copy[r+2][c+2] and board_copy[r][c] == board_copy[r+3][c+3]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r+1][c+1] and board_copy[r][c] == board_copy[r+2][c+2] and board_copy[r][c] == board_copy[r+3][c+3]:
                        count=count-1
            for c in range(0,3):
                for r in range(3,ROW_SIZE):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r-1][c+1] and board_copy[r][c] == board_copy[r-2][c+2] and board_copy[r][c] == board_copy[r-3][c+3]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r-1][c+1] and board_copy[r][c] == board_copy[r-2][c+2] and board_copy[r][c] == board_copy[r-3][c+3]:
                        count=count-1
            return count
        if number == 3:
            for c in range(0,7):
                for r in range(0,2):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r+1][c] and board_copy[r][c] == board_copy[r+2][c]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r+1][c] and board_copy[r][c] == board_copy[r+2][c]:
                        count=count-1
            for c in range(0,3):
                for r in range(0,6):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r][c+1] and board_copy[r][c] == board_copy[r][c+2]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r][c+1] and board_copy[r][c] == board_copy[r][c+2]:
                        count=count-1
            for c in range(0,3):
                for r in range(0,2):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r+1][c+1] and board_copy[r][c] == board_copy[r+2][c+2]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r+1][c+1] and board_copy[r][c] == board_copy[r+2][c+2]:
                        count=count-1
            for c in range(0,3):
                for r in range(3,ROW_SIZE):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r-1][c+1] and board_copy[r][c] == board_copy[r-2][c+2]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r-1][c+1] and board_copy[r][c] == board_copy[r-2][c+2]:
                        count=count-1
            return count
        else:
            for c in range(0,7):
                for r in range(0,2):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r+1][c]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r+1][c]:
                        count=count-1
            for c in range(0,3):
                for r in range(0,6):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r][c+1]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r][c+1]:
                        count=count-1
            for c in range(0,3):
                for r in range(0,2):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r+1][c+1]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r+1][c+1]:
                        count=count-1
            for c in range(0,3):
                for r in range(3,ROW_SIZE):
                    if board_copy[r][c] == piece and board_copy[r][c] == board_copy[r-1][c+1]:
                        count=count+1
                    if board_copy[r][c] == opp and board_copy[r][c] == board_copy[r-1][c+1]:
                        count=count-1
            return count
                
    def _deep_copy(self,board):
        board_copy = board.board_copy()
        return board_copy
    
    def _minimax(self, board, depth, alpha, beta, maximizingPlayer):
        placements = self._select_best_move(board)
        #is_terminal = self._is_terminal_node(board,placements)
        if self._winning_move(board, self.side):
            return (None, None,10000)
        if self._winning_move(board, 3-self.side):
            return (None, None, -10000)
        if len(placements) == 0:
            return (None, None, 0)
        if depth == 0:
            return (None, None, self._count_consecutives(board, 4, self.side)*10000 + self._count_consecutives(board, 3, self.side)*100 + self._count_consecutives(board, 2, self.side))
        if maximizingPlayer:
            value = -math.inf
            row_temp, column_temp = random.choice(placements)
            for (row,col) in placements:
                b_copy = self._deep_copy(board)
                b_copy[row][col] = self.side
                b_copy = Board(b_copy)
                new_score = self._minimax(b_copy,depth-1,alpha,beta,False)[2]
                if new_score > value:
                    value = new_score
                    row_temp = row
                    column_temp = col
                alpha = max(alpha,value)
                if alpha>=beta:
                    break
            return row_temp, column_temp, value
        else:
            value = math.inf
            row_temp,column_temp = random.choice(placements)
            for (row,col) in placements:
                b_copy = self._deep_copy(board)
                b_copy[row][col] = self.side
                b_copy = Board(b_copy)
                new_score = self._minimax(b_copy,depth-1,alpha,beta,True)[2]
                if new_score<value:
                    value = new_score
                    row_temp = row
                    column_temp = col
                beta = min(beta,value)
                if alpha>=beta:
                    break
            return row_temp, column_temp, value
            
            
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
                    
        return possible_placements