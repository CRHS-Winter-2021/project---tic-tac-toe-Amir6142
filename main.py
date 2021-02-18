##Tic Tac Toe
#Name:
#Date:

#1. (Var) Setup the empty board as a list
theBoard = [' ']*10






#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def printBoard(board):
  print(board[7] + ' |' + board[8] + '|' + board [9])
  print(' -+-+-')
  print(board[4] + ' |' + board[5] + '|' + board [6])
  print(' -+-+-')
  print(board[1] + ' |' + board[2] + '|' + board[3])
   





#3a. (fun) Determine if player is X or O
player1 = ''
player2 = ''

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter():
  global player1
  global player2
  letter = input('Enter X or O for player 1')
  if letter == 'X' :
     player1= 'X'
     player2= 'O'
  else  :
     player1= 'O'
     player2= 'X'



#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
   turn = int(input("Player" + player + ", make a move between 1-9 "))
   while board[turn] != ' ':
     printBoard(theBoard)
     turn = input('That spot is taken, choose a different one')
   board[turn] = player
   printBoard(theBoard)

  


#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
    
def checkWin(board, player):
    if board[1] == player and board[2] == player and board[3] == player:
      return True
    elif board[4] == player and board[5] == player and board[6] == player:
      return True
    elif board[7] == player and board[8] == player and board[3] == player:
      return True
    elif board[1] == player and board[4] == player and board[7] == player:
      return True
    elif board[2] == player and board[5] == player and board[8] == player:
      return True
    elif board[3] == player and board[6] == player and board[9] == player:
      return True
    elif board[7] == player and board[5] == player and board[3] == player:
      return True
    elif board[1] == player and board[5] == player and board[9] == player:
      return True
    else : return False
       

#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
  if board.count(' ') == 1:
    return True
  else:
    return False

#7. Main function

def main():
  print('Welcome to 1v1 Tic Tac Toe. ')
  chooseLetter()

  while checkFull(theBoard) != True:
    playerMove(theBoard, player1)
    if checkWin(theBoard, player1) == True:
      print('Congratulations on winning, Player 1')
      break
    if checkFull(theBoard) != False:
      print("It is a draw")
      break
    playerMove(theBoard, player2)
    if checkWin(theBoard, player2) == True:
      print('Congratulations on winning, Player 1')
      break
    if checkFull(theBoard) != False:
      print("It is a draw")
      break
main()
    #print Welcome
    #print instructions

    #game play
    #get player letter choice
    
    #while board is not full
    ###first player move
        #player chooses move
        #print board
        #check win
        #check board full

    ###second player move
        #player chooses move
        #print baord
        #check win
  
    
   
