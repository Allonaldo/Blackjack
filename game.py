from card import Deck, Player, Dealer


def play():

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
    # players.append[dealer]

    # Deal 2 cards to each player
    for player in players:
        dealer.deal(deck, player)
        dealer.deal(deck, player)

    # Blackjack Loop

    for player in players:

        score = player.check_hand()
        if score == 21:
            dealer_first_card = dealer.hand[0]
            if dealer_first_card == 1 or dealer_first_card == 10:
                if dealer.check_hand() == 21:
                    dealer_natural = True
                    # Return bet to player

                else:
                    dealer_natural = False

        # Serve the players
        while 0 < score < 21:
            if player.choice() == 0:
                break

        # Dealer's play
        dealer_score = dealer.check_hand()
        while 0 < dealer_score < 17:
            dealer.hit() 
                
            


        

                


        
    
