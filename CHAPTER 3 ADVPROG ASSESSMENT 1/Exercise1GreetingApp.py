import tkinter as tk
from tkinter import ttk, messagebox

# Function to update greeting
def update_greeting():
    name = entry_name.get().strip()
    color = color_var.get()

    if name == "":
        messagebox.showwarning("Input Required", "Please enter your name!")
        return
    
    greeting = f"Hello, {name}! Welcome!"
    label_greeting.config(text=greeting, fg=color)

# Main window
window = tk.Tk()
window.title("Greeting App")
window.geometry("450x300")
window.resizable(False, False)
window.configure(bg="#dce6f2")

# ------------------- Input Frame -------------------
input_frame = tk.Frame(window, bg="#cde7f0", bd=5, relief="groove")
input_frame.pack(pady=10, padx=10, fill="x")

# Title label
label_title = tk.Label(input_frame, text="Greeting App", font=("Helvetica", 16, "bold"),
                       fg="blue", bg="#cde7f0")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Name label and entry
label_name = tk.Label(input_frame, text="Enter your name:", font=("Arial", 12), bg="#cde7f0")
label_name.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_name = tk.Entry(input_frame, width=25)
entry_name.grid(row=1, column=1, padx=5, pady=5)

# Color selection dropdown
label_color = tk.Label(input_frame, text="Choose color:", font=("Arial", 12), bg="#cde7f0")
label_color.grid(row=2, column=0, padx=5, pady=5, sticky="e")

color_var = tk.StringVar(value="black")
color_menu = ttk.Combobox(input_frame, textvariable=color_var, width=22,
                          values=["red", "green", "blue", "purple", "orange", "black"])
color_menu.grid(row=2, column=1, padx=5, pady=5)

# Update button
btn_update = tk.Button(input_frame, text="Update Greeting", font=("Arial", 11, "bold"),
                       bg="lightgreen", command=update_greeting)
btn_update.grid(row=3, column=0, columnspan=2, pady=10)

# ------------------- Display Frame -------------------
display_frame = tk.Frame(window, bg="#f7f7f7", bd=5, relief="ridge")
display_frame.pack(pady=10, padx=10, fill="both", expand=True)

label_greeting = tk.Label(display_frame, text="", font=("Arial", 14, "bold"),
                          bg="#f7f7f7", wraplength=400)
label_greeting.pack(pady=20)

# Run main loop
window.mainloop()