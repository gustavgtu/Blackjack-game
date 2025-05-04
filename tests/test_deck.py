import unittest
from blackjack.deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_has_52_cards_initially(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_card_reduces_deck_size(self):
        self.deck.deal_card()
        self.assertEqual(len(self.deck.cards), 51)

    def test_deck_resets_when_low(self):
        for _ in range(39):
            self.deck.deal_card()
        self.assertGreaterEqual(len(self.deck.cards), 15)


if __name__ == '__main__':
    unittest.main()
