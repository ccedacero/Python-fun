def clear():
    os.system( 'cls' )


def display_board(board):
    clear()
    print(board[7]+ ' | ' + board[8] + ' | ' + board[9])
    print(board[4]+ ' | ' + board[5] + ' | ' + board[6])
    print(board[1]+ ' | ' + board[2] + ' | ' + board[3])



def player_input():
    marker = 'a'
    while not(marker == 'X' or  marker == 'O'):
      marker = input('Please choose whether you want to play as X or O:__').upper()
    return('X','O') if marker == 'X' else ('O','X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 



import random

def choose_first():
    tur = random.randint(0,1)
    return 'Player1' if tur == 0 else 'Player2'


def space_check(board,position):
   return True if board[position] == ' ' else False



def full_board_check(board):
    filtered_board = len(list(filter(lambda s: s == ' ', board)))
    print(filtered_board)
    return True if filtered_board <= 1 else False 


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))    
    return position


def replay():
    again = input('Play again? Yes : No ?' ).upper()
    return True if again == 'YES' or again == 'Y' else False




print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Yes or No ?')
    print(play_game)
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break