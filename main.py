import random


# is_valid_move
# input: player move (player_a_move or player_b_move)
# output: boolean (True or False) <2>
# function: checks if player move is valid
def is_valid_move(a):
    valid = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    for i in valid:
        if a == i and board[a] == 'none':
            return True
    else:
        return False


# is_game_over
# input: none
# output: boolean, string ( (True) or (True, "Draw") or False) <3>
# function: checks if game is over
def is_game_over():
    conditions = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'],
                  ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]
    for condition in conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == '  X ':
            return (True, "X")
    for condition in conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == '  O ':
            return (True, "O")
    if board['A1'] != 'none' and board['A2'] != 'none' and board['A3'] != 'none' and board['B1'] != 'none' and board[
        'B2'] != 'none' and board['B3'] != 'none' and board['C1'] != 'none' and board['C2'] != 'none' and board[
        'C3'] != 'none':
        return (True, "Draw")
    else:
        return False


# print_board
# input: none
# output: print statements for board
# function: prints board with current standings
def print_board():
    print(' ')
    print(board['C1'] + '|' + board['C2'] + '|' + board['C3'])
    print('--------------')
    print(board['B1'] + '|' + board['B2'] + '|' + board['B3'])
    print('--------------')
    print(board['A1'] + '|' + board['A2'] + '|' + board['A3'])
    print(' ')


# get_computer_move
# input: none
# output: computer move
# function: returns bot move
def get_computer_move():
    dict1 = {'A1': [['A2', 'A3'], ['C1', 'B1'], ['B2', 'C3']],
              'A3': [['A1', 'A2'], ['C3', 'B3'], ['C1', 'B2']],
              'C1': [['C2', 'C3'], ['A1', 'B1'], ['B2', 'A3']],
              'C3': [['C1', 'C2'], ['A3', 'B3'], ['A1', 'B2']]
              }
    dict2 = {'A2': [['A1', 'A3'], ['C2', 'B2']],
             'B1': [['B2', 'B3'], ['A1', 'C1']],
             'B3': [['B1', 'B2'], ['C3', 'A3']],
             'C2': [['C1', 'C3'], ['A2', 'B2']]
             }
    dict3 = {'B2': [['B1', 'B3'], ['C2', 'A2'], ['C1', 'A3'], ['C3', 'A1']]}
    for move in dict1:
        for positions in dict1[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  X ':
                if is_valid_move(move) == True:
                    return move

    for move in dict2:
        for positions in dict2[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  X ':
                if is_valid_move(move) == True:
                    return move

    for move in dict3:
        for positions in dict3[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  X ':
                if is_valid_move(move) == True:
                    return move

    for move in dict1:
        for positions in dict1[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  O ':
                if is_valid_move(move) == True:
                    return move

    for move in dict2:
        for positions in dict2[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  O ':
                if is_valid_move(move) == True:
                    return move

    for move in dict3:
        for positions in dict3[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  O ':
                if is_valid_move(move) == True:
                    return move

    if board['C3'] == '  X ' and board['B2'] == '  O ' and board['A1'] == 'none':
        return 'A1'
    if board['A1'] == '  X ' and board['B2'] == '  O ' and board['C3'] == 'none':
        return 'C3'
    if board['C1'] == '  X ' and board['B2'] == '  O ' and board['A3'] == 'none':
        return 'A3'
    if board['A3'] == '  X ' and board['B2'] == '  O ' and board['C1'] == 'none':
        return 'C1'

    if board['C2'] == board['B1'] == '  O ' or board['C2'] == board['B3'] == '  O ' or board['B3'] == board[
        'A2'] == '  O ' or board['A2'] == board['B1'] == '  O ' or board['B1'] == board['C2'] == '  O ' and board[
        'B2'] == 'none':
        return 'B2'

    move = random_move(['A1', 'A3', 'C1', 'C3'])
    if move != None:
        return move
    if is_valid_move('B2') == True:
        return 'B2'
    move = random_move(['A2', 'B1', 'B3', 'C2'])
    if move != None:
        return move


# get_computer_move_o
# input: none
# output: computer move
# function: returns bot move
def get_computer_move_o():
    dict1 = {'A1': [['A2', 'A3'], ['C1', 'B1'], ['B2', 'C3']],
              'A3': [['A1', 'A2'], ['C3', 'B3'], ['C1', 'B2']],
              'C1': [['C2', 'C3'], ['A1', 'B1'], ['B2', 'A3']],
              'C3': [['C1', 'C2'], ['A3', 'B3'], ['A1', 'B2']]
              }
    dict2 = {'A2': [['A1', 'A3'], ['C2', 'B2']],
             'B1': [['B2', 'B3'], ['A1', 'C1']],
             'B3': [['B1', 'B2'], ['C3', 'A3']],
             'C2': [['C1', 'C3'], ['A2', 'B2']]
             }
    dict3 = {'B2': [['B1', 'B3'], ['C2', 'A2'], ['C1', 'A3'], ['C3', 'A1']]}
    for move in dict1:
        for positions in dict1[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  O ':
                if is_valid_move(move) == True:
                    return move

    for move in dict2:
        for positions in dict2[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  O ':
                if is_valid_move(move) == True:
                    return move

    for move in dict3:
        for positions in dict3[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  O ':
                if is_valid_move(move) == True:
                    return move

    for move in dict1:
        for positions in dict1[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  X ':
                if is_valid_move(move) == True:
                    return move

    for move in dict2:
        for positions in dict2[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  X ':
                if is_valid_move(move) == True:
                    return move

    for move in dict3:
        for positions in dict3[move]:

            p0 = positions[0]
            p1 = positions[1]
            if board[p0] == board[p1] == '  X ':
                if is_valid_move(move) == True:
                    return move

    # X starts from corner
    if board['C1'] == '  X ' and board['A3'] == '  X ' and board['B2'] == '  O ' and board['A1'] == 'none' and board[
        'A2'] == 'none' and board['B1'] == 'none' and board['B3'] == 'none' and board['C2'] == 'none' and board[
        'C3'] == 'none' or board['C3'] == '  X ' and board['A1'] == '  X ' and board['B2'] == '  O ' and board[
        'A3'] == 'none' and board['A2'] == 'none' and board['B1'] == 'none' and board['B3'] == 'none' and board[
        'C2'] == 'none' and board['C1'] == 'none':
        return 'B3'
    if board['C1'] == '  X ' and board['B3'] == '  X ' and board['B2'] == '  O ' and board['A1'] == 'none' and board[
        'A2'] == 'none' and board['A3'] == 'none' and board['B1'] == 'none' and board['C2'] == 'none' and board[
        'C3'] == 'none' or board['A3'] == '  X ' and board['C2'] == '  X ' and board['B2'] == '  O ' and board[
        'A1'] == 'none' and board['A2'] == 'none' and board['B1'] == 'none' and board['B3'] == 'none' and board[
        'C3'] == 'none' and board['C1'] == 'none':
        return 'C3'
    if board['A3'] == '  X ' and board['B1'] == '  X ' and board['B2'] == '  O ' and board['A1'] == 'none' and board[
        'A2'] == 'none' and board['B3'] == 'none' and board['C1'] == 'none' and board['C2'] == 'none' and board[
        'C3'] == 'none' or board['C1'] == '  X ' and board['A2'] == '  X ' and board['B2'] == '  O ' and board[
        'A1'] == 'none' and board['B1'] == 'none' and board['B3'] == 'none' and board['A3'] == 'none' and board[
        'C2'] == 'none' and board['C3'] == 'none':
        return 'A1'
    if board['C3'] == '  X ' and board['A2'] == '  X ' and board['B2'] == '  O ' and board['A1'] == 'none' and board[
        'B1'] == 'none' and board['B3'] == 'none' and board['A3'] == 'none' and board['C2'] == 'none' and board[
        'C1'] == 'none' or board['A1'] == '  X ' and board['B3'] == '  X ' and board['B2'] == '  O ' and board[
        'C3'] == 'none' and board['B1'] == 'none' and board['A2'] == 'none' and board['A3'] == 'none' and board[
        'C2'] == 'none' and board['C1'] == 'none':
        return 'A3'
    if board['C3'] == '  X ' and board['B1'] == '  X ' and board['B2'] == '  O ' and board['A1'] == 'none' and board[
        'A2'] == 'none' and board['B3'] == 'none' and board['C1'] == 'none' and board['C2'] == 'none' and board[
        'C3'] == 'none' or board['A1'] == '  X ' and board['C2'] == '  X ' and board['B2'] == '  O ' and board[
        'A2'] == 'none' and board['B1'] == 'none' and board['B3'] == 'none' and board['A3'] == 'none' and board[
        'C1'] == 'none' and board['C3'] == 'none':
        return 'C1'

    if is_valid_move('B2') == True:
        return 'B2'
    move = random_move(['A1', 'A3', 'C1', 'C3'])
    if move != None:
        return move
    move = random_move(['A2', 'B1', 'B3', 'C2'])
    if move != None:
        return move


# random_move
# input: list of spaces (corner spaces or side spaces)
# output: random free space that is part of input list
# function: returns random free space that is part of input list
def random_move(moves_list):
    possible_moves = []
    for i in moves_list:
        if is_valid_move(i) == True:
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


# main function
board = {}
board["A1"] = "none"
board["A2"] = "none"
board["A3"] = "none"
board["B1"] = "none"
board["B2"] = "none"
board["B3"] = "none"
board["C1"] = "none"
board["C2"] = "none"
board["C3"] = "none"

which_version = raw_input("Do you want to play against the bot (b) or another player (p)?: ")
while which_version != 'b' and which_version != 'p':
    which_version = raw_input("Do you want to play against the bot (b) or another player (p)?: ")
if which_version == 'b':
    first_player = raw_input("Do you want to go first (f) or second (s)?: ")
    while first_player != 'f' and first_player != 's':
        first_player = raw_input("Do you want to go first (f) or second (s)?: ")
    if first_player == 'f':
        player_a = "The bot"
        player_b = raw_input("Please enter your name: ")

        print(' ')
        print(' C1 ' + '|' + ' C2 ' + '|' + ' C3 ')
        print('--------------')
        print(' B1 ' + '|' + ' B2 ' + '|' + ' B3 ')
        print('--------------')
        print(' A1 ' + '|' + ' A2 ' + '|' + ' A3 ')
        print(' ')

        for i in range(9):
            while (True):
                player_b_move = raw_input(player_b + ", what is your move? ")
                result = is_valid_move(player_b_move)
                if result == (False):
                    print(player_b + ", please redo your move: ")
                if result == (True):
                    board[player_b_move] = '  X '
                    print_board()
                    game = is_game_over()
                    if game == (True, "X"):
                        print(player_b + " has won.")
                        quit()
                    else:
                        if game == (True, "Draw"):
                            print("Draw; game over.")
                            quit()
                        else:
                            break
            while (True):
                player_a_move = get_computer_move_o()
                board[player_a_move] = '  O '
                print("Bot's move:")
                print_board()
                game = is_game_over()
                if game == (True, "O"):
                    print(player_a + " has won.")
                    quit()
                else:
                    if game == (True, "Draw"):
                        print("Draw; game over.")
                        quit()
                    else:
                        break
    if first_player == 's':
        player_a = "The bot"
        player_b = raw_input("Please enter your name: ")

        print(' ')
        print(' C1 ' + '|' + ' C2 ' + '|' + ' C3 ')
        print('--------------')
        print(' B1 ' + '|' + ' B2 ' + '|' + ' B3 ')
        print('--------------')
        print(' A1 ' + '|' + ' A2 ' + '|' + ' A3 ')
        print(' ')

        for i in range(9):
            while (True):
                player_a_move = get_computer_move()
                board[player_a_move] = '  X '
                print("Bot's move:")
                print_board()
                game = is_game_over()
                if game == (True, "X"):
                    print(player_a + " has won.")
                    quit()
                else:
                    if game == (True, "Draw"):
                        print("Draw; game over.")
                        quit()
                    else:
                        break
            while (True):
                player_b_move = raw_input(player_b + ", what is your move? ")
                result = is_valid_move(player_b_move)
                if result == (False):
                    print(player_b + ", please redo your move: ")
                if result == (True):
                    board[player_b_move] = '  O '
                    print_board()
                    game = is_game_over()
                    if game == (True, "O"):
                        print(player_b + " has won.")
                        quit()
                    else:
                        if game == (True, "Draw"):
                            print("Draw; game over.")
                            quit()
                        else:
                            break
if which_version == 'p':
    player_a = raw_input("Player A, please enter your name: ")
    player_b = raw_input("Player B, please enter your name: ")
    while player_b == player_a:
        player_b = raw_input("Player B, please enter another name: ")

    print(' ')
    print(' C1 ' + '|' + ' C2 ' + '|' + ' C3 ')
    print('--------------')
    print(' B1 ' + '|' + ' B2 ' + '|' + ' B3 ')
    print('--------------')
    print(' A1 ' + '|' + ' A2 ' + '|' + ' A3 ')
    print(' ')

    for i in range(9):
        while (True):
            player_a_move = raw_input(player_a + ", what is your move? ")
            result = is_valid_move(player_a_move)
            if result == (False):
                print(player_a + ", please redo your move: ")
            if result == (True):
                board[player_a_move] = '  X '
                print_board()
                game = is_game_over()
                if game == (True, "X"):
                    print(player_a + " has won.")
                    quit()
                else:
                    if game == (True, "Draw"):
                        print("Draw; game over.")
                        quit()
                    else:
                        break
        while (True):
            player_b_move = raw_input(player_b + ", what is your move? ")
            result = is_valid_move(player_b_move)
            if result == (False):
                print(player_b + ", please redo your move: ")
            if result == (True):
                board[player_b_move] = '  O '
                print_board()
                game = is_game_over()
                if game == (True, "O"):
                    print(player_b + " has won.")
                    quit()
                else:
                    if game == (True, "Draw"):
                        print("Draw; game over.")
                        quit()
                    else:
                        break