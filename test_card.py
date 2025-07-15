import unittest
from game_objects import Card, Deck, Player, Dealer

class TestBlackjack(unittest.TestCase):
    def test_card_value(self):
        self.assertEqual(Card('Hearts', 1).value, 1)
        self.assertEqual(Card('Spades', 'King').value, 10)
        self.assertEqual(Card('Diamonds', 10).value, 10)

    def test_deck_init(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        suits = set(card.suit for card in deck.cards)
        self.assertEqual(suits, {'Clubs', 'Diamonds', 'Hearts', 'Spades'})

    def test_player_bet_and_bank(self):
        player = Player('Test')
        player.funds = 100
        player.bet = 10
        dealer = Dealer()
        dealer.funds = 1000
        dealer.pay(player)
        self.assertEqual(player.funds, 120)
        self.assertEqual(dealer.funds, 980)

    def test_dealer_deal(self):
        deck = Deck()
        dealer = Dealer()
        player = Player('Test')
        dealer.deal(deck, player)
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(len(deck.cards), 51)

    def test_check_hand_blackjack(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 10)]
        self.assertEqual(player.check_hand(), 21)

    def test_check_hand_bust(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 10), Card('Spades', 10), Card('Clubs', 5)]
        self.assertEqual(player.check_hand(), 0)

    def test_check_hand_ace(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 7)]
        self.assertEqual(player.check_hand(), 18)

if __name__ == '__main__':
    unittest.main()
