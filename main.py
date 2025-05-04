from blackjack.account import Account
from blackjack.game import BlackjackGame

if __name__ == '__main__':
    myaccount = Account()
    myaccount.deposit(100)
    game=BlackjackGame(myaccount)
    game.start()
