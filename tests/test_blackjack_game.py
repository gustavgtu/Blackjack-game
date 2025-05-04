import unittest
from blackjack.game import BlackjackGame
from blackjack.account import Account

class TestBlackjackGame(unittest.TestCase):
    def test_initial_account_balance(self):
        acc = Account()
        acc.deposit(100)
        game = BlackjackGame(acc)
        self.assertEqual(game.account.get_balance(), 100)

if __name__ == '__main__':
    unittest.main()
