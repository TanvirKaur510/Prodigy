import re
import tkinter as tk
from tkinter import messagebox


# Function to check password complexity
def check_password_complexity(password):
    complexity_score = 0

    # Criteria 1: Length
    if len(password) >= 8:
        complexity_score += 1
    if len(password) >= 12:
        complexity_score += 1

    # Criteria 2: Lowercase letters
    if re.search(r'[a-z]', password):
        complexity_score += 1

    # Criteria 3: Uppercase letters
    if re.search(r'[A-Z]', password):
        complexity_score += 1

    # Criteria 4: Digits
    if re.search(r'[0-9]', password):
        complexity_score += 1

    # Criteria 5: Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        complexity_score += 1

    # Criteria 6: No repeated characters (more than 2 consecutive)
    if not re.search(r'(.)\1\1', password):
        complexity_score += 1

    return complexity_score


# Function to evaluate and display password strength
def evaluate_password():
    password = password_entry.get()
    complexity_score = check_password_complexity(password)

    if complexity_score <= 2:
        strength = "Weak"
    elif complexity_score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

        # Show password if it's very strong
        if complexity_score >= 6:
            messagebox.showinfo("Password Strength", f"Password Strength: {strength}\nYour password is: {password}")
            return

    messagebox.showinfo("Password Strength", f"Password Strength: {strength}")


# Function to clear the input field
def clear_input():
    password_entry.delete(0, tk.END)


# GUI setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x250")
root.configure(bg='#f0f0f0')

# Password input label and entry
password_label = tk.Label(root, text="Enter Password:", font=('Helvetica', 12, 'bold'), bg='#f0f0f0', fg='#333333')
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=30, show='*', font=('Helvetica', 12))
password_entry.pack(pady=5)

# Buttons
check_button = tk.Button(root, text="Check Complexity", command=evaluate_password, bg='#4CAF50', fg='white',
                         font=('Helvetica', 12, 'bold'))
check_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_input, bg='#f44336', fg='white',
                         font=('Helvetica', 12, 'bold'))
clear_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
