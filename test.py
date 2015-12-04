# coding=utf-8
__author__ = 'Israel Estévez Hatchuell'


def heuristic1(state):
    """ ... """

    if state.utility != 0:
        return state.utility * infinity
    aux = 0
    maximum_X = 0
    maximum_O = 0
    for move, player in state.board.iteritems():
        aux += (num_in_row(state.board, move, player, (0, 1)))
        aux += (num_in_row(state.board, move, player, (1, 0)))
        aux += (num_in_row(state.board, move, player, (1, -1)))
        aux += (num_in_row(state.board, move, player, (1, 1)))
        if player == 'X':
            maximum_X += aux
        else:
            maximum_O += aux
        aux = 0
    print maximum_X - maximum_O
    return maximum_X - maximum_O


def num_in_row(board, move, player, (delta_x, delta_y)):
    """Return true if there is a line through move on board for player."""
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player:
        n += 1
        x, y = x + delta_x, y + delta_y
    # if board.get((x, y)) is not None:
    #     n -= 1
    x, y = move
    while board.get((x, y)) == player:
        n += 1
        x, y = x - delta_x, y - delta_y
    # if board.get((x, y)) is not None:
    #     n -= 1
    n -= 1  # Because we counted move itself twice
    return n
