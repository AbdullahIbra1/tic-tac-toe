import random
import time

def main():
    print("\n\t\tHello! Welcome to Tic Tac Toe game!")
    print("\n\n\n")
    print("Player1 and computer, first choose who play first and what letter [p1 or cmp].")
    print("\n")
    choice = input("\t\tinput [p1 or cmp] -> ")

    symb = ["X","O"]
    
    # if player 1 is playing first: 
    if choice == "p1":
         playerChoice = input("\n\n\t\tPlayer 1, do you want to be [X] or [O] ? -> ")  #choose x or o
         if playerChoice == "X":
            cmpChoice = "O"
            print("\n\n\t\tplayer1 is [X]")
            print("\t\tComputer is [O].\n\n")
         else :
             cmpChoice="X"
             print("\n\n\t\tplayer1 is [O]")
             print("\t\tComputer is [X].\n\n")

    # if computer playing first:
    elif choice =="cmp":
        symb = ["X","O"]
        cmpChoice = random.choice(symb)     # randomly choose x or o
        if cmpChoice == "X":
            playerChoice = "O"
            print("\n\n\t\tComputer is [X].")
            print("\t\tplayer1 is [O].\n\n")
           
        else :
            playerChoice = "X"
            print("\n\n\t\tComputer is [O].")
            print("\t\tplayer1 is [X]\n\n")      
    else :
        print("\t\tWrong input")
        return 
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]   
    rows = len(board)
    cols = len(board)
    printTable(board)


    compChoice = [0,1,2]    

    for i in range(10):

        if i==9 and isWinner(board, playerChoice, cmpChoice) == False:
            print("***\t\t\t Draw! ***")                            #full? break
            break
        elif choice == "p1":                        #player turn
            print("\t\tPlayer1 it is your turn ")
            row = int(input("\n\t\tPick a row [upper row: enter 0], [middle row: enter 1], [bottom row: enter 2] -> "))
            column = int(input("\n\t\tPick a column: [left column: enter 0], [middle column: enter 1], [right column enter 2] -> "))
            while (board[row][column] == symb[0])or (board[row][column] == symb[1]):
                print("\n\t\t [The square you picked is already filled. Pick another one].")
                row = int(input("\n\t\tPick a row [upper row: enter 0], [middle row: enter 1], [bottom row: enter 2] -> "))
                column = int(input("\n\t\tPick a column: [left column: enter 0], [middle column: enter 1], [right column enter 2] -> "))
            
            board[row][column] = playerChoice
            printTable(board)
            if isWinner(board, playerChoice, cmpChoice) == True:  #win? break
                break
            choice = "cmp"                                         #availability? continue
            continue
        elif choice =="cmp":                        #computer turn
            print("\n\t\t[Computer turn]... ")
            time.sleep(2)
            row = random.choice(compChoice)
            column = random.choice(compChoice)
            while (board[row][column] == symb[0])or (board[row][column] == symb[1]):
                 row = random.choice(compChoice)
                 column = random.choice(compChoice)

            board[row][column] = cmpChoice
            printTable(board)
            if isWinner(board, playerChoice, cmpChoice) == True:  #win? break
                break
            choice = "p1"                                          #availability? continue
            continue

def printTable(board):
    print("\n\n\t\t(current table) : \n\n")
    print("\t\t _______________________")
    print("\t\t|\t|\t|\t|")
    print("\t\t|  ",board[0][0],"\t|  ",board[0][1],"\t|  ",board[0][2],"\t|")
    print("\t\t|_______|_______|_______|")
    print("\t\t|\t|\t|\t|")
    print("\t\t|  ",board[1][0],"\t|  ",board[1][1],"\t|  ",board[1][2],"\t|")
    print("\t\t|_______|_______|_______|")
    print("\t\t|\t|\t|\t|")
    print("\t\t|  ",board[2][0],"\t|  ",board[2][1],"\t|  ",board[2][2],"\t|")
    print("\t\t|_______|_______|_______|\n\n\n")

def isWinner(board, X_symb, Y_symb):
    win = False
    # check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == X_symb):
            win = True
            print("\t\t\t *** Player won! *** ")
            return win
        elif (board[row][0] == board[row][1] == board[row][2] == Y_symb):
            win = True
            print("\t\t\t *** Computer won! *** ")
            return win               
    # check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == X_symb):
            win = True
            print("\t\t\t *** Player1 won! *** ")
            return win
        elif (board[0][col] == board[1][col] == board[2][col] == Y_symb):
            win = True
            print("\t\t\t *** Computer won! *** ")
            return win
    # check the diagnoals
    if board[0][0] == board[1][1] == board[2][2] == X_symb:
        win = True 
        print("\t\t\t *** Player1 won! *** ")
        return win
    elif board[0][0] == board[1][1] == board[2][2] == Y_symb:
        win = True
        print("\t\t\t *** Computer won! *** ")
        return win
    elif board[0][2] == board[1][1] == board[2][0] == X_symb:
        win = True
        print("\t\t\t *** Player1 won! *** ")
        return win
    elif board[0][2] == board[1][1] == board[2][0] == Y_symb:
        win = True
        print("\t\t\t *** Computer won! *** ")
        return win
    return win
main()