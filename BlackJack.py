import random

suits = ["♣ CLUB", "♦ DIAMOND","❤ HEART","♠ SPADE"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']

# Step 1: Create the deck of cards
# Create a dictionary to store the value of each card rank
# Cards 2–10 are worth their face value, J, Q, K are worth 10, 
# and Ace can be 1 or 11
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
'JACK':10, 'QUEEN':10,'KING':10, 'ACE':11}

# deck of cards
deck = []

#Player hand
player_hand = []

#the bankers hand
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
banker_hand = []

print(player_hand)