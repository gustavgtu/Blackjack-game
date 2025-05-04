from abc import ABC, abstractmethod
from .hand import Hand
from .strategy import HumanPlayerStrategy, DealerPlayerStrategy

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