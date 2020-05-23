# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:16:58 2020

@author: Dell
"""

import sys
from pathlib import Path
sys.path.insert(1, str(Path.cwd()))

from board import Board
from random_player import RandomPlayer
#from AIPlayer import AIPlayer


PLAYER_X = 1
PLAYER_O = 2

def play(board, player1, player2, learn):
    """ Player 1 -> X, X goes first
        player 2 -> O
    """
    player1.set_side(PLAYER_X)
    player2.set_side(PLAYER_O)

    while not board.game_over():
        #board.print_board()
        player1.move(board)
        #board.print_board()
        player2.move(board)

    if learn == True:
        player1.learn(board)
        player2.learn(board)

    return board.game_result



def battle(board, player1, player2, iter, learn=False, show_result=True):
    p1_stats = [0, 0, 0] # draw, win, lose
    for i in range(0, iter):
        result = play(board, player1, player2, learn)
        p1_stats[result] += 1
        board.reset()

    p1_stats = [round(x / iter * 100.0, 1) for x in p1_stats]
    if show_result:
        print('_' * 60)
        print('{:>15}(X) | Wins:{}% Draws:{}% Losses:{}%'.format(player1.__class__.__name__, p1_stats[1], p1_stats[0], p1_stats[2]).center(50))
        print('{:>15}(O) | Wins:{}% Draws:{}% Losses:{}%'.format(player2.__class__.__name__, p1_stats[2], p1_stats[0], p1_stats[1]).center(50))
        print('_' * 60)
        print()

    return p1_stats


if __name__ == "__main__":

    # Example Usage
    # battle(Board(show_board=True, show_result=True), RandomPlayer(), RandomPlayer(), 1, learn=False, show_result=True)
    # battle(Board(), RandomPlayer(), RandomPlayer(), 100, learn=False, show_result=True)
    # battle(Board(), RandomPlayer(), SmartPlayer(), 100, learn=False, show_result=True)
    # battle(Board(), RandomPlayer(), PerfectPlayer(), 100, learn=False, show_result=True)
    # battle(Board(), SmartPlayer(), PerfectPlayer(), 100, learn=False, show_result=True)

   # qlearner = QLearner()
    #NUM = qlearner.GAME_NUM

    # train: play NUM games against players who only make random moves
    board = Board(show_board=True, show_result=True)
    #battle(board, RandomPlayer(), RandomPlayer(), 10, learn=False, show_result=False)
    #battle(board, qlearner, RandomPlayer(), NUM, learn=True, show_result=False)

    # test: play 1000 games against each opponent
    print('Playing QLearner against RandomPlayer for 10 times......')
    q_rand = battle(board, RandomPlayer(), RandomPlayer(), 50)
    rand_q = battle(board, RandomPlayer(), RandomPlayer(), 50)
    #print('Playing QLearner against SmartPlayer for 1000 times......')
    #q_smart = battle(board, qlearner, SmartPlayer(), 500)
    #smart_q = battle(board, SmartPlayer(), qlearner, 500)
    #print('Playing QLearner against PerfectPlayer for 1000 times......')
    #q_perfect = battle(board, qlearner, PerfectPlayer(), 500)
    #perfect_q = battle(board, PerfectPlayer(), qlearner, 500)

    # summarize game results
    winning_rate_w_random_player  = round(100 -  (q_rand[2] + rand_q[1]) / 2, 2)
    
    print("Summary:")
    print("_" * 60)
    print("QLearner VS  RandomPlayer |  Win/Draw Rate = {}%".format(winning_rate_w_random_player))
    print("_" * 60)

    grade = 0
    
#   output_file = sys.argv[1]
#    with open(output_file, 'w') as f:
#        f.write(str(grade) + '\n')

