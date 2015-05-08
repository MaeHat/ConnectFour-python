# coding=utf-8
__author__ = 'Israel Estévez Hatchuell'
from utils import *
import random


def get_advantage_player(state):
    """ ... """
    max_in_row = {}
    maximum_X = 0
    maximum_O = 0
    for move, player in state.board.iteritems():
        max_in_row[(num_in_row(state.board, move, player, (0, 1)))] = player
        max_in_row[(num_in_row(state.board, move, player, (1, 0)))] = player
        max_in_row[(num_in_row(state.board, move, player, (1, -1)))] = player
        max_in_row[(num_in_row(state.board, move, player, (1, 1)))] = player
    for key, player in max_in_row.iteritems():
        if player == 'X' and key > maximum_X:
            if key >= 4:
                # print ' Ganaba la x en ', state.board
                return 1000
            else:
                maximum_X = key
        elif key > maximum_O:
            if key >= 3:
                # print ' Ganaba el 0 en ', state.board
                return -1000
            else:
                maximum_O = key
    # print maximum_X, ' en linea para x, ', maximum_O, ' en linea para 0 '
    return maximum_X - maximum_O


def num_in_row(board, move, player, (delta_x, delta_y)):
    """Return true if there is a line through move on board for player."""
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y
    if board.get((x, y)) is not None:
        n -= 1
    x, y = move
    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y
    if board.get((x, y)) is not None:
        n -= 1
    n -= 1  # Because we counted move itself twice
    return n


def heuristic1(state):
    """ This heuristic give us ... """
    h = get_advantage_player(state)
    # print "Tablero en este estado: ", state.board
    # print "Ventaja de X sobre O: ", h
    # print "Ventaja: ", h
#    print "Heurística para X en este nodo: ", h
    return h


def heuristic2(state):
    return random.randint(0, 4)
