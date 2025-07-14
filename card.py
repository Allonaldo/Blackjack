import random

ranks = [i for i in range(1,11)] + ['Jack', 'Queen', 'King']
suits = ['Clubs',
         'Diamonds',
         'Hearts',
         'Spades',
         ]

# Implement card class
class Card:
    """"
    Represents a playing card of given suit and rank.
    """
    def __init__(self, suit, rank):
        
        """
        Initializes a Card object

        Args:
            suit (str): The suit of the card.
            rank (int or str): Rank of the card (1-10, 'Jack', 'Queen', 'King').

        Raises:
            ValueError: If suit or rank is invalid.
        """
        
        if suit not in suits:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in ranks:
            raise ValueError(f"Invalid rank: {rank}")

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

    """"
    Represent a deck of 52 playing cards.
    """

    def __init__(self):

        """"
        Initialize Deck object (with 52 cards).
        """
        
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))    

    
    def shuffle(self):

        """"
        Shuffle the stack of cards.
        """        

        random.shuffle(self.cards)
    
    def __repr__(self):
        return "Deck()"

# Implement player hand
class Player:

    """
    Represents a blackjack player and their hand.
    """

    def __init__(self, name):
        
        """
        Initialize a Player object

        Args:
            name (str): the player's name
        """

        self.name = name # Player name
        self.hand = []
        self.bet = 0
        self.bank = 1000

    def place_bet(self):

        """
        Prompts a player to place a bet.
        Sets self.bet to the valid amount.
        """        

        print("Place a bet from $2 to $500")
        while True:
            try:
                bet = int(input("Place your bet: $"))
                if 1 < bet < 501:
                    self.bet = bet
                    self.bank -= bet
                    break
                else:
                    print("Bet must be between $2 and $500.")
            except ValueError:
                print("Please enter a valid number.")

    
    def choice(self, dealer, deck):
        
        """
        Asks the player whether to hit or stand.

        Args:
            dealer (Dealer): The dealer object.
            deck (Deck): The deck of cards currently in use.

        Returns:
            0 if the player stands.
        """

        print("Hit or stand?")
        while True:
            player_choice = input("Enter h or s: ").lower()

            if player_choice == 'h':
                dealer.deal(deck, self)
            elif player_choice == 's':
                return 0
    
    def hit(self, card):
        
        """
        Represents a hit in blackjack. 

        Args:
            card (Card): The card to add to the player's hand.
        """
        self.hand.append(card)
        
    def check_hand(self):
        
        """
        Calculate the value of the cards held according to blackjack rules.

        Returns:
            int: The value of the hand (0 if bust, 21 if natural)
        """        
        values = [card.value for card in self.hand]
        value = sum(values)
        has_ace = 1 in values
        
        # Check for naturals
        if len(values) == 2 and value == 21:
            return 21
        
        # Bust
        if value > 21:
            return 0
        
        # Handle ace
        if value > 11:
            return value
        elif has_ace:
            return value + 10
          
    def __repr__(self):
        return f"Player({self.name})"

    def __str__(self):

    # Can be improved later, with ascii representation. 
        return ', '.join(str(card) for card in self.hand)

class Dealer(Player):
    
    """
    Represent the dealer in blackjack.
    Inherits from the Player class.
    Takes no arguments, the name is automatically "Dealer".
    """    

    def __init__(self):
        super().__init__("Dealer")

    def deal(self, deck, player):
        """
        Deals a card from the deck to a player.

        Args:
            deck (Deck): The deck of cards.
            player (Player): The player receiving the card.
        """        

        card = deck.cards.pop()
        player.hit(card)

    @staticmethod
    def pay(player, multiplier=1):

        """
        Dealer pays the player

        Args:
            player (Player): The payee.
            multiplier (float): The multiplyer by default is 1. Should be changed to 1.5 in 
            certain cases.
        """


        player.bank += multiplier * player.bet

