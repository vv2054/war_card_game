from random import shuffle
from player import Player

class WarCardGame:
    """Game initializer
    """
    def __init__(self):
        self.cards = [(j, i) for i in range(1, 5) for j in range(2, 15)]   # Ace -> 14
        self.suits = {1: 'Clubs', 2: 'Diamonds', 3: 'Hearts', 4: 'Spades'}
        self.pot = []
    
    def shuffle(self):
        shuffled_cards = [j for j in range(52)]
        # shuffle(shuffled_cards)
        self.cards = [self.cards[i] for i in shuffled_cards]
    
    def split_cards(self):
        return self.cards[:26], self.cards[26:]
    
    def player_wins(self, player):
        player.add_pot(self.pot)
        self.empty_pot()
    
    def empty_pot(self):
        self.pot = []
    
    def play(self, player1, player2):
        while True: # if none of the player won yet
            player1_card_count = player1.get_cards_counts()
            player2_card_count = player2.get_cards_counts()
            if (player1_card_count == player2_card_count == 0):  return 'MATCH TIED'
            elif player1_card_count == 52:  return 'PLAYER 1 WON'
            elif player2_card_count == 52:  return 'PLAYER 2 WON'
            else:
                print(player1_card_count, player2_card_count)
                print('------------------')

            player1_top_card = player1.get_cards().pop(0)
            player2_top_card = player2.get_cards().pop(0)

            if player1_top_card[0] > player2_top_card[0]:   # player 1 wins
                self.pot.extend([player1_top_card, player2_top_card])
                self.player_wins(player1)
                
            elif player1_top_card[0] < player2_top_card[0]:   # player 2 wins
                self.pot.extend([player1_top_card, player2_top_card])
                self.player_wins(player2)

            else:
                self.pot.extend([player1_top_card, player2_top_card])
        

            
    
    
