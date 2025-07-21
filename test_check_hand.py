import unittest
from game_objects import Card, Player

class TestCheckHand(unittest.TestCase):
    def test_blackjack(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 10)]
        self.assertEqual(player.value, 21)

    def test_bust(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 10), Card('Spades', 10), Card('Clubs', 5)]
        self.assertEqual(player.value, 0)

    def test_ace_high(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 7)]
        self.assertEqual(player.value, 18)

    def test_ace_low(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 10), Card('Clubs', 10)]
        self.assertEqual(player.value, 21)

    def test_no_ace(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 9), Card('Spades', 7)]
        self.assertEqual(player.value, 16)

    def test_empty_hand(self):
        player = Player('Test')
        player.hand = []
        self.assertEqual(player.value, 0)

    def test_multiple_aces(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 1), Card('Clubs', 9)]
        self.assertEqual(player.value, 21)

    def test_three_aces(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 1), Card('Clubs', 1)]
        self.assertEqual(player.value, 13)

    def test_face_cards(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 'King'), Card('Spades', 'Queen')]
        self.assertEqual(player.value, 20)

    def test_ace_and_face_card(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 'Queen')]
        self.assertEqual(player.value, 21)

    def test_bust_with_ace(self):
        player = Player('Test')
        player.hand = [Card('Hearts', 1), Card('Spades', 10), Card('Clubs', 10), Card('Diamonds', 2)]
        self.assertEqual(player.value, 0)

if __name__ == '__main__':
    unittest.main()
