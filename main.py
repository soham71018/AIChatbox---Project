import pyautogui
import time
import pyperclip
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    api_key="Your API " #inster your api here
)

def is_last_message_from_sender(chat_log, sender_name="Sohu"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False
    
    

# Step 1: Click to open the app (e.g., WhatsApp or Chrome)
pyautogui.moveTo(1125, 1062, duration=0.5)
pyautogui.click()
time.sleep(5)  # Let the app load

while True:
    time.sleep(5)  # Wait before checking again

    # Step 2: Select text by dragging from top-left to bottom-right of chat area
    pyautogui.moveTo(436, 90, duration=0.5)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.dragTo(1465, 896, duration=1, button='left')
    pyautogui.mouseUp()

    # Step 3: Copy selected text
    time.sleep(0.5)
    pyautogui.hotkey('command', 'c')
    time.sleep(0.5)

    pyautogui.click(677, 202)  # Deselect after copy

    # Step 4: Get chat content
    chat_history = pyperclip.paste()
    print("Copied text:", chat_history)

    # Step 5: Check if last message is from Sohu
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Naruto who speaks Hindi and English. You are from India and you're a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)."},
                {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Sohu: "},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 6: Click input box
        pyautogui.click(792, 1031)
        time.sleep(1)

        # Step 7: Paste response
        pyautogui.hotkey('command', 'v')    
        time.sleep(1)

        # Step 8: Send message
        pyautogui.press('enter')
