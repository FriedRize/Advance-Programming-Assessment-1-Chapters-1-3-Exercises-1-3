import tkinter as tk
from tkinter import messagebox

# Function to convert temperature
def convert_temp():
    try:
        temp = float(entry_temp.get())
        if var.get() == 1:  # Celsius to Fahrenheit
            result = (temp * 9/5) + 32
            label_result.config(text=f"{temp}°C = {result:.2f}°F")
        elif var.get() == 2:  # Fahrenheit to Celsius
            result = (temp - 32) * 5/9
            label_result.config(text=f"{temp}°F = {result:.2f}°C")
        else:
            messagebox.showwarning("Selection Missing", "Please select a conversion type.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

# Create main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("400x250")
window.resizable(False, False)
window.configure(bg="#e6f2ff")

# Title Label
label_title = tk.Label(window, text="Temperature Converter", 
                       font=("Helvetica", 16, "bold"), bg="#e6f2ff", fg="darkblue")
label_title.pack(pady=10)

# Input Frame
frame_input = tk.Frame(window, bg="#e6f2ff")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Enter Temperature:", bg="#e6f2ff", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_temp = tk.Entry(frame_input, width=15)
entry_temp.grid(row=0, column=1, padx=5)

# Radio buttons for conversion type
var = tk.IntVar()
tk.Radiobutton(window, text="Celsius to Fahrenheit", variable=var, value=1, bg="#e6f2ff", font=("Arial", 11)).pack()
tk.Radiobutton(window, text="Fahrenheit to Celsius", variable=var, value=2, bg="#e6f2ff", font=("Arial", 11)).pack()

# Convert Button
btn_convert = tk.Button(window, text="Convert", bg="lightgreen", font=("Arial", 12, "bold"), command=convert_temp)
btn_convert.pack(pady=10)

# Result Label
label_result = tk.Label(window, text="Result: ", font=("Arial", 13, "bold"), bg="#e6f2ff", fg="darkred")
label_result.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()