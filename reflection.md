# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.
When I first ran the game, it appeared to work, but several behaviors were incorrect. The hint system seemed buggy. I also found that the New Game button did not restart the game. 

| Input                  | Expected Behavior      | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Secret number 74, guess 1|Should say "Go higher" |Said "Go lower"   |none |
|Secret number 72, guess 80|Should say "Go lower" |Said "Go higher"  |none |
| Clicked New Game | Should reset the game and generate a new secret number | Game did not restart until browser refresh | none |

Additional Issues: 
1.  After starting a new game, the previous guess remains in the input box instead of clearing.
2. Entering a new guess requires extra clicking before the input feels responsive.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ChatGPT and the AI assistant in VS Code for this project. One correct suggestion was identifying that the hint messages in check_guess() were reversed. I verified this by comparing the output to the secret number and then testing the code. One misleading suggestion was assuming the pytest tests were correct. After running pytest, I discovered the tests expected a string, but check_guess() returns a tuple. I verified this by reading the function and looking at the error produced.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

For the hint bug, I tested guesses above and below the secret number and confirmed the messages were correct. For the New Game bug, I won a game and clicked New Game to verify that the game restarted properly. I used pytest to verify the behavior of check_guess(). After updating the tests to match the return value, all three tests passed. This gave me confirmation that the logic was correct. AI helped me understand why the tests were failing. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the whole script whenever the user interacts with a botton or input. So normal variables can reset. st.session_state is like the app's memory because it keeps values such as the secret number, score, attempts, status and history across reruns. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I want to reuse testing one bug at a time instead of trying to fix everything at once. I also want to keep using pytest. Next time I work with AI on code I would ask it to explain the logic before asking it to fix. This project made me realize that AI generated code can look great but still contain bugs. So I need to verify it with my own tests. 