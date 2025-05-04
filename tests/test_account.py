import unittest
from blackjack.account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()

    def test_initial_balance_is_zero(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit_increases_balance(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_withdraw_decreases_balance(self):
        self.account.deposit(100)
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_more_than_balance(self):
        self.account.deposit(50)
        self.account.withdraw(100)  # Should not change the balance
        self.assertEqual(self.account.get_balance(), 50)

if __name__ == '__main__':
    unittest.main()
