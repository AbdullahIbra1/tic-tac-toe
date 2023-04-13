# tic-tac-toe
## A traditional tic tac toe game
## project for course CS492


the user choose who play first, the player or computer
if the user choose player to play first then he will choose a letter X or O, otherwise the computer will chose random letter and play the first move

## In case of player play first
```
if choice == "p1":
         if playerChoice == "X":
            cmpChoice = "O"
         else :
             cmpChoice="X"   
```

## In case of computer play first

```
if choice == "cmp":
         symb = ["X","O"]
         cmpChoice = random.choice(symb)  
         if cmpChoice == "X":
            playerChoice = "O"
         else :
            playerChoice = "X"
```

## In each iteration computer choose where to play randomly

```
compChoice = [0,1,2]
row = random.choice(compChoice)
column = random.choice(compChoice)
board[row][column] = cmpChoice
```

## To decide who wins we must iterate through each row and column and diagonals and check if they have the same symbol for both X and O
