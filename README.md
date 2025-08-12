# Keylogger (Educational Only)

This is a simple **educational keylogger** written in Python. It logs keystrokes, timestamps, and the active window title. Use it responsibly **only on your own machine** or with full user consent.

---

## Legal Disclaimer

> This project is for **educational purposes only**.  
> Unauthorized monitoring of someone else's computer is **illegal** and **unethical**.  
> Always get **explicit permission** before running this on any system you do not personally own.

---

## Features

- Logs:
  - Pressed keys
  - Timestamp of the event
  - Active application/window name
- Saves logs to a text file (`key_log.txt`)

---

## Requirements

- Python 3.x
- `pynput`
- `pywin32` (for Windows active window capture)

### Install dependencies:

```bash
pip install pynput pywin32
```

## Sample Output (key_log.txt)

2025-08-06 19:40:12 | Notepad | h

2025-08-06 19:40:13 | Notepad | e

2025-08-06 19:40:13 | Notepad | l

2025-08-06 19:40:14 | Notepad | l

2025-08-06 19:40:14 | Notepad | o

2025-08-06 19:40:14 | Notepad | [Key.space]

This provides clear visibility into when, where, and what was typed.

## Usage

```bash
python keylogger.py
```

- Press ESC key to stop the logger.
- Output is saved in key_log.txt.

##  Notes
- Works best on Windows (due to win32gui for window capture)
- You can adapt this to Linux/Mac using xdotool, pyobjc, or other OS-specific modules.

## Security Best Practices
- Never use this tool without the user’s permission.
- Do not distribute or run this on any system you do not control.

## License
This project is licensed under the MIT License.
