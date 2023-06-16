
import pyautogui
import time
import keyboard


'''
The program will start to run 3s after executing for 30s, ctrl e kills the process 

'''



# Delay before starting the scroll (in seconds)
start_delay = 3

# Total duration of the scroll (in seconds)
scroll_duration = 5

# Delay between each scroll action (in seconds)
scroll_delay = 0.0001

# Calculate the number of scroll actions based on the scroll duration and delay
num_scrolls = int(scroll_duration / scroll_delay)

# Flag to indicate if scrolling is active
scrolling_active = True

# Function to stop scrolling when Ctrl+G is pressed
def stop_scrolling(event):
    global scrolling_active
    if event.name == "e" and keyboard.is_pressed("ctrl"):
        scrolling_active = False

# Register the hotkey Ctrl+G to stop scrolling
keyboard.on_press(stop_scrolling)

# Wait for the start delay
time.sleep(start_delay)

# Get the current mouse position
mouse_x, mouse_y = pyautogui.position()

# Perform the scroll actions
for _ in range(num_scrolls):
    if scrolling_active:
        pyautogui.scroll(-50, x=mouse_x, y=mouse_y)  # Scroll up by 1 unit at the current mouse position
        time.sleep(scroll_delay)
    else:
        break

# Unregister the hotkey after scrolling is stopped
keyboard.unhook_all()


