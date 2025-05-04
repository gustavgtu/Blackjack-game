import random

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