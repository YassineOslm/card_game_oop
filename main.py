from utils.game import Board
from utils.player import Player

def main():
    """
    Function that starts the card game by:
    - Creating a Board instance.
    - Creating a list of Players.
    - Assigning players to the board.
    - Launching the game loop.
    """
    board = Board()
    player_names = ["Alice", "Bob", "Charlie", "Diana"]
    board.players = [Player(name) for name in player_names]
    board.start_game()

if __name__ == "__main__":
    main()