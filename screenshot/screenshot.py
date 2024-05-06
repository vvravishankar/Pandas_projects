#pip install Pillow
#pip install pyscreenshot
#pip install keyboard

import pyscreenshot
import keyboard
import datetime

def take_screenshot():
    # To capture the screen
    image = pyscreenshot.grab()

    # Generate timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # To save the screenshot
    image.save(r"C:\Users\VVRAVISH\Downloads\GitHUB\Python_learning\python_projects\screeshot\image\screenschot_{}.png".format(timestamp))

    print("Screenshot saved successfully.")

# Function to be called when the shortcut key is pressed
def on_triggered():
    print("Shortcut key pressed, taking screenshot...")
    take_screenshot()

# Register the shortcut key (Alt + S)
keyboard.add_hotkey('alt+s', on_triggered)

# Keep the script running
print("Press Alt + S to take a screenshot. Press Ctrl + C to exit.")
keyboard.wait('ctrl+c')
