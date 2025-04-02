# import random


# def diceGuess(par1):
#     rNum1 = random.randint(1,6)
#     if rNum1 == par1:
#         return True
#     else:
#         return False
        
# print(diceGuess(4))

def initboard():
    board = []

    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)

    return board

def printboard(board):
    #empty space
    count = 1
    #retriving the board row
    for row in board:
        for col in row:
            print(f'| {count} ', end = '')

            if count % 3 == 0: # helps to calculate new row
                print('|')
                print('-'*13)
            count += 1

board = initboard()
printboard(board)


pMove = input('Enter a number from 1-9: ')


if pMove.isdigit():
    pass
else:
    print('ERROR : ...  -  ..-  .--.  ..  -..')
    