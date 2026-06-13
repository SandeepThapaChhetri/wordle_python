# Wordle (Python)

A terminal-based clone of the popular word-guessing game **Wordle**, built in Python as part of my journey learning the language.

This project documents every milestone of building a Wordle game from scratch — including game logic, letter-state evaluation (correct/present/absent), and a colored command-line interface.

## Features

- Random secret word chosen from a word list each time you play
- 6 attempts to guess a 5-letter word
- Color-coded feedback for each guess:
  - 🟩 **Green** — letter is correct and in the right position
  - 🟨 **Yellow** — letter is in the word but in the wrong position
  - ⬜ **White** — letter is not in the word
- Input validation (rejects guesses that aren't 5 letters or aren't in the word list)
- Visual results board displayed after each guess

## Demo

```
Number of words loaded: 1503

Type your guess: CRANE

Your results so far....


You have 5 attempts remaining.

┌───────────┐
│ C R A N E │
│ _ _ _ _ _ │
│ _ _ _ _ _ │
│ _ _ _ _ _ │
│ _ _ _ _ _ │
│ _ _ _ _ _ │
└───────────┘
```


## Project structure

wordle_python/
├── wordle.py          # Core game logic (Wordle class)
├── letter_state.py     # Represents the state of a single guessed letter
├── play_wordle.py       # Entry point - run this to play
├── data/
│   ├── wordle_words.txt  # Word list used for secrets and valid guesses
│   └── convert_words.py  # Helper script to generate/clean wordle_words.txt
└── README.md

## Getting started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SandeepThapaChhetri/wordle_python.git
   cd wordle_python
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   (Currently just [colorama](https://pypi.org/project/colorama/), used for colored terminal output.)

### Running the game

```bash
python play_wordle.py
```

You'll be prompted to enter a 5-letter word. After each guess, the board updates to show which letters were correct, present, or absent — keep guessing until you solve the word or run out of attempts!

## How it works

- **`wordle.py`** — Contains the `Wordle` class, which holds the secret word, tracks attempts, and evaluates guesses against the secret.
- **`letter_state.py`** — A small helper class (`LetterState`) representing a single letter's evaluation: whether it appears in the word, and whether it's in the correct position.
- **`play_wordle.py`** — The command-line interface: loads the word list, runs the game loop, takes user input, and renders the colored result board.

## What I learned

This project was my first real Python project, and helped me practice:

- Object-oriented design (classes, properties)
- Working with files and sets for fast lookups
- String manipulation and indexing
- Using third-party packages (`colorama`) for terminal styling
- Structuring a small Python project across multiple files

## Possible future improvements

- [ ] Handle duplicate letters correctly (e.g., guess "HELLO" vs secret "APPLE")
- [ ] Add unit tests for `Wordle` and `LetterState`
- [ ] Add a "play again" option without restarting the script
- [ ] Track and display win/loss statistics
- [ ] Support different word lengths or difficulty levels

## License

This project is open source and available under the [MIT License](LICENSE).