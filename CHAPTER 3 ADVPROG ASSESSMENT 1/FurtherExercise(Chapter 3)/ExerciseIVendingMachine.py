import tkinter as tk
from tkinter import ttk, messagebox

class VendingMachine(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🥤 ZENIE'S VENDING MACHINE 🍪")
        self.geometry("520x550")
        self.resizable(False, False)
        self.configure(bg="#0d0d0d")  # black background

        # --- Define Theme Colors ---
        self.primary_color = "#6A0DAD"  # purple
        self.secondary_color = "#0077FF"  # blue
        self.text_color = "white"

        # --- Prices ---
        self.items = {
            "Coke": 4.0,
            "Sprite": 4.0,
            "Water": 2.0,
            "Lays": 3.5,
            "Doritos": 4.0,
            "Oreo": 2.5,
            "KitKat": 3.0,
            "Pringles": 5.0
        }

        self.selected_items = {}

        # --- Title ---
        title_label = tk.Label(
            self,
            text="ZENIE'S VENDING MACHINE",
            font=("Trebuchet MS", 18, "bold"),
            bg="#0d0d0d",
            fg=self.secondary_color
        )
        title_label.pack(pady=20)

        subtitle = tk.Label(
            self,
            text="Choose your favorite drink or snack!",
            font=("Arial", 11),
            bg="#0d0d0d",
            fg=self.primary_color
        )
        subtitle.pack()

        # --- Items Frame ---
        items_frame = tk.Frame(self, bg="#0d0d0d", highlightbackground=self.primary_color, highlightthickness=2)
        items_frame.pack(padx=20, pady=15, fill="x")

        label = tk.Label(
            items_frame, text="Select Your Items", font=("Arial", 13, "bold"),
            bg="#0d0d0d", fg=self.text_color
        )
        label.pack(pady=5)

        for item, price in self.items.items():
            var = tk.IntVar()
            chk = tk.Checkbutton(
                items_frame,
                text=f"{item} - AED {price:.2f}",
                variable=var,
                bg="#0d0d0d",
                fg=self.text_color,
                selectcolor=self.primary_color,
                activebackground="#0d0d0d",
                font=("Arial", 11)
            )
            chk.pack(anchor="w", padx=25, pady=3)
            self.selected_items[item] = var

        # --- Payment Frame ---
        payment_frame = tk.Frame(self, bg="#0d0d0d", highlightbackground=self.secondary_color, highlightthickness=2)
        payment_frame.pack(padx=20, pady=15, fill="x")

        tk.Label(payment_frame, text="Total (AED):", font=("Arial", 12), bg="#0d0d0d", fg=self.text_color).grid(row=0, column=0, padx=5, pady=5)
        self.total_var = tk.StringVar(value="0.00")
        tk.Entry(payment_frame, textvariable=self.total_var, width=10, state="readonly", 
                 justify="center", font=("Arial", 12), bg="#1a1a1a", fg=self.secondary_color, bd=0).grid(row=0, column=1, padx=5)

        calc_btn = tk.Button(
            payment_frame,
            text="Calculate Total",
            command=self.calculate_total,
            font=("Arial", 11, "bold"),
            bg=self.primary_color,
            fg="white",
            activebackground=self.secondary_color,
            relief="flat",
            padx=10, pady=5
        )
        calc_btn.grid(row=0, column=2, padx=15, pady=5)

        tk.Label(payment_frame, text="Payment (AED):", font=("Arial", 12), bg="#0d0d0d", fg=self.text_color).grid(row=1, column=0, padx=5, pady=5)
        self.payment_entry = tk.Entry(payment_frame, width=10, justify="center",
                                      font=("Arial", 12), bg="#1a1a1a", fg=self.secondary_color, bd=0)
        self.payment_entry.grid(row=1, column=1, padx=5, pady=5)

        pay_btn = tk.Button(
            payment_frame,
            text="Pay",
            command=self.process_payment,
            font=("Arial", 11, "bold"),
            bg=self.secondary_color,
            fg="white",
            activebackground=self.primary_color,
            relief="flat",
            padx=15, pady=5
        )
        pay_btn.grid(row=1, column=2, padx=15, pady=5)

        # --- Change Label ---
        self.change_label = tk.Label(payment_frame, text="", font=("Arial", 12, "bold"),
                                     bg="#0d0d0d", fg="#00FFAA")
        self.change_label.grid(row=2, column=0, columnspan=3, pady=10)

        # --- Footer ---
        footer = tk.Label(
            self,
            text="Thank you for choosing ZENIE'S 💜💙",
            bg="#0d0d0d",
            fg="#6666FF",
            font=("Arial", 10, "italic")
        )
        footer.pack(side="bottom", pady=10)

    # --- Functions ---
    def calculate_total(self):
        """Calculate total based on selected items"""
        total = 0
        for item, var in self.selected_items.items():
            if var.get() == 1:
                total += self.items[item]
        self.total_var.set(f"{total:.2f}")

    def process_payment(self):
        """Handle payment and show change"""
        try:
            total = float(self.total_var.get())
            payment = float(self.payment_entry.get())
            if total == 0:
                messagebox.showwarning("No Items", "Please select at least one item.")
                return
            if payment < total:
                messagebox.showerror("Insufficient Payment", "Not enough money! Please insert more.")
            else:
                change = payment - total
                self.change_label.config(text=f"Change: AED {change:.2f}")
                messagebox.showinfo("Purchase Successful", "Enjoy your snacks and drinks! 🥤🍪")
                self.reset()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for payment.")

    def reset(self):
        """Reset selections and payment after purchase"""
        for var in self.selected_items.values():
            var.set(0)
        self.payment_entry.delete(0, tk.END)
        self.total_var.set("0.00")

# --- Run App ---
if __name__ == "__main__":
    app = VendingMachine()
    app.mainloop()
