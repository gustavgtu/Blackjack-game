class Blackjack_bet:
    def __init__(self, bet_amount):
        self.__bet_amount=bet_amount

    def payout_win(self):
        return self.__bet_amount*2

    def payout_draw(self):
        return self.__bet_amount

    def get_bet_amount(self):
        return self.__bet_amount