def get_range_for_difficulty(difficulty: str):
    """
    Return the inclusive guessing range for a selected difficulty level.

    Args:
        difficulty: The selected difficulty name, such as "Easy",
            "Normal", or "Hard".

    Returns:
        A tuple containing the lowest and highest allowed guesses.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Convert raw user input into an integer guess.

    Args:
        raw: The raw text entered by the user.

    Returns:
        A tuple of three values:
        - ok: True if the input was successfully parsed, otherwise False.
        - guess_int: The parsed integer guess, or None if parsing failed.
        - error_message: An error message when parsing fails, otherwise None.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare a player's guess to the secret number.

    Args:
        guess: The player's parsed guess.
        secret: The target value the player is trying to guess.

    Returns:
        A tuple containing:
        - outcome: "Win", "Too High", or "Too Low".
        - message: A user-facing hint message.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        guess_text = str(guess)

        if guess_text == secret:
            return "Win", "🎉 Correct!"

        if guess_text > secret:
            return "Too High", "📉 Go LOWER!"

        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Calculate the updated score after a guess.

    Args:
        current_score: The score before applying the latest result.
        outcome: The result returned by check_guess().
        attempt_number: The current attempt count.

    Returns:
        The updated score after applying the scoring rules.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score