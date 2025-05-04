import unittest
from blackjack.hand import Hand

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()

    def test_add_card_and_total(self):
        self.hand.add_card('5')
        self.hand.add_card('6')
        self.assertEqual(self.hand.get_total(), 11)

    def test_ace_handling(self):
        self.hand.add_card('Ace')
        self.hand.add_card('King')
        self.hand.add_card('5')
        self.assertEqual(self.hand.get_total(), 16)

    def test_multiple_aces(self):
        self.hand.add_card('Ace')
        self.hand.add_card('Ace')
        self.hand.add_card('9')
        self.assertEqual(self.hand.get_total(), 21)

    def test_bust(self):
        self.hand.add_card('10')
        self.hand.add_card('Queen')
        self.hand.add_card('2')
        self.assertGreater(self.hand.get_total(), 21)

if __name__ == '__main__':
    unittest.main()
