import random

ranks = [i for i in range(1,11)] + ['Jack', 'Queen', 'King']
suits = ['Clubs',
         'Diamonds',
         'Hearts',
         'Spades',
         ]

# Implement card class
class Card:

    def __init__(self, suit, rank):

        self.suit = suit
        if type(rank) == str:
            self.rank = 10
        else:
            self.rank = rank

    def __str__(self):
        
        return "----> Suit: {}, Rank: {}".format(self.suit, self.rank)
    
    def __add__(self, other):

        return self.rank + other.rank


# Implement deck class
class Deck:

    def __init__(self):
        
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))    

    def deal(self):
        
        card_taken = self.cards.pop()

        return card_taken
    
    def shuffle(self):

        random.shuffle(self.cards)

# Implement player hand
class Hand:

    def __init__(self, name):

        self.name = name # Player name
        self.hand = []
        self.value = 0   
        self.has_ace = 0 
    
    def add_card(self, card):

        self.hand.append(card)
        
    def check_hand(self):

        pass


    
card1 = Card('Spades', 'Jack')
card2 = Card('Hearts', 1)

print(card1)
print(card1 + card2)

