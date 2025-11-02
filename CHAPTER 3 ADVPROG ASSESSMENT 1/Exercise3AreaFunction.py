import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

class ShapeAreaCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Area Calculator")
        self.geometry("400x300")
        self.resizable(False, False)

        # Create a Notebook (tabbed interface)
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both', padx=10, pady=10)

        # Add tabs
        self.circle_tab(notebook)
        self.square_tab(notebook)
        self.rectangle_tab(notebook)

    # --- Circle Tab ---
    def circle_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Circle")

        ttk.Label(frame, text="Enter radius (r):").pack(pady=10)
        radius_entry = ttk.Entry(frame)
        radius_entry.pack()

        result_label = ttk.Label(frame, text="", font=("Arial", 12))
        result_label.pack(pady=10)

        def calc_circle_area():
            try:
                r = float(radius_entry.get())
                area = math.pi * (r ** 2)
                result_label.config(text=f"Area = {area:.2f}")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number.")

        ttk.Button(frame, text="Calculate Area", command=calc_circle_area).pack(pady=5)

    # --- Square Tab ---
    def square_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Square")

        ttk.Label(frame, text="Enter side length (a):").pack(pady=10)
        side_entry = ttk.Entry(frame)
        side_entry.pack()

        result_label = ttk.Label(frame, text="", font=("Arial", 12))
        result_label.pack(pady=10)

        def calc_square_area():
            try:
                a = float(side_entry.get())
                area = a ** 2
                result_label.config(text=f"Area = {area:.2f}")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number.")

        ttk.Button(frame, text="Calculate Area", command=calc_square_area).pack(pady=5)

    # --- Rectangle Tab ---
    def rectangle_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Rectangle")

        ttk.Label(frame, text="Enter length (l):").pack(pady=5)
        length_entry = ttk.Entry(frame)
        length_entry.pack()

        ttk.Label(frame, text="Enter width (w):").pack(pady=5)
        width_entry = ttk.Entry(frame)
        width_entry.pack()

        result_label = ttk.Label(frame, text="", font=("Arial", 12))
        result_label.pack(pady=10)

        def calc_rectangle_area():
            try:
                l = float(length_entry.get())
                w = float(width_entry.get())
                area = l * w
                result_label.config(text=f"Area = {area:.2f}")
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid numbers.")

        ttk.Button(frame, text="Calculate Area", command=calc_rectangle_area).pack(pady=5)


# --- Run Application ---
if __name__ == "__main__":
    app = ShapeAreaCalculator()
    app.mainloop()
