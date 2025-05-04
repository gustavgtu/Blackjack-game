import unittest
from blackjack.strategy import DealerPlayerStrategy

class TestDealer(unittest.TestCase):
    def test_dealer_hits_under_17(self):
        strategy = DealerPlayerStrategy()
        self.assertEqual(strategy.decide_hit_or_stand(['10', '6'], 16), 'hit')
        self.assertEqual(strategy.decide_hit_or_stand(['10', '7'], 17), 'stand')
