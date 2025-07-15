from game_objects import Deck, Player, Dealer


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

    # Place bets
    print("Place a bet from $2 to $500")
    for player in players:
        player.place_bet()


    # Deal 2 cards to each player
    for player in players:
        dealer.deal(deck, player)
        dealer.deal(deck, player)
        print(player)

    print("DEALER")
    print(dealer)

    # Check for blackjack/naturals
    for player in players:
        score = player.check_hand()
        print(player)
        if score == 21:
            player.bet = 0
            dealer_up = dealer.hand[0]

            # Check if dealer's faceup card is Ace or 10
            if dealer_up == 1 or dealer_up == 10:
                if dealer.check_hand() == 21:
                    # Return wager
                    dealer.pay(player)
                else:
                    dealer.pay(player,1.5)


    # Player turns
    for player in players:
        while 0 < player.check_hand() < 21:
            # Player stands
            if player.choice(dealer, deck) == 0:
                break

    # Dealer's turn
    while 0 < dealer.check_hand() < 17:
        dealer.deal(deck, dealer)

    # Check results
    dealer_score = dealer.check_hand()
    for player in players:

        # Dealer bust
        if dealer_score == 0:
            dealer.pay(player)

        # Dealer wins
        elif dealer_score > player.check_hand():
            dealer.funds += player.bet

        # Player wins
        elif dealer_score < player.check_hand():
            dealer.pay(player)
        
        # Tie
        else:
            player.bank += player.bet

                
            


        

                


        
    
