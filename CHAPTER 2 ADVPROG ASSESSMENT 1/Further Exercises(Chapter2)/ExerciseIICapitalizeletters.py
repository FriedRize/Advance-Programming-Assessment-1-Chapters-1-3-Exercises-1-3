import tkinter as tk
from tkinter import messagebox

# Function to convert text to uppercase
def to_uppercase():
    user_text = entry_text.get()
    if user_text.strip() == "":
        messagebox.showwarning("Input Required", "Please enter some text!")
    else:
        result = user_text.upper()
        label_result.config(text=f"Uppercase Text: {result}")

# Create main window
window = tk.Tk()
window.title("Uppercase Converter")
window.geometry("400x250")
window.resizable(False, False)
window.configure(bg="#f0f8ff")

# Title label
label_title = tk.Label(window, text="Convert Text to UPPERCASE",
                       font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="darkblue")
label_title.pack(pady=10)

# Entry label and input box
label_prompt = tk.Label(window, text="Enter your text:", bg="#f0f8ff", font=("Arial", 11))
label_prompt.pack(pady=5)

entry_text = tk.Entry(window, width=40)
entry_text.pack(pady=5)

# Button to convert text
btn_convert = tk.Button(window, text="Convert", bg="lightgreen", font=("Arial", 11, "bold"),
                        command=to_uppercase)
btn_convert.pack(pady=10)

# Label to show result
label_result = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="#f0f8ff", fg="darkred", wraplength=350)
label_result.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()