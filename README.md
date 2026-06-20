# 🎮 Game Glitch Investigator: The Impossible Guesser

## 📝 Document Your Experience

The game is a Streamlit number guessing game where the player tries to guess a secret number within a limited number of attempts. 
While testing the game:
- I found that the hint messages were reversed, so guesses above the secret number said "GO HIGHER" and guesses below the secret number said "GO LOWER"
- I also found that the New Game button did not restart the game.

To fix these issues:
- I fixed the hint logic
- Reset the session state values for a new game
- Moved check_guess() into logic_utils.py
- Updated pytest tests

## 📸 Demo Walkthrough

1. User starts the app and selects a difficulty level
2. User enters a guess and received feedback based on whether the guess is high, low or correct.
3. User enters a guess below the secret number and the game returns "GO HIGHER"
4. User enters the correct secret number and the game shows a win message with the final score
5. User clicks "New Game" and the game resets the secret number, score, attempts, status and guess history.

## Screenshot

![Winning Game](screenshot-winning-game.png)

## 🧪 Test Results

```text
$ pytest
============================= test session starts ==============================
platform darwin -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
collected 6 items

tests/test_game_logic.py ......                                          [100%]

============================== 6 passed in 0.02s ===============================
```

## 🚀 Stretch Features

Added a temperature based hint system to improve user feedback: 
 - 🔥 Very Hot (within 5 of the secret number)
 - 🌡️ Warm (within 15 of the secret number)
 - 🥶 Cold (far from the secret number)

 This feature is implemented using the get_temperature_hint() function in app.py