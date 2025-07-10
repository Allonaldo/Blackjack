from card import Deck, Player, Dealer


def play():

    deck = Deck()
    deck.shuffle()
    dealer = Dealer()
    players = [dealer]

    # Let players join
    print("Enter player names one by one.")
    while True:

        name = input("Enter player name: ")
        if not name:
            break
        players.append(Player(name))

    # Deal 2 cards to each player
    for player in players:
        dealer.deal(deck, player)
        dealer.deal(deck, player)

    # Blackjack Loop
    while True:
        pass
        
    
