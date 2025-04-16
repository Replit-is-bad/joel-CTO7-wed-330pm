import random


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

def printboard(argboard):
    #empty space
    count = 1
    #retriving the board row
    for row in argboard:
        for col in row:
            if col == " ":
                print(f'| {count}' , end=' ')
            else:
                print(f'| {col} ', end = '')

            if count % 3 == 0: # helps to calculate new row
                print('|')
                print('-'*13)
            count += 1

def get_player_move(argboard,cplayer):

    while True:
        
        pMove = input(f'Player {cplayer}, enter a number from 1-9: ')

        if pMove.isdigit():
            pMove = int(pMove)
            if pMove >=1 and pMove <= 9:
                pMove = pMove -1
                row = pMove // 3
                col = pMove % 3
                print(f"row = {row}, col{col}")

                #check if cell is empty
                if argboard[row][col] == " ":
                    argboard[row][col] = cplayer 
                    break
                else:
                    print(f'{pMove + 1 } is already eaten by : https://www.youtube.com/channel/UC63anZxfVGHUEmfBAf5w7pw')
            else:
                print('ERROR :.... .- ...- . / .- / -. .. -.-. . / -.. .- -.-- .-.-.- .-.-.- .-.-.- . .-.. ... . .-- .... . .-. . .-.-.-')
        else:
            print('ERROR : ...  -  ..-  .--.  ..  -..')
    return argboard

#find the player turn
def getcurrentplayer(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'
    

#winner function
def checkwin(argboard):
    win = [
    [argboard[0][0],argboard[0][1], argboard[0][2]],# row 1
    [argboard[1][0],argboard[1][1], argboard[1][2]],# row 2
    [argboard[2][0],argboard[2][1], argboard[2][2]],# row 3

    [argboard[0][0],argboard[1][0], argboard[2][0]],# col 1
    [argboard[0][1],argboard[1][1], argboard[2][1]],# col 2
    [argboard[0][2],argboard[1][2], argboard[2][2]],# col 3

    [argboard[0][0],argboard[1][1], argboard[2][2]],# digonal 1
    [argboard[0][2],argboard[1][1], argboard[2][0]]# digonal 2
    ]


    for condition in win:
        if condition[0] == condition[1] == condition[2] and condition[0] !=' ':
            return True
    return False

def checktie(argboard):
    for row in argboard:
        for cell in row:
            if cell ==' ':
                return False
    return True


# 1. Check if AI can win in the next move == take that move.
# 2. Check if player can win in next move == block it.
# 3. If center is empty == take center.
# 4. If a corner is empty == take a corner.
# 5. Else == take any available space.

#Main game loop
board = initboard()
cplayer =''

while True:
    printboard(board)

    cplayer = getcurrentplayer(cplayer)

    #check if player or bot
    if cplayer == "X":
        board = get_player_move(board, cplayer)
    else:
        board = get_bot_move(board,cplayer)
    if checkwin(board):
        print(f'Player {cplayer} wins!!')
        printboard(board)
        break
    elif checktie(board):
        print('its a tie????')
        printboard(board)
        break