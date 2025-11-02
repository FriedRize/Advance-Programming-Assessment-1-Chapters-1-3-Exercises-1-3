import tkinter as tk
from tkinter import ttk, messagebox

class ShapeDrawer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Drawer")
        self.geometry("600x500")
        self.resizable(False, False)

        # --- Canvas ---
        self.canvas = tk.Canvas(self, width=400, height=350, bg="white", relief="sunken", borderwidth=2)
        self.canvas.pack(side="right", padx=10, pady=10)

        # --- Control Frame ---
        control_frame = ttk.Frame(self)
        control_frame.pack(side="left", fill="y", padx=10, pady=10)

        ttk.Label(control_frame, text="Select a shape:", font=("Arial", 11)).pack(pady=5)
        self.shape_var = tk.StringVar()
        shapes = ["Oval", "Rectangle", "Square", "Triangle"]
        self.shape_menu = ttk.Combobox(control_frame, textvariable=self.shape_var, values=shapes, state="readonly")
        self.shape_menu.pack()
        self.shape_menu.bind("<<ComboboxSelected>>", self.update_inputs)

        # Frame for coordinate inputs
        self.input_frame = ttk.Frame(control_frame)
        self.input_frame.pack(pady=10, fill="x")

        # Draw button
        ttk.Button(control_frame, text="Draw Shape", command=self.draw_shape).pack(pady=10)
        ttk.Button(control_frame, text="Clear Canvas", command=lambda: self.canvas.delete("all")).pack(pady=5)

    def update_inputs(self, event=None):
        """Update coordinate entry boxes depending on selected shape"""
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        shape = self.shape_var.get()

        if shape in ["Oval", "Rectangle"]:
            ttk.Label(self.input_frame, text="x1:").pack()
            self.x1_entry = ttk.Entry(self.input_frame)
            self.x1_entry.pack()
            ttk.Label(self.input_frame, text="y1:").pack()
            self.y1_entry = ttk.Entry(self.input_frame)
            self.y1_entry.pack()
            ttk.Label(self.input_frame, text="x2:").pack()
            self.x2_entry = ttk.Entry(self.input_frame)
            self.x2_entry.pack()
            ttk.Label(self.input_frame, text="y2:").pack()
            self.y2_entry = ttk.Entry(self.input_frame)
            self.y2_entry.pack()

        elif shape == "Square":
            ttk.Label(self.input_frame, text="Top-left x:").pack()
            self.x1_entry = ttk.Entry(self.input_frame)
            self.x1_entry.pack()
            ttk.Label(self.input_frame, text="Top-left y:").pack()
            self.y1_entry = ttk.Entry(self.input_frame)
            self.y1_entry.pack()
            ttk.Label(self.input_frame, text="Side length:").pack()
            self.side_entry = ttk.Entry(self.input_frame)
            self.side_entry.pack()

        elif shape == "Triangle":
            ttk.Label(self.input_frame, text="x1, y1 (1st vertex):").pack()
            self.x1_entry = ttk.Entry(self.input_frame)
            self.x1_entry.pack()
            self.y1_entry = ttk.Entry(self.input_frame)
            self.y1_entry.pack()

            ttk.Label(self.input_frame, text="x2, y2 (2nd vertex):").pack()
            self.x2_entry = ttk.Entry(self.input_frame)
            self.x2_entry.pack()
            self.y2_entry = ttk.Entry(self.input_frame)
            self.y2_entry.pack()

            ttk.Label(self.input_frame, text="x3, y3 (3rd vertex):").pack()
            self.x3_entry = ttk.Entry(self.input_frame)
            self.x3_entry.pack()
            self.y3_entry = ttk.Entry(self.input_frame)
            self.y3_entry.pack()

    def draw_shape(self):
        """Draw the selected shape based on input coordinates"""
        shape = self.shape_var.get()
        try:
            if shape in ["Oval", "Rectangle"]:
                x1, y1, x2, y2 = map(float, (self.x1_entry.get(), self.y1_entry.get(),
                                             self.x2_entry.get(), self.y2_entry.get()))
                if shape == "Oval":
                    self.canvas.create_oval(x1, y1, x2, y2, outline="blue", width=2)
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="green", width=2)

            elif shape == "Square":
                x1, y1 = float(self.x1_entry.get()), float(self.y1_entry.get())
                side = float(self.side_entry.get())
                x2, y2 = x1 + side, y1 + side
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="purple", width=2)

            elif shape == "Triangle":
                x1, y1 = float(self.x1_entry.get()), float(self.y1_entry.get())
                x2, y2 = float(self.x2_entry.get()), float(self.y2_entry.get())
                x3, y3 = float(self.x3_entry.get()), float(self.y3_entry.get())
                self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="red", fill="", width=2)

            else:
                messagebox.showwarning("Select Shape", "Please select a shape to draw.")

        except Exception:
            messagebox.showerror("Invalid Input", "Please enter valid coordinate values!")

# --- Run the App ---
if __name__ == "__main__":
    app = ShapeDrawer()
    app.mainloop()
