import tkinter as tk
from tkinter import messagebox

class CaesarCipher:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Caesar Cipher")

        # Set the background image
        self.background_image = tk.PhotoImage(file="key.ppm")
        self.background_label = tk.Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame for the input text
        self.input_frame = tk.Frame(self.window, bg="#f0f0f0", bd=2, relief="groove")
        self.input_frame.place(x=50, y=50, width=400, height=200)

        # Create a label and text entry for the input text
        self.input_label = tk.Label(self.input_frame, text="Enter text to encrypt/decrypt:", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.input_label.place(x=10, y=10)
        self.input_entry = tk.Text(self.input_frame, width=40, height=10, font=("Arial", 12), bg="#ffffff", bd=2, relief="solid")
        self.input_entry.place(x=10, y=40)

        # Create a frame for the shift value
        self.shift_frame = tk.Frame(self.window, bg="#f0f0f0", bd=2, relief="groove")
        self.shift_frame.place(x=50, y=260, width=200, height=50)

        # Create a label and text entry for the shift value
        self.shift_label = tk.Label(self.shift_frame, text="Shift value:", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.shift_label.place(x=10, y=10)
        self.shift_entry = tk.Entry(self.shift_frame, width=5, font=("Arial", 12), bd=2, relief="solid")
        self.shift_entry.place(x=100, y=10)

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self.window, bg="#f0f0f0", bd=2, relief="groove")
        self.button_frame.place(x=50, y=320, width=400, height=50)

        # Create encrypt and decrypt buttons
        self.encrypt_button = tk.Button(self.button_frame, text="Encrypt", command=self.encrypt, font=("Arial", 12, "bold"), bg="#4CAF50", fg="#ffffff", relief="raised")
        self.encrypt_button.place(x=10, y=10)
        self.decrypt_button = tk.Button(self.button_frame, text="Decrypt", command=self.show_decrypt_options_window, font=("Arial", 12, "bold"), bg="#f44336", fg="#ffffff", relief="raised")
        self.decrypt_button.place(x=120, y=10)

        # Create a label to display the result
        self.result_label = tk.Label(self.window, text="Result:", bg="#ffffff", font=("Arial", 12, "bold"))
        self.result_label.place(x=50, y=380)
        self.result_text = tk.Text(self.window, width=40, height=10, font=("Arial", 12), bg="#ffffff", bd=2, relief="solid")
        self.result_text.place(x=50, y=410)

    def encrypt(self):
        try:
            text = self.input_entry.get("1.0", tk.END).strip()
            shift = int(self.shift_entry.get())
            result = ""

            for char in text:
                if char.isalpha():
                    ascii_offset = 65 if char.isupper() else 97
                    result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    result += char

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", result)
        except Exception as e:
            print(f"Error encrypting text: {e}")

    def show_decrypt_options_window(self):
        # Create a new window for decryption options
        decrypt_window = tk.Toplevel(self.window)
        decrypt_window.title("Decryption Options")

        # Add some padding and background color to the decryption window
        decrypt_window.configure(bg="#f0f0f0")

        # Create buttons for decryption options
        decrypt_entered_button = tk.Button(decrypt_window, text="Decrypt Entered Text", command=self.decrypt_entered_value, font=("Arial", 12, "bold"), bg="#2196F3", fg="#ffffff", relief="raised")
        decrypt_entered_button.pack(pady=10)

        decrypt_encrypted_button = tk.Button(decrypt_window, text="Decrypt Encrypted Text", command=self.decrypt_encrypted_value, font=("Arial", 12, "bold"), bg="#2196F3", fg="#ffffff", relief="raised")
        decrypt_encrypted_button.pack(pady=10)

    def decrypt_entered_value(self):
        try:
            text = self.input_entry.get("1.0", tk.END).strip()
            shift = int(self.shift_entry.get())
            result = ""

            for char in text:
                if char.isalpha():
                    ascii_offset = 65 if char.isupper() else 97
                    result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                else:
                    result += char

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", result)
        except Exception as e:
            print(f"Error decrypting entered text: {e}")

    def decrypt_encrypted_value(self):
        try:
            text = self.result_text.get("1.0", tk.END).strip()
            shift = int(self.shift_entry.get())
            result = ""

            for char in text:
                if char.isalpha():
                    ascii_offset = 65 if char.isupper() else 97
                    result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                else:
                    result += char

            self.result_text.delete("1.0", tk.END)
            self.result_text.insert("1.0", result)
        except Exception as e:
            print(f"Error decrypting encrypted text: {e}")

    def run(self):
        self.window.geometry("600x600")
        self.window.mainloop()

if __name__ == "__main__":
    cipher = CaesarCipher()
    cipher.run()
