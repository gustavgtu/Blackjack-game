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

class PlayerStrategy(ABC):
    @abstractmethod
    def decide_hit_or_stand(self, hand, total):
        pass

class Human_Player_Strategy(PlayerStrategy):
    def decide_hit_or_stand(self, hand, total):
        while True:
            choice = input("Hit or stand?").lower()
            if choice in ['hit', 'stand']:
                return choice
            else:
                print("Invalid input, type 'hit' or 'stand'")


class Dealer_Player_Strategy(PlayerStrategy):
    def decide_hit_or_stand(self, hand, total):
        return 'hit' if total<17 else 'stand'



class BlackjackGame:
    def __init__(self, account):
        self.account = account
        self.card_values={'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.deck=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] * 4
        random.shuffle(self.deck)

        self.history_filename="BlackjackHistory.txt"
        with open (self.history_filename, 'w') as f:
            f.write("===Blackjack History===\n")

    def deck_check(self):
        if len(self.deck) < 15:
            self.deck=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] * 4
            random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def calculate_total(self, hand):
        total=sum(self.card_values[card] for card in hand)
        ace_count = hand.count('Ace')
        while ace_count and total>21:
            total-=10
            ace_count -= 1
        return total

    def play_turn(self, hand, strategy):
        while True:
            total=self.calculate_total(hand)
            choice=strategy.decide_hit_or_stand(hand, total)
            if choice=='hit':
                hand.append(self.deal_card())
                total = self.calculate_total(hand)
                print("Hand:", hand, "Total", total)
                if total > 21:
                    print("Bust!")
                    return False
            else:
                return True



    def deal_cards(self):
        return [self.deal_card(), self.deal_card()]

    def play_round(self, bet_amount):
        self.deck_check()
        bet=Blackjack_bet(bet_amount)

        player_hand=self.deal_cards()
        dealer_hand=self.deal_cards()

        print("*********** New Round ***********")
        print("Your hand is ", player_hand, "Your total is", self.calculate_total(player_hand))
        print("Dealer's visible card is  ", dealer_hand[0])

        player_strategy=Human_Player_Strategy()
        dealer_strategy=Dealer_Player_Strategy()

        player_in_game=self.play_turn(player_hand, player_strategy)
        if player_in_game:
            print("Dealer's turn:")
            self.play_turn(dealer_hand, dealer_strategy)
            print("Dealer's hand is ", dealer_hand, "Dealer's total is", self.calculate_total(dealer_hand))

            dealer_total=self.calculate_total(dealer_hand)
            player_total=self.calculate_total(player_hand)

            if dealer_total>21 or player_total>dealer_total:
                result="You won!"
                print(result)
                self.account.deposit(bet.payout_win())
            elif dealer_total>player_total:
                result="You lost!"
                print(result)
            else:
                result="Draw!"
                print(result)
                self.account.deposit(bet.payout_draw())

            with open(self.history_filename, 'a') as f:
                f.write(f"\nresult: {result}\n")
                f.write(f"Amount bet: {bet_amount}      ")
                if result=="You won!":
                    f.write(f"Amount won {bet.payout_win()}")
                elif result=="You lost!":
                    f.write(f"Amount lost {bet_amount}")
                f.write(f"\nPlayer hand {player_hand}, Player hand total: {player_total}\n")
                f.write(f"Dealer hand {dealer_hand}, Dealer hand total: {dealer_total}\n")

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

            if bet_amount > self.account.get_balance():
                print("You don't have enough money")

            self.account.withdraw(bet_amount)
            self.play_round(bet_amount)

            again=input("Do you want to play again?").lower()

            if again!='yes':
                print("Thank you for playing")
                break


if __name__ == '__main__':
    myaccount = Account()
    myaccount.deposit(100)
    game=BlackjackGame(myaccount)
    game.start()



