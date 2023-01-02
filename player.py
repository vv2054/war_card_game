class Player:
    def __init__(self, cards):
        self.cards = cards
        pass

    def get_cards(self):
        return self.cards
    
    def get_cards_counts(self):
        return len(self.cards)

    def add_pot(self, pot):
        self.cards += pot