class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        if self.find(card.name):
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        if self.find(card):
            self.cards.remove(self.find(card))
            self.count -= 1

    def find(self, name):
        for c in self.cards:
            if c.name == name:
                return c
