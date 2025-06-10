class Symbol:

    def __init__(self, color: str, icon: str):
        self.color = color
        self.icon = icon

    def __str__(self):
        return f"{self.icon} ({self.color})"


class Card(Symbol):

    def __init__(self, color: str, icon: str, value: str):
        super().__init__(color, icon)
        self.value = value

    def __str__(self):
        return f"{self.value}{self.icon}"