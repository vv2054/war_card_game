from war_card_game import WarCardGame
from player import Player

if __name__ == "__main__":
    wcg = WarCardGame()
    wcg.shuffle()
    set1, set2 = wcg.split_cards()
    player1, player2 = Player(set1), Player(set2)
    print(wcg.play(player1, player2))
