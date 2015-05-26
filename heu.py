# coding=utf-8
__author__ = 'Israel Estévez Hatchuell'
from utils import *
import random


def heuristic(state):
    """ Return difference between 'X' - 'O' """
    if state.utility != 0:
        return state.utility * infinity

    maximum_X = 0
    maximum_O = 0
    aux = 0
    for move, player in state.board.iteritems():
        aux += (num_in_row(state.board, move, player, (0, 1)))
        aux += (num_in_row(state.board, move, player, (1, 0)))
        aux += (num_in_row(state.board, move, player, (1, -1)))
        aux += (num_in_row(state.board, move, player, (1, 1)))
        if player == 'X':
            maximum_X += aux
        elif player == 'O':
            maximum_O += aux
        aux = 0

    return maximum_X - maximum_O


def num_in_row(board, move, player, (delta_x, delta_y)):
    """Return true if there is a line through move on board for player."""
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player or board.get((x, y)) is None and 1 < y < 7 and 1 <= x <= 6:
        n += 1
        x, y = x + delta_x, y + delta_y
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) is None and 1 < y < 7 and 1 <= x <= 6:
        n += 1
        x, y = x - delta_x, y - delta_y
    n -= 1  # Because we counted move itself twice
    return n
