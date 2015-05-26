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


def difficulty():
    while True:
        try:
            dif = int(raw_input("Choose difficulty you are willing to tolerate (Easy=1, Medium=2, Hard=3): "))
            if dif == 1:
                return 0
            elif dif == 2:
                return 2
            elif dif == 3:
                return 4
        except ValueError:
            print "Write 1 to easy, 2 to medium or 3 to hard level!"


def players():
    while True:
        answer = raw_input("Would you like the computer as your adversary?(yes/no): ")
        if answer == 'yes':
            return True
        elif answer == 'no':
            print "Ok, you will play with your friend. Enjoy!"
            return False
        print "Just write yes or no!"

game = games.ConnectFour()
state = game.initial
player = game.to_move(state)
welcome = "New Game of {0} and begin the player {1}"
print welcome.format(game, player).center(80, "*")
adversary_computer = players()
if adversary_computer:
    depth = difficulty()


while True:
    print "It's up to: ", game.to_move(state)
    print "Legal moves: ", game.legal_moves(state)
    if player == 'X':
        if adversary_computer:
            move = games.alphabeta_search(state, game, d=depth, eval_fn=heu.heuristic)
            state = game.make_move(move, state)
        else:
            state = next_state(state, game)
    else:
        state = next_state(state, game)
    game.display(state)
    print "-------------------"
    if game.terminal_test(state):
        if state.utility != 0:
            print "The winner is: ", player
        else:
            print "Draw!"
        break
    player = game.to_move(state)
