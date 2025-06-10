import random
from typing import List
from utils.card import Card

class Player:
    def __init__(self, name: str):
        """
        Class representing a player in the card game.
        :param name: The name of the player.
        :attribute cards: A list of Card instances held by the player.
        :attribute turn_count: An integer tracking the number of turns taken.
        :attribute number_of_cards: An integer representing the number of cards the player holds.
        :attribute history: A list of Card instances already played by the player.
        """
        self.name = name
        self.cards: list[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: list[Card] = []

    def __str__(self):
        """
        Method to return a string representation of the player.
        :return: A string with player name, card count and number of turns played.
        """
        return f"Player {self.name} | Cards: {self.number_of_cards} | Turns played: {self.turn_count}"

    def play(self) -> Card:
        """
        Method to randomly choose and play a card from the player's hand.
        - Chooses a card at random.
        - Removes it from the player's cards.
        - Adds it to the player's history.
        - Updates turn and card counters.
        :return: The Card instance that was played.
        """
        chosen_card = random.choice(self.cards)
        self.cards.remove(chosen_card)
        self.history.append(chosen_card)
        self.turn_count += 1
        self.number_of_cards -= 1
        print(f"{self.name} {self.turn_count} played: {chosen_card.value} {chosen_card.icon}")
        return chosen_card

class Deck:
    def __init__(self):
        """
        Class representing a deck of playing cards.
        :attribute cards: A list of Card instances contained in the deck.
        """
        self.cards: list[Card] = []

    def fill_deck(self):
        """
        Method to fill the deck with 52 unique cards (13 values per 4 suits).
        """
        icons = ['♥', '♦', '♣', '♠']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for icon in icons:
            for value in values:
                if icon in ['♥', '♦']:
                    self.cards.append(Card('red', icon, value))
                else:
                    self.cards.append(Card('black', icon, value))

    def shuffle(self):
        """
        Method to shuffle the deck of cards randomly.
        """
        random.shuffle(self.cards)

    def distribute(self, players: List[Player]):
        """
        Method to evenly distribute cards among the given list of players.
        :param players: A list of Player instances to receive cards.
        """
        card_per_player_number = len(self.cards) // len(players)
        for player in players:
            player.cards.extend(self.cards[:card_per_player_number])
            player.number_of_cards += card_per_player_number
            self.cards = self.cards[card_per_player_number:]