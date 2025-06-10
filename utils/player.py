import random
from typing import List
from utils.card import Card

class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards: list[Card] = []
        self.turn_count: int = 0
        self.number_of_cards: int = 0
        self.history: list[Card] = []

    def __str__(self):
        return f"Player {self.name} | Cards: {self.number_of_cards} | Turns played: {self.turn_count}"

    def play(self) -> Card:
        chosen_card = random.choice(self.cards)
        self.cards.remove(chosen_card)
        self.history.append(chosen_card)
        self.turn_count += 1
        self.number_of_cards -= 1
        print(f"{self.name} {self.turn_count} played: {chosen_card.value} {chosen_card.icon}")
        return chosen_card

class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def fill_deck(self):
        icons = ['♥', '♦', '♣', '♠']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for icon in icons:
            for value in values:
                if icon in ['♥', '♦']:
                    self.cards.append(Card('red', icon, value))
                else:
                    self.cards.append(Card('black', icon, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def distribute(self, players: List[Player]):
        card_per_player_number = len(self.cards) // len(players)
        for player in players:
            player.cards.extend(self.cards[:card_per_player_number])
            player.number_of_cards += card_per_player_number
            self.cards = self.cards[card_per_player_number:]