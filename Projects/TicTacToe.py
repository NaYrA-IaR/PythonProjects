from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print(board[1]+'  |'+board[2]+'  |'+board[3])
    print('---|---|---')
    print(board[4]+'  |'+board[5]+'  |'+board[6])
    print('---|---|---')
    print(board[7]+'  |'+board[8]+'  |'+board[9])
    

print("Welcome to TicTacToe")
print("Rules:\nThe board is like a numpad i.e.1 at the top left and 9 at bottom right\nThe first person to have the same marker at three consecutive spaces wins the game i.e. vertically , horizontally or diagonally\n The board is like------------->")

print('1'+'  |'+'2'+'  |'+'3')
print('---|---|---')
print('4'+'  |'+'5'+'  |'+'6')
print('---|---|---')
print('7'+'  |'+'8'+'  |'+'9')
choice = True
