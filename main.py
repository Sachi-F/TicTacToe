'''
Tic Tac Toe Game!!!
'''
from Board import Board
import random

print("Welcome to Tic Tac Toe game!")
print()

if __name__ == "__main__":

  # eri's code
  mode = 0
  while(mode not in [1, 2]):
    mode = int(input("How many players?: "))
  # end of eri's code
  
  Game = Board()
  Game.display()

  XorO = ["X", "O"]
  player = random.choice(XorO)
  # eri's code
  if mode == 1:
    Game.AI = player
  # end of eri's code
  round = 1
  
  # (think of some condition to keep playing):
  while Game.checkWinner() == False and round <= 9:
    
    # display some message about who's turn it is and what the board looks like
    print()
    if player == "X":
      print("X's turn!")
    elif player == "O":
      print("O's turn!")

    if Game.AI != player:
      # take input about what coordinate they want to place their next move
      # must be in the range of 0 - 2
      validInput = False
      while not validInput:
        row = int(input("Please enter row from 0-2: "))
        col = int(input("Please enter column from 0-2: "))
  
        if (row in range(3)) and (col in range(3)) and Game.cells[row][col] == "":
          validInput = True
  
        else:
          print("Your input was invalid")
    
      # register the input
      print()
  
      Game.setCell(row, col, player)

    # eri's code
    else:
      Game.AIMakeMove()
      #print(Game.checkWinner())
      
      
    Game.display()
    print()    
    
    # switch the player after their turn of over
    if player == "X":
      player = "O"
    elif player == "O":
      player = "X"

    round += 1

  if Game.checkWinner() == False and round > 9:
    print("This game was a tie")
  
  if Game.checkWinner() != False:
    Game.announceWinner()


