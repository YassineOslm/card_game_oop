from utils.game import Board
from utils.player import Player


def main():
    board = Board()
    player_names = ["Alice", "Bob", "Charlie", "Diana"]
    board.players = [Player(name) for name in player_names]
    board.start_game()


if __name__ == "__main__":
    main()
