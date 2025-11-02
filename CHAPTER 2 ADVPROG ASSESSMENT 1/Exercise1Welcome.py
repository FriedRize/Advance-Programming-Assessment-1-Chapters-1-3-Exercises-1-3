import tkinter as tk
from tkinter import font

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Welcome Window")

# Set default window size (width x height)
window.geometry("400x200")

# Disable window resizing
window.resizable(False, False)

# Set background color
window.configure(bg="#ADD8E6")  # Light blue background

# Create a custom font for the label
custom_font = ("Helvetica", 18, "bold")

# Create a label with welcome message
welcome_label = tk.Label(window, 
                         text="Welcome to Tkinter GUI!", 
                         font=custom_font, 
                         bg="#ADD8E6", 
                         fg="darkblue")

# Position the label in the center
welcome_label.pack(expand=True)

# Run the Tkinter event loop
window.mainloop()