# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  When I first ran the game, I noticed the difficulty settings felt off. Easy goes from 1-20 with 6 attempts, Normal goes from 1-100 with 8 attempts, but Hard only goes from 1-50 with 5 attempts. Hard should be the most challenging, but its number range is actually smaller than Normal's, which doesn't make sense. A harder level should have a wider range of numbers, not a narrower one.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The difficulty ranges don't scale correctly — Hard (1–50, 5 attempts) is actually easier than Normal (1–100, 8 attempts).
  2. The hint always displays "Go LOWER" regardless of the guess, even when entering a negative number or a smaller number than the secret.
  3. The input field accepts negative numbers, which fall outside the valid guess range for any difficulty level.
  4. The "New Game" button does not wor, pressing it does not reset the game.
  5. The secret number is always drawn from 1–100 regardless of the selected difficulty.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used Claude (via Claude Code) as my primary AI assistant throughout this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  Claude correctly identified that the hint logic was broken because the comparison was inverted. It was always returning "Go LOWER" regardless of the actual guess. It suggested flipping the condition so that `guess < secret_number` shows "Go HIGHER" and `guess > secret_number` shows "Go LOWER." I verified this by testing guesses below, above, and equal to the secret number and confirming each hint was correct.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  When I asked Claude to fix the number ranges based on difficulty, it set the Hard level to 1–200 instead of the intended range. That wasn't what I asked for. Because I reviewed Claude's suggested code before applying it, I caught the issue and corrected the range myself before accepting the change.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.

  I decided a bug was fixed when I could reproduce the original broken behavior, apply the fix, and then confirm the correct behavior via UI and test cases. For example, for the hint bug I tested guesses that were lower, higher, and exactly equal to the secret number to make sure all three branches of the hint logic worked correctly.

- Did AI help you design or understand any tests? How?

  Yes, I asked Claude what edge cases I should test for the hint logic, and it pointed out that I should explicitly test a guess of exactly the secret number, a guess of the minimum value (1), and a guess of the maximum value for the current difficulty.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  I want to keep the practice of listing all observed bugs before fixing any of them. Early in this project I started patching things as soon as I spotted them, which caused me to miss interactions between bugs. Making a written bug list first let me see the full picture and prioritize fixes in a smarter order.

- What is one thing you would do differently next time you work with AI on a coding task?

  I would always paste the exact relevant code snippet into my prompt instead of describing it in English. Several times AI gave me an off-target suggestion because it was working from my description rather than the actual code, giving it the real code made its answers immediately more accurate.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

  Before this project I assumed AI-generated code was either correct or obviously wrong. Now I understand it can be subtly wrong in ways that look plausible, so I treat every AI suggestion as a starting point that needs to be read, reasoned about, and tested, not just copy-pasted.
