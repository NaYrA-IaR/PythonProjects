from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print(board[1]+'  |'+board[2]+'  |'+board[3])
    print('---|---|---')
    print(board[4]+'  |'+board[5]+'  |'+board[6])
    print('---|---|---')
    print(board[7]+'  |'+board[8]+'  |'+board[9])
    
def player_input():
    
    #Ask for player 1's marker i.e. either 'X' or 'O'
    
    choice=''
    
    while choice != 'X' and choice != 'O':
        choice=input("Player 1 choose your marker('X' or 'O'): ")
        
    player1 = choice
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return(player1,player2)

def place_marker(board,marker,position):
    
    board[position]=marker

def win_check(board,mark):
    
    #Function to check who won
    
    if ( board[1] == mark and board[2] == mark and board[3] == mark ) or ( board[1] == mark and board[4] == mark and board[7] == mark ) or ( board[1] == mark and board[5] == mark and board[9] == mark ) or ( board[2] == mark and board[5] == mark and board[8] == mark ) or ( board[3] == mark and board[5] == mark and board[7] == mark ) or ( board[3] == mark and board[6] == mark and board[9] == mark ) or ( board[4] == mark and board[5] == mark and board[6] == mark ) or ( board[7] == mark and board[8] == mark and board[9] == mark ):
        
        return True
    
    else:
    
        return False
    
import random

def choose_first():
    
    #To decide which player goes first
    
    first_chance=random.randint(1,2)
    return first_chance

def space_check(board,position):
    
    #To check if the given position is available on the board
    
    if board[position] != ' ':
        
        return False
    
    else:
        
        return True

def full_board_check(board):
    
    #Checking if the board is full
    
    for posi in range(1,10):
        
        if space_check(board,posi):
            
            return False
        
    else:
        print("This game is a draw!!")
        return True
    
def player_choice(board):

    choice=False
    
    # To get the position(1-9)
    
    while choice!=True:
    
    #
    
        position=int(input("Enter a postion(1-9): "))
        if position in range(1,10):
            
            rand_var=space_check(board,position)
            if rand_var == False:
                continue
            else:
                return position

def replay():
    
    choice=False
    
    while choice!=True:
        accept=input("Do you want to play again?(Y or N): ")
        if accept.lower() == 'y':
            return True
        elif accept.lower() == 'n':
            print("Thank You for playing the game!!\n Hope you enjoyed it")
            return False
        else:
            continue
            
print("Welcome to TicTacToe")
print("Rules:\nThe board is like a numpad i.e.1 at the top left and 9 at bottom right\nThe first person to have the same marker at three consecutive spaces wins the game i.e. vertically , horizontally or diagonally\n The board is like------------->")

print('1'+'  |'+'2'+'  |'+'3')
print('---|---|---')
print('4'+'  |'+'5'+'  |'+'6')
print('---|---|---')
print('7'+'  |'+'8'+'  |'+'9')
choice = True


while choice == True:
    board=[' ']*10
    
    player1_marker,player2_marker = player_input()
    chance=choose_first()
    
    while True:
        # Chance is random .
        if chance == 1:
            print("Player 1 it's your turn...")
            position = player_choice(board)
            place_marker(board,player1_marker,position)
            display_board(board)
            if win_check(board,player1_marker)==True:
                display_board(board)
                print("Player 1 has won the game!!")
                break
            else:
                if full_board_check(board)==True:
                    display_board(board)
                    print("The game is a draw!!")
                    break
                else:
                    chance = 2
        else:
            print("Player 2 it's your turn")
            position = player_choice(board)
            place_marker(board,player2_marker,position)
            display_board(board)
            if win_check(board,player2_marker)==True:
                display_board(board)
                print("Player 2 has won the game!!")
                break
            else:
                if full_board_check(board)==True:
                    display_board(board)
                    print("The game is a draw!!")
                    break
                else:
                    chance=1
    if replay():
        continue
    else:
        choice = False