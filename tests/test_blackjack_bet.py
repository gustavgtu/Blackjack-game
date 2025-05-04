import unittest
from blackjack.bet import Blackjack_bet

class TestBlackjack(unittest.TestCase):
    def test_payout_win(self):
        bet = Blackjack_bet(50)
        self.assertEqual(bet.payout_win(), 100)

    def test_payout_draw(self):
        bet = Blackjack_bet(30)
        self.assertEqual(bet.payout_draw(), 30)
