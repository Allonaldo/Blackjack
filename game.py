from card import Deck, Player, Dealer


def play():

    # Setup game
    deck = Deck()
    deck.shuffle()
    dealer = Dealer()
    players = []

    # Let players join
    print("Enter player names one by one.")
    while True:

        name = input("Enter player name: ")
        if not name:
            break
        players.append(Player(name))

    # Deal 2 cards to each player
    for _ in range(2):
        for player in players:
            dealer.deal(player)

    # TODO: Handle naturals before the play


    # Blackjack loop
    for player in players:
        
        score = player.check_hand()
        while 0 < score < 21:
            # Ask to hit or stand
            if player.choice():
                dealer.deal(player)
            else: 
                break

    dealer_score = dealer.check_hand()
    while dealer_score < 17:
        dealer.deal(dealer)

    


        
    
        

        
    
