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