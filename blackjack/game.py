import time
from .account import Account
from .bet import Blackjack_bet
from .strategy import HumanPlayerStrategy, DealerPlayerStrategy
from .deck import Deck
from .participant import Player, Dealer
from .logger import GameLogger


class BlackjackGame:
    def __init__(self, account):
        self.account = account
        self.deck=Deck()
        self.logger=GameLogger()


    def play_round(self, bet_amount):
        self.deck.reset()
        bet=Blackjack_bet(bet_amount)

        player = Player()
        dealer = Dealer()

        for _ in range(2):
            player.hand.add_card(self.deck.deal_card())
            dealer.hand.add_card(self.deck.deal_card())

        print("*********** New Round ***********")
        print(f"Your hand is {player.hand}")
        print(f"Dealer's visible card is {dealer.hand.cards[0]}")

        if not player.play_turn(self.deck):
            print(f"You busted! Dealer wins, You lost {bet.get_bet_amount()}")
            self.logger.log(bet, "You lost!", player, dealer)
            return

        print("\nDealer's turn:")
        dealer.play_turn(self.deck)
        print(f"Dealer's hand is {dealer.hand}")

        player_total=player.hand.get_total()
        dealer_total=dealer.hand.get_total()

        if dealer_total>21 or player_total>dealer_total:
            result="You won!"
            bet_result=f"You won {bet.payout_win()}!"
            self.account.deposit(bet.payout_win())
        elif dealer_total>player_total:
            result = "You lost!"
            bet_result=f"You lost {bet.get_bet_amount()}!"
        else:
            result = "Draw!"
            bet_result=f"Returned {bet.get_bet_amount()}!"
            self.account.deposit(bet.payout_draw())

        print(result, bet_result)
        self.logger.log(bet, result, player, dealer)

    def start(self):
        while True:
            print(f'Your balance is: {self.account.get_balance()}')
            try:
                bet_amount = int(input("Enter bet amount: "))

            except ValueError:
                print("Bet must be a number")
                continue

            if bet_amount <= 0:
                print("Bet must be a positive number")
                continue

            if bet_amount > self.account.get_balance():
                print("You don't have enough money")
                continue

            self.account.withdraw(bet_amount)
            self.play_round(bet_amount)

            if self.account.get_balance() == 0:
                print("You don't have any money left to play with")
                time.sleep(10)
                break

            again=input("Do you want to play again?").lower()

            if again!='yes':
                print("Thank you for playing")
                break