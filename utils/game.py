from utils.player import Player, Deck
from utils.card import Card


class Board:
    def __init__(self):
        """
        Class that represents the game board.
        :attribute players: A list of Player instances involved in the game.
        :attribute turn_count: An integer counting the number of turns played.
        :attribute active_cards: A list of Card instances currently in play.
        :attribute history_cards: A list of all Card instances played so far.
        """
        self.players: list[Player] = []
        self.turn_count = 0
        self.active_cards: list[Card] = []
        self.history_cards: list[Card] = []

    def __str__(self):
        """
        Method to provide a readable string representation of the game state.
        :return: A string summary of the current board state.
        """
        player_str = "\n".join(str(player) for player in self.players)
        return (
            f"===== GAME STATE =====\n"
            f"Turn: {self.turn_count}\n"
            f"Active cards: {[str(c) for c in self.active_cards]}\n"
            f"History length: {len(self.history_cards)}\n"
            f"Players:\n{player_str}\n"
            f"======================"
        )

    def isAllPlayersOutOfCards(self):
        """
        Method that checks if all players have no cards left.
        :return: True if all players are out of cards, False otherwise.
        """
        return not any(player.number_of_cards == 0 for player in self.players)

    def start_game(self):
        """
        Method to start and control the main game loop.
        - Creates and fills a deck.
        - Shuffles and distributes cards to all players.
        - Repeats turn-based play until no cards are left.
        - Displays the result of each turn.
        """
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute(self.players)
        while self.isAllPlayersOutOfCards():
            self.active_cards = []

            if (self.turn_count == 0):
                print("=" * 40)

            for player in self.players:
                if player.number_of_cards > 0:
                    card = player.play()
                    self.active_cards.append(card)
            self.history_cards.extend(self.active_cards)
            self.turn_count += 1


            print(f"\n--- Tour {self.turn_count} ---")
            print("Cards played in this turn:", end = "")
            for card in self.active_cards:
                print(f"  {card.value} {card.icon}", end=" ; ")
            print()
            print(f"Total number of cards played : {len(self.history_cards)}")
            print("=" * 40)