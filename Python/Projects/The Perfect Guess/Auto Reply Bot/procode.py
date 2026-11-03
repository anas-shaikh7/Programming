import pyautogui
import pyperclip
import time
from openai import OpenAI


client = OpenAI(
api_key = "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",
)
# Click on the icon at (1292, 1048)

# while True

pyautogui.click(x=1123, y=1048)

# Add a short delay to ensure the click is registered
time.sleep(0.5)

# Drag from (1259, 219) to (1860, 704) to select the text
pyautogui.moveTo(1443,530)
pyautogui.dragTo(1552, 858, duration=1, button='left')

# Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1369, 604)

# Add a short delay to ensure the text is copied
time.sleep(0.5)

# Get the text from the clipboard
selected_text = pyperclip.paste()

# Print the selected text (for verification)
print(selected_text)


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are my assistant,  named Jarvis Pro Player better than the simple Jarvis."},
    {"role": "user", "content": "When will cambridge result 2024 arive?"}
  ]
)

response = completion.choices[0]. selected_text
pyperclip.copy(response)

# Step 5: Click at (1556, 933) to focus the input area
pyautogui.click(x=1556, y=933)

# Add a short delay to ensure the click is registered
time.sleep(0.5)

# Step 6: Paste the text from the clipboard
pyautogui.hotkey('ctrl', 'v')

# Step 7: Press Enter
pyautogui.press('enter')
