# Feb 6
- debug the code, why does the game stop when the AI wins?
- make Github account

# Jan 31
- complete the setcell in `board.py`
- understand the edits in `main.py`
- try the game yourself and debug the code
- <ins>Let Eri know what you want to do!</ins>
  - [**project/questions**] more academic programming (more prep for the course!)
  - [**project base**] website development (making resources)
  - [**project base**] web scraping (gathering resources)
  - [**project base**] data science (organizing resources)


# Jan 30
- FINISH `AIMakeMove`

# Jan 16
- be able to explain the difference between an assignment (=) and boolean (==)
- complete the update of `checkWinner`
- update the announceWinner so that it uses self.Winner instead of row col inputs
- be able to terminate the game after all cells are filled

# Dec 19

- make the first player random
- check the winner after each round
- annouce the winner at the end
- prevent overriding the cells
  -  check if the given row and col are already assigned
- decorate the game

# Dec 11

- finish the `while loop`
- clean up the `diplay()` method
    - make sure the cols are aligned

# Dec 5

- finish the checkWinner()` method
- clean up the `diplay()` method
    - make sure the cols are aligned
- add `setCells()` until X wins the game under line 27

# Nov 28 

- make a class called Board
-  def __init__(self)
   -  contains 3x3 lists to store the state of the tic tac toe game
   -  e.g. `cells = [["", "", ""], ["", "", ""], ["", "", ""]]`
-  def display(self)
    -  make a display method to print the state of the cells
    -  e.g. `cells = [["X", "", ""], ["", "O", ""], ["", "", "X"]]`

```python
Game.display()
 X |   |  
   | O |  
   |   | X 
```
- def setCell(row, col, val)
    - this will update the value of the cell at the given row, col to the val [^1]
    ```python
    e.g. 
    cells = [["X", "", ""], ["", "O", ""], ["", "", "X"]]
    setCell(0, 2, "X")
    cells = [["X", "", "X"], ["", "O", ""], ["", "", "X"]]
    setCell(1, 0, "O")
    cells = [["X", "", "X"], ["O", "O", ""], ["", "", "X"]]
    ```

[^1]: list coordinate references
    ```
        0    1    2
    0[ ["X", "", "X"], 
    1  ["O", "O", ""], 
    2  ["", "", "X"]]
    ```