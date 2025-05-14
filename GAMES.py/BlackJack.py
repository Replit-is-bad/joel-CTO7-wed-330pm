import random
import time

suits = ["♣ CLUB", "♦ DIAMOND","❤ HEART","♠ SPADE"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']

# Step 1: Create the deck of cards
# Create a dictionary to store the value of each card rank
# Cards 2–10 are worth their face value, J, Q, K are worth 10, 
# and Ace can be 1 or 11
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
'JACK':10, 'QUEEN':10,'KING':10, 'ACE':11}

# Deck of cards
deck = []

# Player hand
player_hand = []

# The bankers hand
banker_hand = []

# to build the deck
for suit in suits:
    for rank in ranks:
        deck.append([suit,rank])

# shuffle the deck
for i in range(10):
    random.shuffle(deck)

# Draw two cards into the player and the bankers hand
player_hand = [deck.pop(),deck.pop()]
banker_hand = [deck.pop(), deck.pop()]

def calculate(hand):
    points = 0
    count_aces = 0

    # loop through cards in hand
    for card in hand:
        cardpoint = values[card[1]]
        points += cardpoint
        

        if card[1] == 'ACE':
            count_aces += 1

    while points > 21 and count_aces > 0:
        points -= 10
        count_aces -= 1 

    return points



# Function to display the hand
# params : hand, typeofhand (banker_hide, player_show, banker_show)
def show_hand(hand,playtype):
    if playtype == "player_show":
        # show the player's hand
        print('@' * 20)
        print('     PLAYER HAND')
        for card in hand:
            print(f' {card[1]} {card[0]}')

        print(f' YOU HAVE {calculate(hand)} POINTS.')
        print('@' * 20)

    elif playtype == 'banker_hide':
        print('$' * 20)
        print('     BANKER HAND')
        print(f' {hand[0][1]} {hand[0][0]}')
        print('? ? ?' * 4)
        print('$' * 20)
    print()

# main game loop
while True:
    show_hand(banker_hand, 'banker_hide')
    show_hand(player_hand, 'player_show')

    # check if player win
    if calculate(player_hand) == 21:
        print('YOU WIN ! BLACK JACK !')
        break
    else:
        action = input(" 1 - hit , 2 - check : ")
        if action == "1":
            player_hand.append(deck.pop())


        # check if player bust or win
        if calculate(player_hand) > 21:
            print('YOU BUSTED 21 !')
            print('YOU LOST !')
            break
        elif action == "2":

            while calculate(banker_hand) <= 17:
                print('$$$ BANKER IS THINKING $$$$')
                time.sleep(1)
                banker_hand.append(deck.pop)