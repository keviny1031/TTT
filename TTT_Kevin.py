from copy import *

score1 = 0
score2 = 0

def printGame(g):
    game = copy(g)
    for i in range(9):
        if (game[i].isnumeric()):
            game[i] = " "
            
    print((game[0] + ' | ' + game[1] + ' | ' + game[2]).center(75))
    print('---+---+---'.center(75))
    print((game[3] + ' | ' + game[4] + ' | ' + game[5]).center(75))
    print('---+---+---'.center(75))
    print((game[6] + ' | ' + game[7] + ' | ' + game[8] + "\n").center(75))
    
def gameOver():
    again = input(("Play again? [Y/N]: \n".center(75)))

    while (not (again.upper() == "Y" or again.upper() == "N")):
        print("Invalid input. Please input either Y or N]\n".center(75))
        again = input(("Play again? [Y/N]: \n".center(75)))
        
    if (again.upper() == "Y"):
        print("\n" * 3)
        main()
        
    elif (again.upper() == "N"):
        print("\n")
        print("*** Final Scores ***".center(75))
        print(("Player 1: " + str(score1) + "   Player 2: " + str(score2)).center(75))
        print("\n" * 3)
        
        if (score1 > score2):
            print("*** PLAYER 1 WINS! ***".center(75))
            print("\n")
        elif (score2 > score1):
            print("*** PLAYER 2 WINS! ***".center(75))
            print("\n")
        else:
            print("*** TIE GAME! ***".center(75))
            print("\n")
            
        print("See you next time!".center(75))
        print("\n")
        input('Press Enter to exit'.center(75))
        

def instructions():
    print(" *** Welcome to the Instructions! *** \n".center(75))
    print("This version of Tic Tac Toe uses numbers".center(75))
    print("to represent each space on the board\n".center(75))
    game = [str(i+1) for i in range (9)]
    printGame(game)
    print("When prompted at your turn, simply input".center(75))
    print("the corresponding number to draw your mark".center(75))
    print("on a space".center(75))
    game[4] = 'X'
    print("\n")
    print("For example, to play 'X' in the middle on the".center(75))
    print("first turn, enter '5' at the prompt, as so:\n".center(75))
    print("Player 1 turn. Input position: 5\n".center(75))
    printGame(game)
    print("Simple as that! First to get 3 in a row wins!\n".center(75))
    print("[Type 1 to play or 2 to return to menu]\n".center(75))
    choice = input("Input [1 / 2]: \n".center(75))

    while (not choice.isnumeric()):
        print("[Invalid input. Please input either 1 or 2]\n".center(75))
        choice = input("Input [1 / 2]: \n".center(75))

    choice = int(choice)
    
    while (choice != 1 and choice != 2):
        print("Invalid input. Please input either 1 or 2]\n".center(75))
        choice = int(input("Input [1 / 2]: \n".center(75)))
        
    if (choice == 1):
        print("\n" + "~" * 75 + "\n")
        main()
        
    elif (choice == 2):
        print("\n" + "~" * 75 + "\n")
        welcome()


def welcome():
    print(" *** Welcome to Tic Tac Toe! *** ".center(75))
    print("Made by Kevin Yuan\n".center(75))
    print("[Type 1 to play or 2 to view the instructions.]\n".center(75))
    choice = input("Input [1 / 2]: \n".center(75))

    while (not choice.isnumeric()):
        print("[Invalid input. Please input either 1 or 2]\n".center(75))
        choice = input("Input [1 / 2]: \n".center(75))

    choice = int(choice)

    while (choice != 1 and choice != 2):
        print("Invalid input. Please input either 1 or 2\n".center(75))
        choice = int(input("Input [1 / 2]: \n".center(75)))
        
    if (choice == 1):
        print("\n" + "~" * 75 + "\n")
        main()
    
    elif (choice == 2):
        print("\n" + "~" * 75 + "\n")
        instructions()
    



def main():
    global score1
    global score2
    
    board = [str(i) for i in range (9)]
    player = 1
    count = 0
    print(("Player 1: " + str(score1) + "   Player 2: " + str(score2) + "\n").center(75))

    printGame(board)
    
    while True:
            
        pos = input(("Player " + str(player) + " turn. Input position: \n").center(75))

        if (not pos.isnumeric()):
            print(("Invalid input. Try again.\n").center(75))
            continue

        pos = int(pos)
        
        if ((not (pos >= 1 and pos <= 9)) or board[pos - 1] == 'X' or board[pos - 1] == 'O' ):
            print(("Invalid input. Try again.\n").center(75))
            continue

        if (player == 1):
            board[pos - 1] = 'X'
            
        elif (player == 2):
            board[pos - 1] = 'O'

        printGame(board)
        count += 1
        
        if (count >= 5):
            if (board[6] == board[7] == board[8] or
                board[3] == board[4] == board[5] or
                board[0] == board[1] == board[2] or
                board[6] == board[3] == board[0] or
                board[7] == board[4] == board[1] or
                board[8] == board[5] == board[2] or
                board[6] == board[4] == board[2] or
                board[8] == board[4] == board[0]):
                
                print("\n")
                print("Game Over.\n".center(75))             
                print((" **** Player " + str(player) + " won. ****").center(75))
                
                if (player == 1):
                    score1 += 1

                else:
                    score2 += 1
                    
                gameOver()
                break
                

        if (count == 9):
            print("\n")
            print("Game Over.\n".center(75))
            print(" **** TIE GAME ****".center(75))
            gameOver()
            break


        if (player == 1):
            player = 2

        else:
            player = 1



welcome()
           
        
        
