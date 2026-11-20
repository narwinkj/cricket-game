# Hand Cricket (Odd or Even) - Python Console Game

A console-based hand-cricket game built in Python, played against the computer. Developed completely on my own as my first Python project, with no AI assistance.

## Features

- Toss with Heads or Tails; the winner chooses batting or bowling (the computer picks randomly if it wins)
- Two innings with a target chase
- Batter and bowler each pick a number from 1 to 10
- Special moves: **Stroke** (batter) and **Spin** (bowler)
- Declare option: type `d` to declare the match
- Ball and over tracking with over-end score updates
- Input validation (invalid entries do not cost a ball)
- Match summary with winner and margin, plus a replay option

## How to Play

1. **Toss:** call Heads or Tails.
2. **Choose:** if you win the toss, pick Batting or Bowling.
3. **Each ball:** you and the computer both choose a number from 1 to 10 (or a special move).
4. **Out:** the batter is out if both numbers match, or if the batter plays Stroke against Spin.
5. **Runs:** otherwise, the batter scores the number they chose.
6. **Chase:** the second innings ends when the target is passed or the batter is out.
7. **Declare:** type `d` at any ball to declare the match.

## Requirements

- Python 3.8 or higher (uses the walrus operator `:=`)
- No external libraries (uses only `random` and `time`)

## How to Run

    git clone https://github.com/narwinkj/cricket-game.git
    cd cricket-game
    python main.py

Replace `main.py` with the actual name of your Python file.

## Concepts Used

- Loops and conditionals
- Dictionaries and lists
- f-strings
- Walrus operator
- `random` and `time` modules
- Input validation

## Known Limitations

- Repeated code across the innings blocks (about 337 lines)
- Variable names like `Score_1` to `Score_4` are not very descriptive
- Console only, no GUI or saved stats

## Future Improvements

- [ ] Refactor into functions and classes
- [ ] AI opponent that learns the player's pattern and predicts moves
- [ ] GUI version
- [ ] Save match history and player statistics

## Author

**Narwin K J**
B.Tech (AI/ML), Woxsen University

Feedback and suggestions are welcome..!!
