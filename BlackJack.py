import random

suits = ["♣ CLUB", "♦ DIAMOND","❤ HEART","♠ SPADE"]
ranks = ['2','3','4','5','6','7','8','9','JACK','QUEEN','KING','ACE']

# deck of cards
deck = []

for suit in suits:
    for rank in ranks:
        deck.append([suit,rank])

# shuffle the deck
for i in range(10):
    random.shuffle(deck)

print(deck)
# Draw a card
card1 = deck.pop()

print(card1)