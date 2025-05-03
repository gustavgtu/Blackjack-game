import random
from abc import ABC, abstractmethod

class Account:
    def __init__(self):
        self.__balance=0

    def deposit(self, amount):
        self.__balance+=amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance-=amount
        else:
            print("You don't have enough money")

    def get_balance(self):
        return self.__balance

class Blackjack_bet:
    def __init__(self, bet_amount):
        self.__bet_amount=bet_amount

    def payout_win(self):
        return self.__bet_amount*2

    def payout_draw(self):
        return self.__bet_amount

    def get_bet_amount(self):
        return self.__bet_amount

class PlayerStrategy(ABC):
    @abstractmethod
    def decide_hit_or_stand(self, hand, total):
        pass

class HumanPlayerStrategy(PlayerStrategy):
    def decide_hit_or_stand(self, hand, total):
        while True:
            choice = input("Hit or stand?").lower()
            if choice in ['hit', 'stand']:
                return choice
            else:
                print("Invalid input, type 'hit' or 'stand'")


class DealerPlayerStrategy(PlayerStrategy):
    def decide_hit_or_stand(self, hand, total):
        return 'hit' if total<17 else 'stand'

class Hand:
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10,
                   'King': 10, 'Ace': 11}

    def __init__(self):
        self.cards=[]

    def add_card(self, card):
        self.cards.append(card)

    def get_total(self):
        total=sum(self.card_values[card] for card in self.cards)
        ace_count=self.cards.count("Ace")
        while ace_count and total>21:
            total-=10
            ace_count-=1
        return total

    def __str__(self):
        return f"{self.cards}, (total: {self.get_total()})"

class Deck:
    def __init__(self):
        self.reset()

    def reset(self):
        self.cards=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] * 4
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards)<15:
            self.reset()
        return self.cards.pop()

class Participant(ABC):
    def __init__(self, strategy):
        self.hand=Hand()
        self.strategy=strategy

    def play_turn(self, deck):
        while True:
            total=self.hand.get_total()
            choice=self.strategy.decide_hit_or_stand(self.hand.cards, total)
            if choice=='hit':
                self.hand.add_card(deck.deal_card())
                print(f'Hand is {self.hand}')
                if self.hand.get_total() > 21:
                    print(f"{self.__class__.__name__} busts with {self.hand}!")
                    return False

            else:
                return True

class Player(Participant):
    def __init__(self):
        super().__init__(HumanPlayerStrategy())

class Dealer(Participant):
    def __init__(self):
        super().__init__(DealerPlayerStrategy())

class GameLogger:
    def __init__(self, filename="BlackjackHistory.txt"):
        self.filename = filename
        with open(self.filename, 'w') as f:
            f.write("=== Blackjack History ===\n")

    def log(self, bet, result, player, dealer):
        with open(self.filename, 'a') as f:
            f.write(f"\nResult: {result}\n")
            f.write(f"Bet: {bet.get_bet_amount()} | ")
            if result == "You won!":
                f.write(f"Won: {bet.payout_win()}\n")
            elif result == "Draw!":
                f.write(f"Returned: {bet.get_bet_amount()}\n")
            else:
                f.write(f"Lost: {bet.get_bet_amount()}\n")
            f.write(f"Player hand: {player.hand.cards} (Total: {player.hand.get_total()})\n")
            f.write(f"Dealer hand: {dealer.hand.cards} (Total: {dealer.hand.get_total()})\n")


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
            bet_result=f"You got back to {bet.get_bet_amount()}!"
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
                break

            again=input("Do you want to play again?").lower()

            if again!='yes':
                print("Thank you for playing")
                break


if __name__ == '__main__':
    myaccount = Account()
    myaccount.deposit(100)
    game=BlackjackGame(myaccount)
    game.start()



