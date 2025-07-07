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
        self.rank = rank

        if self.rank in ['Jack', 'Queen', 'King']:
            self.value = 10
        else:
            self.value = self.rank

    def __str__(self):
        
        return "----> Suit: {}, Rank: {}, Value: {}".format(self.suit, self.rank, self.value)
    
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

    def __str__(self):

        # Can be improved later, with ascii representation. 
        return ', '.join(str(card) for card in self.cards)

# Implement player hand
class Player:

    def __init__(self, name):

        self.name = name # Player name
        self.hand = []
        self.value = 0   
        self.has_ace = 0 
    
    def add_card(self, card):

        self.hand.append(card)
        
    def check_hand(self, hand):

        self.value = 0
        # Iterate over hand
        # Count value of cards
        # Return hand value
        for card in self.hand:
            if card.value == 1:
                self.has_ace += 1
                self.value += 1
            else:
                self.value += card.value
                
        return self.value

    
deck1 = Deck()
deck1.shuffle()
print(deck1)

player1 = Player('Jan')
player1.add_card(deck1.deal())

