from abc import ABC, abstractmethod

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