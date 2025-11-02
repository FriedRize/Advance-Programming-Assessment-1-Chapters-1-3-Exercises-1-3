import tkinter as tk
from tkinter import messagebox

def count_characters():
    text = entry_text.get()

    # Initialize counters
    vowels = 0
    consonants = 0
    special_chars = 0

    # Define vowels
    vowel_set = "aeiouAEIOU"

    # Count characters
    for char in text:
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1
        elif not char.isspace():
            special_chars += 1

    total_letters = vowels + consonants

    # Display results
    label_result.config(
        text=f"Total letters: {total_letters}\n"
             f"Vowels: {vowels}\n"
             f"Consonants: {consonants}\n"
             f"Special characters: {special_chars}"
    )

# Create main window
window = tk.Tk()
window.title("Vowel & Consonant Counter")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#e8f0fe")

# Title label
label_title = tk.Label(window, text="Vowel and Consonant Counter",
                       font=("Helvetica", 14, "bold"), bg="#e8f0fe", fg="darkblue")
label_title.pack(pady=10)

# Entry field
label_prompt = tk.Label(window, text="Enter a word or sentence:", bg="#e8f0fe", font=("Arial", 11))
label_prompt.pack(pady=5)

entry_text = tk.Entry(window, width=40)
entry_text.pack(pady=5)

# Button to process input
btn_count = tk.Button(window, text="Count", bg="lightgreen", font=("Arial", 11, "bold"),
                      command=count_characters)
btn_count.pack(pady=10)

# Label to display results
label_result = tk.Label(window, text="", font=("Arial", 11), bg="#e8f0fe", justify="left")
label_result.pack(pady=10)

# Run the window
window.mainloop()