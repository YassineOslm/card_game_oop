# Card Game Project

## Description
This project is a basic simulation of a card game developed in Python. It was created as part of a technical challenge for a job application at the fictional company **WeTakeYourMoney**, an online casino.

The current version lays the groundwork for a card game engine, handling deck generation, shuffling, card distribution to players, and a turn-based loop where each player plays one card per round until no cards remain.

### The Mission
> You apply for a job as a developer for an online casino called WeTakeYourMoney. They are interested in your profile. During the interview challenge, they ask you to build a card game in Python.

### Must-have features
- A full deck of 52 cards is generated.
- The deck is shuffled and distributed equally among all players.
- Each player plays one card per turn.
- The game continues until all players have no cards left.

### Nice-to-have features (to be implemented later)
- Make the game interactive (ask players to choose which card to play).
- Add game-over conditions (e.g., no moves left, player quits).
- Award points for the strongest card played each turn.
- Declare a winner at the end based on points.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/card-game.git
   cd card-game
   ```

2. Make sure you are using Python 3.9 or higher.

3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. No additional dependencies are required as the game uses only Python’s standard library.

---

## Usage

To start the game, simply run:
```bash
python main.py
```

You will see each player drawing and playing cards, turn by turn, until the deck is empty and the game ends.

---

Enjoy building on top of this foundation to create your own card game!