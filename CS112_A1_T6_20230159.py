# Program:This is the second game (Tic-Tac-Toe with numbers):A board of 3 x 3 is displayed 
# and player 1 takes odd numbers 1,3, 5, 7, 9 and player 2 takes even numbers 0, 2, 4, 6, 8.
# Players take turns to write their numbers. Odd numbers start. Use each number only once.
# The first person to complete a line that adds up to 15 is the winner.

# Author:Zyad Mohamed Ahmed Abdelzaher (20230159) 
# Version:1.0
# Date:2/28/2024

def show_board(board): #Function to show the board
    print(board[0])
    print(board[1])
    print(board[2])

def win(board): #Function to check if someone won
        first_diagonal=[board[0][0],board[1][1],board[2][2]]
        second_diagonal=[board[0][2],board[1][1],board[2][0]]  
        if 'x' not in first_diagonal: #We make sure that the diagonal is a complete line of numbers
            if sum(first_diagonal)==15: #Checking if it sums up to 15
                return True
        if 'x' not in second_diagonal:
            if sum(second_diagonal)==15:
                return True   
            
        for row in board: #Iterates through every row in the board
            if 'x' not in row: #Make sure that the row is a complete line of numbers
                if sum(row)==15: #Checking if it sums up to 15
                    return True   
                           
        for i in range(3):
            column_sum = 0 #Variable to store the sum of every number in each column
            complete_column = 1 #Variable to check if we have a complete column
            for j in range(3): #Access every element in every column
                if board[j][i] == 'x':  #Make sure that the column is a complete line of numbers
                    complete_column = 0
                    break
                else:
                    column_sum += board[j][i] #We add the number to the sum
            if complete_column == 0: #If it wasn't a complete column we continue to the next iteration
                continue        
            if column_sum == 15 : #Checking if it sums up to 15
                return True 

player1_numbers=[1,3,5,7,9] #Player 1 numbers
player2_numbers=[0,2,4,6,8] #Player 2 numbers
board=[ ['x','x','x'] , ['x','x','x'] , ['x','x','x'] ] #Initial values of the board

while True:

    print("Player 1 turn:")
    print("Your numbers are: "+ str(player1_numbers)) #Show him his available numbers
    show_board(board) 
    number=input("Enter the number you want to play:\n")
    while not(number.isdigit()) or int(number) not in player1_numbers: #Make sure he chooses a valid number from his available numbers
        number=input("Please enter a valid number:\n")
    number=int(number)
    player1_numbers.remove(number) #We remove his choise from his available numbers

    row_index=input("Which row do you want to put this number?\n")
    while not(row_index.isdigit()) or int(row_index)<1 or int(row_index)>3: #Make sure he chooses a valid row from 1 to 3
        row_index=input("Enter a valid number:\n")
    row_index=int(row_index)

    column_index=input("Which column do you want to put this number?\n")
    while not(column_index.isdigit()) or int(column_index)<1 or int(column_index)>3: #Make sure he chooses a valid column from 1 to 3
        column_index=input("Enter a valid number:\n")
    column_index=int(column_index)  

    while board[row_index-1][column_index-1] != 'x' : #Check if he chooses a filled place
        print("This is a filled place")
        row_index=input("Which row do you want to put this number?\n") #Ask him again where to put his number
        while not(row_index.isdigit()) or int(row_index)<1 or int(row_index)>3:
            row_index=input("Enter a valid number:\n")
        row_index=int(row_index)
        column_index=input("Which column do you want to put this number?\n")
        while not(column_index.isdigit()) or int(column_index)<1 or int(column_index)>3:
            column_index=input("Enter a valid number:\n")
        column_index=int(column_index) 

    board[row_index-1][column_index-1] = number #Add the number to the place he chooses
    show_board(board)

    if win(board): #Check if he won and the game ends
        print("Player 1 is the winner!")
        break

    print("Player 2 turn:") #Everything is the same with player two
    print("Your numbers are: "+ str(player2_numbers))
    show_board(board)
    number=input("Enter the number you want to play:\n")
    while not(number.isdigit()) or int(number) not in player2_numbers:
        number = input("Please enter a valid number:\n")
    number = int(number)
    player2_numbers.remove(number)

    row_index = input("Which row do you want to put this number?\n")
    while not(row_index.isdigit()) or int(row_index) < 1 or int(row_index) > 3:
        row_index = input("Enter a valid number:\n")
    row_index = int(row_index)

    column_index = input("Which column do you want to put this number?\n")
    while not(column_index.isdigit()) or int(column_index) < 1 or int(column_index) > 3:
        column_index = input("Enter a valid number:\n")
    column_index = int(column_index)  

    while board[row_index-1][column_index-1] != 'x' :
        print("This is a filled place")
        row_index = input("Which row do you want to put this number?\n")
        while not(row_index.isdigit()) or int(row_index) < 1 or int(row_index) > 3:
            row_index = input("Enter a valid number:\n")
        row_index = int(row_index)

        column_index = input("Which column do you want to put this number?\n")
        while not(column_index.isdigit()) or int(column_index) < 1 or int(column_index) > 3:
            column_index = input("Enter a valid number:\n")
        column_index = int(column_index) 

    board[row_index-1][column_index-1] = number
    show_board(board)

    if win(board):
        print("Player 2 is the winner!")
        break

