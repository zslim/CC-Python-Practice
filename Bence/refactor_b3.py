tictactoe_board = [' '] * 9
# tictactoe_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

game_ended = False


def player_1_move(board):
    placement = input('\33[34m' + 'Player1 (X), choose a number: ' + '\33[0m')
    if placement.isdigit() is False or int(placement) < 1 or int(placement) > 9:
        print('\33[33m' + "Enter a number between 1 and 9!" + '\33[0m')
        player_1_move(board)
    elif board[int(placement)-1] == 'X' or board[int(placement)-1] == 'O':
        print('\33[33m' + "You can't place it there!" + '\33[0m')
        player_1_move(board)
    else:
        board[int(placement)-1] = 'X'


def player_2_move(board):
    placement = input('\33[31m' + 'Player2 (O), choose a number: ' + '\33[0m')
    if placement.isdigit() is False or int(placement) < 1 or int(placement) > 9:
        print('\33[33m' + "Enter a number between 1 and 9!" + '\33[0m')
        player_2_move(board)
    elif board[int(placement)-1] == 'X' or board[int(placement)-1] == 'O':
        print('\33[33m' + "You can't place it there!" + '\33[0m')
        player_2_move(board)
    else:
        board[int(placement)-1] = 'O'


def draw_board(board):
    print(' ' + board[0], '|', board[1], '|', board[2])
    print('-----------')
    print(' ' + board[3], '|', board[4], '|', board[5])
    print('-----------')
    print(' ' + board[6], '|', board[7], '|', board[8])


def check_for_game_end(board):
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] == 'X':
            print('\33[34m' + "Player 1 won the game!" + '\33[0m')
            return True
        elif board[i] == board[i+1] == board[i+2] == 'O':
            print('\33[31m' + "Player 2 won the game!" + '\33[0m')
            return True

    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == 'X':
            print('\33[34m' + "Player 1 won the game!" + '\33[0m')
            return True
        elif board[i] == board[i+3] == board[i+6] == 'O':
            print('\33[31m' + "Player 2 won the game!" + '\33[0m')
            return True

    if board[0] == board[4] == board[8] == 'X' or board[6] == board[4] == board[2] == 'X':
        print('\33[34m' + "Player 1 won the game!" + '\33[0m')
        return True
    elif board[0] == board[4] == board[8] == 'O' or board[6] == board[4] == board[2] == 'O':
        print('\33[31m' + "Player 2 won the game!" + '\33[0m')
        return True

    if board.count('X') + board.count('O') == 9:
        print('\33[32m' + "The game ended in a draw!" + '\33[0m')
        return True


draw_board(tictactoe_board)
print('\n')
while not game_ended:
    player_1_move(tictactoe_board)
    print('\n')
    draw_board(tictactoe_board)
    print('\n')
    game_ended = check_for_game_end(tictactoe_board)
    if game_ended:
        break
    player_2_move(tictactoe_board)
    print('\n')
    draw_board(tictactoe_board)
    print('\n')
    game_ended = check_for_game_end(tictactoe_board)
    if game_ended:
        break
