import tkinter as tk
from tkinter import messagebox

# Function to perform arithmetic operations
def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operation == "mod":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 % num2

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed.")

# Create the main window
window = tk.Tk()
window.title("Arithmetic Operations GUI")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#f2f2f2")

# Title Label
label_title = tk.Label(window, text="Simple Arithmetic Calculator", 
                       font=("Helvetica", 14, "bold"), bg="#f2f2f2")
label_title.grid(row=0, column=0, columnspan=3, pady=10)

# Input fields
tk.Label(window, text="Enter First Number:", bg="#f2f2f2", font=("Arial", 11)).grid(row=1, column=0, pady=5, sticky="e")
entry_num1 = tk.Entry(window, width=20)
entry_num1.grid(row=1, column=1, pady=5)

tk.Label(window, text="Enter Second Number:", bg="#f2f2f2", font=("Arial", 11)).grid(row=2, column=0, pady=5, sticky="e")
entry_num2 = tk.Entry(window, width=20)
entry_num2.grid(row=2, column=1, pady=5)

# Buttons for operations
tk.Button(window, text="Add", width=10, bg="#99ccff", command=lambda: calculate("add")).grid(row=3, column=0, pady=10)
tk.Button(window, text="Subtract", width=10, bg="#ffcc99", command=lambda: calculate("sub")).grid(row=3, column=1, pady=10)
tk.Button(window, text="Multiply", width=10, bg="#ccff99", command=lambda: calculate("mul")).grid(row=3, column=2, pady=10)

tk.Button(window, text="Divide", width=10, bg="#ff9999", command=lambda: calculate("div")).grid(row=4, column=0, pady=10)
tk.Button(window, text="Modulo", width=10, bg="#d9b3ff", command=lambda: calculate("mod")).grid(row=4, column=1, pady=10)

# Result Label
label_result = tk.Label(window, text="Result: ", font=("Arial", 12, "bold"), bg="#f2f2f2", fg="darkblue")
label_result.grid(row=5, column=0, columnspan=3, pady=15)

# Run the GUI loop
window.mainloop()