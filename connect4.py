# coding=utf-8
__author__ = 'Israel Estévez Hatchuell'

import games
import heu

def next_state(state, game):
    while True:
        try:
            column = int(raw_input("Select a column into the range: "))
            break
        except ValueError:
            print "ATENTION: This input is not a valid number, try again!"
    return game.make_move(column, state)


game = games.ConnectFour()
state = game.initial
player = game.to_move(state)

welcome = "New Game of {0} and begin the player {1}"
print welcome.format(game, player).center(80, "*")

while True:
    print "It's up to: ", game.to_move(state)
    print "Legal moves: ", game.legal_moves(state)
    if player == 'X':
        move = games.alphabeta_search(state, game, d=2, eval_fn=heu.heuristic1)
        state = game.make_move(move, state)
        player = game.to_move(state)
    else:
        state = next_state(state, game)
        player = game.to_move(state)
    game.display(state)
    print "-------------------"
    if game.terminal_test(state):
        winner = game.to_move(state)
        if winner == 'X':
            winner = 'O'
        else:
            winner = 'X'
        print "Final de la partida, el ganador es: ", winner
        break


# x = 0
# o = 0
#
# for i in range(10):
#     game = games.ConnectFour()
#     state = game.initial
#     player = game.to_move(state)
#     while True:
#         if player == 'X':
#             move = games.alphabeta_search(state, game, eval_fn=heu.heuristic1)
#             state = game.make_move(move, state)
#             player = game.to_move(state)
#         else:
#             move = games.alphabeta_search(state, game, eval_fn=heu.heuristic2)
#             state = game.make_move(move, state)
#             # state = next_state(state, game)
#             player = game.to_move(state)
#         game.display(state)
#         print "-------------------"
#         if game.terminal_test(state):
#             winner = game.to_move(state)
#             if winner == 'X':
#                 winner = 'O'
#                 o += 1
#             else:
#                 winner = 'X'
#                 x += 1
#             print "Final de la partida, el ganador es: ", winner
#             break
# print "Total de veces ganadas X: ", x
# print "Total de veces ganadas O: ", o

