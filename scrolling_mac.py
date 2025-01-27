import pyautogui
import time
from pynput import keyboard
import threading

'''
The program will scroll continuously after a 3-second delay.
Press Control + Command + E to stop the scrolling.
'''

# Delay before starting the scroll (in seconds)
start_delay = 3

# Delay between each scroll action (in seconds)
scroll_delay = 0.01

# Flag to indicate if scrolling is active
scrolling_active = True

# Key combination to stop scrolling
stop_keys = {keyboard.Key.ctrl, keyboard.Key.cmd, keyboard.KeyCode(char='e')}
current_keys = set()


def scroll_task():
    """
    Perform the scrolling action until stopped manually.
    """
    global scrolling_active
    while scrolling_active:
        pyautogui.scroll(-50)  # Scroll down by 50 units
        time.sleep(scroll_delay)


def on_press(key):
    """
    Detect when keys are pressed and check for the stop combination (Control + Command + E).
    """
    global scrolling_active, current_keys
    current_keys.add(key)
    if stop_keys.issubset(current_keys):
        scrolling_active = False
        return False  # Stop the listener


def on_release(key):
    """
    Remove keys from the current set when released.
    """
    current_keys.discard(key)


# Start the scrolling task in a separate thread
scroll_thread = threading.Thread(target=scroll_task)

# Start the key listener for Control + Command + E
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Allow time to prepare
print(f"Scrolling will start in {start_delay} seconds...")
time.sleep(start_delay)

# Start scrolling
print("Scrolling in progress. Press Control + Command + E to stop.")
scroll_thread.start()

# Wait for the listener and scrolling thread to finish
scroll_thread.join()
listener.join()

print("Scrolling stopped.")
