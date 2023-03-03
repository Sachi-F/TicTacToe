import math

class Board:
  def __init__(self):
    self.cells = [["", "", ""], ["", "", ""], ["", "", ""]]
    self.winner = ""
    self.AI = ""
    
  def display1 (self):
    print(self.cells[0], self.cells[1], self.cells[2])
    
  def setCell (self, row, col, val):
    self.cells[row][col] = val
    
  def display (self):
    for i in range(3):    # for each row
      for j in range(3):  # for each col
        
        print(" ", end="")
        if self.cells[i][j] != "":
          print(self.cells[i][j], end="")
        else:
          print(" ", end="")
        print(" ", end="")
        
        # end of the cell line
        if j != 2:
          print("|", end="")
        else:
          print("")


  def checkWinner(self):
    # top row
    if self.cells[0][0] != "" and self.cells[0][0] == self.cells[0][1] == self.cells[0][2]:
      if self.cells[0][0] == "X":
        self.winner = "X"
      else:
        self.winner = "O"

    # middle row
    elif self.cells[1][0] != "" and self.cells[1][0] == self.cells[1][1] == self.cells[1][2]:
      if self.cells[1][0] == "X":
        self.winner = "X"
      else:
        self.winner = "O"

    # bottom row
    elif self.cells[2][0] != "" and self.cells[2][0] == self.cells[2][1] == self.cells[2][2]:
      if self.cells[2][0] == "X":
        self.winner = "X"
      else:
        self.winner = "O"

    # left col
    elif self.cells[0][0] != "" and self.cells[0][0] == self.cells[1][0] == self.cells[2][0]:
      if self.cells[0][0] == "X":
        self.winner = "X"
      else:
        self.winner = "O"

    # middle col
    elif self.cells[0][1] != "" and self.cells[0][1] == self.cells[1][1] == self.cells[2][1]:
      if self.cells[0][1] == "X":
        self.winner = "X"
      else:
        self.winner = "O"

    # right col
    elif self.cells[0][2] != "" and self.cells[0][2] == self.cells[1][2] == self.cells[2][2]:
      if self.cells[0][2] == "X":
        self.winner = "X"
      else:
        self.winner = "O"

    # -ve tan x
    elif self.cells[0][0] != "" and self.cells[0][0] == self.cells[1][1] == self.cells[2][2]:
      if self.cells[0][0] == "X":
        self.winner = "X"
      else:
        self.winner = "O"

    # +ve tan 
    elif self.cells[0][2] != "" and self.cells[0][2] == self.cells[1][1] == self.cells[2][0]:
      if self.cells[0][2] == "X":
        self.winner = "X"
      else:
        self.winner = "O"

    else:
      return False

  # def announceWinner(self): 
  def announceWinner(self):
    print (self.winner + " wins!")


  # return the index (row, col) that yields the largest point
  def AIMakeMove(self):
    
    # calculate the best move
    # find the move with the highest <points> -> 
    '''
              1 2  1
              1 X  1
              1 X  1
              1 2  1
              -> representation of the points
    '''
      # calculate the possible points at each cell and 
      # chose the move with the highest attainable points
  
      # 1. for loop to address each index of the cell //for i in range(row): ... cell[i][j]
      # 2. calculate the point at the index
          # compare the current point with the max point seen so far
          #     a. currentPoint > maxPoint -> update the maxPoint AND its corresponding indeces
          #     b.currentPoint < maxPoint -> 何もしない
      # AFTER the for loop... WE KNOW THE BEST MOVE! -> maxPointが大きいところ!

    maxPoint = -math.inf
    maxPointRow = 0
    maxPointCol = 0

    for i in range(3): 
      for j in range(3):
        # dx と dy を±1でローテーションさせる
        for dx in range(-1, 2):
          for dy in range(-1, 2):
            checkX, checkY = i + dx, j + dy
            currentPoint = 0
            while 0<=checkX<3 and 0<=checkY<3 and self.cells[i][j] == "" and self.cells[checkX][checkY] == self.AI:
              currentPoint += 1
              checkX, checkY = i+(2*dx), j+(2*dy)
              break
              
            if currentPoint > maxPoint:
              maxPoint = currentPoint
              maxPointRow = i
              maxPointCol = j


    self.cells[maxPointRow][maxPointCol] = self.AI
    print("AI made the move")


