# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the AI assistant to help plan a feature extension for the guessing game. I chose a Guess History sidebar because the app already stores guesses, but the history is only visible in the Developer Debug section.

**What did the agent do?**

The AI suggested displaying st.session_state.history in the sidebar. I updated app.py to add Guess History section that lists each guess during the game and shows "No guesses yet" before the first guess.

**What did you have to verify or fix manually?**

I manually tested the app and saw the history display felt delayed. I fixed this by moving the Guess History display lower in app.py after the submit logic. So the sidebar updates immediately after each guess.
---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number("-5")| Suggest edge case test for parse_guess() that might reveal bugs | Verify that parse_guess("-5") returns a valid integer and no error | Yes | Negative numbers are unusual inputs that the user may enter, so I wanted to handle them correctly |
| Decimal input("42.7") | Suggest edge case tests for parse_guess() that might reveal bugs | Verify that parse_guess("42.7") converts the value to 42 and does not produce an error | Yes | The code handles decinmal strings, so I wanted to verify if it was implemented correctly |
| Non numeric text ("abc") | Suggest edge case tests for parse_guess() that might reveal bugs | Verify that parse_guess("abc") returns an error message instead of crashing | Yes | Users often enter invalid text and the game should respond correctly. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Add professional docstrings to every function in logic_utils.py and review the file for simple PEP 8 readability issues.
```

**Linting output before:**

```
No formal linter was run. I reviewed the file manually and used pytest to confirm the changes did not break behavior.
```

**Changes applied:**

I added more detailed docstrings to the functions in logic_utils.py. I also improved readability by spacing functions and simplifying one else branch in check_guess(). After the documentation, I ran pytest and confirmed that all 6 tests passed.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
