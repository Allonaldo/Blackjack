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
    
    def __repr__(self):
        return f"Card({self.suit, self.rank})"
    
# Implement deck class
class Deck:

    def __init__(self):
        
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))    

    def deal(self):
        
        return self.cards.pop()
    
    def shuffle(self):

        random.shuffle(self.cards)
    
    def __repr__(self):
        return "Deck()"

# Implement player hand
class Player:

    def __init__(self, name):

        self.name = name # Player name
        self.hand = []
    
    def hit(self, card):

        self.hand.append(card)
        
    def check_hand(self):

        values = [card.value for card in self.hand]
        aces = values.count(1)
        value = sum(values)

        # Check for naturals
        if len(values) == 2 and value == 21:
            return 21
        
        # Bust (ace was counted as 1)
        if value > 21:
            return 0
        
        # Else, ask if ace should be 11 or 1?
        return value, aces
          
    def __repr__(self):
        return f"Player({self.name})"

    def __str__(self):

    # Can be improved later, with ascii representation. 
        return ', '.join(str(card) for card in self.hand)

    
deck1 = Deck()
deck1.shuffle()
print(deck1)

player1 = Player('Jan')
player1.add_card(deck1.deal())

