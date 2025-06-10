class Symbol:

    def __init__(self, color: str, icon: str):
        """
        Class representing a symbol used in a card.
        :param color: A string representing the color of the symbol (e.g., 'red' or 'black').
        :param icon: A single character representing the suit of the card (e.g., ♥, ♦, ♣, ♠).
        """
        self.color = color
        self.icon = icon

    def __str__(self):
        """
        Method that returns a string representation of the symbol.
        :return: A string with the icon and its color.
        """
        return f"{self.icon} ({self.color})"


class Card(Symbol):

    def __init__(self, color: str, icon: str, value: str):
        """
        Class representing a full playing card, inheriting from Symbol.
        :param color: The color of the card.
        :param icon: The suit symbol of the card.
        :param value: The value of the card (e.g., 'A', '2', ..., 'K').
        """
        super().__init__(color, icon)
        self.value = value

    def __str__(self):
        """
        Method that returns a string representation of the card.
        :return: A string combining the card's value and suit (e.g., "A♥").
        """
        return f"{self.value}{self.icon}"