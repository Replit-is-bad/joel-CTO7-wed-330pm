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

def get_player_move(argboard):

    while True:
        
        pMove = input('Enter a number from 1-9: ')

        if pMove.isdigit():
            pMove = int(pMove)
            if pMove >=1 and pMove <= 9:
                pMove = pMove -1
                row = pMove // 3
                col = pMove % 3
                print(f"row = {row}, col{col}")

                #check if cell is empty
                if argboard[row][col] == " ":
                    argboard[row][col] ='X' 
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
    

#Main game loop
board = initboard()
cplayer =''

while True:
    printboard(board)


    board = get_player_move(board)



