# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:10:53 2020
@author: Dell
"""
import numpy as np

ROW_SIZE = 6
COL_SIZE = 7

ONGOING = -1
DRAW = 0
X_WIN = 1
O_WIN = 2


class Board:

    def __init__(self, state=None, show_board=False, show_result=False):
        """ board cell:
                Empty -> 0
                X -> 1
                O -> 2
        """
        if state is None:
            self.state = np.zeros((ROW_SIZE+1, COL_SIZE), dtype=np.int)
            for i in range(0,7):
                self.state[6][i] = 3
        else:
            self.state = state.copy()
        self.game_result = ONGOING
        self.show_board  = show_board
        self.show_result = show_result

    def set_show_board(self, show_board):
        self.show_board = show_board
    
    def board_copy(self):
        state_copy = np.zeros((ROW_SIZE, COL_SIZE), dtype=np.int)
        for i in range(0,ROW_SIZE):
            for j in range(0,COL_SIZE):
                state_copy[i][j] = self.state[i][j]        
        return state_copy           

    def encode_state(self):
        """ Encode the current state of the board as a string
        """
        return ''.join([str(self.state[i][j]) for i in range(ROW_SIZE) for j in range(COL_SIZE)])

    def reset(self):
        self.state.fill(0)
        self.game_result = ONGOING

    def is_valid_move(self, row, col):
        if(row == 0):
            return col < COL_SIZE and col >=0 and self.state[row][col] == 0 and self.state[row+1][col] != 0
        if(row == ROW_SIZE-1):
            return col < COL_SIZE and col >=0 and self.state[row][col] == 0 and self.state[row-1][col] == 0
        return row < ROW_SIZE and row >= 0 and col < COL_SIZE and col >=0 and self.state[row][col] == 0 and self.state[row-1][col] == 0 and self.state[row+1][col] != 0

    def move(self, row, col, player):
        """
        Parameters
        ----------
        row : 0, 1, 2
        col : 0, 1, 2
        player: X -> 1, O -> 2

        Returns
        -------
        state: state after the move
        result: game result after the move
        """
        if not self.is_valid_move(row, col):
            print (row, col)
            self.print_board()
            raise ValueError("Invalid Move")

        self.state[row][col] = player
        self.game_result = self._check_winner()

        if self.show_board:
            p = 'X' if player == 1 else 'O'
            print('player {} moved: {}, {}'.format(p, row, col))
            self.print_board()

        if self.show_result:
            self.game_result_report()

        return self.state, self.game_result

    def game_over(self):
        return self.game_result != ONGOING


    def print_board(self):
        board = self.encode_state()
        board = board.replace('0', ' ')
        board = board.replace('1', 'X')
        board = board.replace('2', 'O')
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('--- --- --- --- --- --- ---')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ' + board[10] + ' | ' + board[11] + ' | ' + board[12] + ' | ' + board[13])
        print('--- --- --- --- --- --- ---')
        print(' ' + board[14] + ' | ' + board[15] + ' | ' + board[16]+ ' | ' + board[17] + ' | ' + board[18]+ ' | ' + board[19] + ' | ' + board[20])
        print('--- --- --- --- --- --- ---')
        print(' ' + board[21] + ' | ' + board[22] + ' | ' + board[23]+ ' | ' + board[24] + ' | ' + board[25]+ ' | ' + board[26] + ' | ' + board[27])
        print('--- --- --- --- --- --- ---')
        print(' ' + board[28] + ' | ' + board[29] + ' | ' + board[30]+ ' | ' + board[31] + ' | ' + board[32]+ ' | ' + board[33] + ' | ' + board[34])
        print('--- --- --- --- --- --- ---')
        print(' ' + board[35] + ' | ' + board[36] + ' | ' + board[37]+ ' | ' + board[38] + ' | ' + board[39]+ ' | ' + board[40] + ' | ' + board[41])
        print()

    def game_result_report(self):
        if self.game_result is ONGOING:
            return
        print ('=' * 30)
        if self.game_result is DRAW:
            print ('Game Over : Draw'.center(30))
        elif self.game_result is X_WIN:
            print ('Game Over : Winner X'.center(30))
        elif self.game_result is O_WIN:
            print ('Game Over : Winner O'.center(30))
        print ('=' * 30)

    def _check_winner(self):
        # check each row and column
        for c in range(0,6):
            for r in range(0,4):
                if self.state[r][c] > 0 and self.state[r][c]!=3 and self.state[r][c] == self.state[r+1][c] and self.state[r][c] == self.state[r+2][c] and self.state[r][c] == self.state[r+3][c]:
                    return X_WIN if self.state[r][c] == 1 else O_WIN
        for c in range(0,3):
            for r in range(0,7):
                if self.state[r][c] > 0 and self.state[r][c]!=3 and self.state[r][c] == self.state[r][c+1] and self.state[r][c] == self.state[r][c+2] and self.state[r][c] == self.state[r][c+3]:
                    return X_WIN if self.state[r][c] == 1 else O_WIN
        for c in range(0,3):
            for r in range(0,4):
                if self.state[r][c] > 0 and self.state[r][c]!=3 and self.state[r][c] == self.state[r+1][c+1] and self.state[r][c] == self.state[r+2][c+2] and self.state[r][c] == self.state[r+3][c+3]:
                    return X_WIN if self.state[r][c] == 1 else O_WIN
        for c in range(0,3):
            for r in range(3,ROW_SIZE):
                if self.state[r][c] > 0 and self.state[r][c]!=3 and self.state[r][c] == self.state[r-1][c+1] and self.state[r][c] == self.state[r-2][c+2] and self.state[r][c] == self.state[r-3][c+3]:
                    return X_WIN if self.state[r][c] == 1 else O_WIN
        # draw
        count = 0
        for r in range(0,7):
            for c in range(0,6):
                if self.state[r][c]==0:
                    count=count+1
        if count == 0:
            return DRAW
        return ONGOING



