def printGame(game):
    print(game[6] + '|' + game[7] + '|' + game[8])
    print('-+-+-')
    print(game[3] + '|' + game[4] + '|' + game[5])
    print('-+-+-')
    print(game[0] + '|' + game[1] + '|' + game[2])

def gameOver():
    again = input("Play again? [Y/N]: ")
    if (again == "Y"):
        main()
    else:
        print("See you next time!")
    

def main():

    board = [str(i) for i in range (9)]
    player = 1
    count = 0
    running = True

    while running:
        
        pos = int(input("Player " + str(player) + " turn. Input position: "))
        
        if (board[pos] == 'X' or board[pos] == 'O'):
            print("Invalid input. Try again.")
            continue

        if (player == 1):
            board[pos] = 'X'
            
        elif (player == 2):
            board[pos] = 'O'

        count += 1

        printGame(board)


        if (count >= 5):

            if (board[6] == board[7] == board[8] or
                board[3] == board[4] == board[5] or
                board[0] == board[1] == board[2] or
                board[6] == board[3] == board[0] or
                board[7] == board[4] == board[1] or
                board[8] == board[5] == board[2] or
                board[6] == board[4] == board[2] or
                board[8] == board[4] == board[0]):

                print(board[6] == board[7] == board[8] )
                
                print("\nGame Over.\n")                
                print(" **** Player " + str(player) + " won. ****")
                running = False
                gameOver()

        if (count == 9):
            print("\nGame Over.\n")
            print(" **** TIE GAME ****")
            running = False
            gameOver()
            
        if (player == 1):
            player = 2

        else:
            player = 1


main()

            
                

    
           
        
        
