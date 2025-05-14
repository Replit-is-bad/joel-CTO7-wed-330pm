import random

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

    
# Function to display the hand
# params : hand, typeofhand (banker_hide, player_show, banker_show)
def show_hand(hand,playtype):
    if playtype == "player_show":
        # show the player's hand
        print('@' * 15)
        print('PLAYER HAND')
        for card in hand:
            print(f'{card[1]} {card[0]}')
        print('@' * 15)

    elif playtype == 'banker_hide':
        print('$' * 15)
        print('BANKER HAND')
        print(f'{hand[0][1]} {hand[0][0]}')
        print('? ? ?' * 3)
        print('$' * 15)
    print()


show_hand(player_hand, 'player_show')
show_hand(banker_hand, 'banker_hide')
# print(banker_hand)
# print(player_hand)