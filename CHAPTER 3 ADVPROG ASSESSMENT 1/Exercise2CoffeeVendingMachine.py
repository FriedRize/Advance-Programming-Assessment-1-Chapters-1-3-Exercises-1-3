import tkinter as tk
from tkinter import messagebox

# ---------------------------- WINDOW SETUP ---------------------------- #
root = tk.Tk()
root.title("ZENS COFFEE MACHINE")
root.geometry("650x600")
root.config(bg="lightgray")

# ---------------------------- VARIABLES ---------------------------- #
coffee_var = tk.StringVar(value="Cappuccino")
sugar_var = tk.IntVar(value=0)
milk_var = tk.IntVar(value=0)
money_var = tk.DoubleVar(value=0.0)

coffee_prices = {
    "Cappuccino": 2.5,
    "Latte": 3.0,
    "Espresso": 2.0
}

# ---------------------------- FUNCTIONS ---------------------------- #
def update_image():
    coffee = coffee_var.get()
    if coffee == "Cappuccino":
        coffee_img_label.config(image=cappuccino_img)
        coffee_img_label.image = cappuccino_img
    elif coffee == "Latte":
        coffee_img_label.config(image=latte_img)
        coffee_img_label.image = latte_img
    else:
        coffee_img_label.config(image=espresso_img)
        coffee_img_label.image = espresso_img

def show_order():
    coffee = coffee_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()
    money = money_var.get()
    price = coffee_prices[coffee]

    if money < price:
        messagebox.showwarning("Insufficient Money", f"Please insert ${price:.2f}.")
        return

    change = money - price
    order_summary = f"Coffee: {coffee}\nSugar: {sugar} tsp\nMilk: {milk} ml\nPaid: ${money:.2f}\nChange: ${change:.2f}"
    messagebox.showinfo("Order Summary", order_summary)

# ---------------------------- IMAGES ---------------------------- #
cappuccino_img = tk.PhotoImage(file="cappuccino.png").subsample(6,6)
latte_img = tk.PhotoImage(file="latte.png").subsample(5,5)
espresso_img = tk.PhotoImage(file="espresso.png").subsample(4,4)

# ---------------------------- TITLE BOX ---------------------------- #
title_box = tk.Frame(root, bg="saddlebrown", bd=2, relief="raised")
title_box.pack(fill="x", pady=5, padx=5)

title_label = tk.Label(
    title_box,
    text="☕ ZENS COFFEE MACHINE ☕",
    bg="saddlebrown", fg="lightgray",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=5)

# ---------------------------- COFFEE + IMAGE BOX ---------------------------- #
coffee_image_box = tk.Frame(root, bg="white", bd=2, relief="ridge", padx=5, pady=5)
coffee_image_box.pack(fill="x", pady=5, padx=10)

# Coffee options (left)
options_frame = tk.Frame(coffee_image_box, bg="white")
options_frame.pack(side=tk.LEFT, anchor="n", padx=5)

tk.Label(options_frame, text="Select Coffee:", bg="white", fg="saddlebrown", font=("Arial", 14, "bold")).pack(anchor="w", pady=(0,5))

def create_coffee_choice(text, value):
    frame = tk.Frame(options_frame, bg="white", bd=1, relief="solid", padx=3, pady=3)
    tk.Radiobutton(frame, text=text, variable=coffee_var, value=value, bg="white", fg="saddlebrown", font=("Arial", 12), command=update_image).pack(anchor="w")
    frame.pack(fill="x", pady=3)
    return frame

create_coffee_choice("Cappuccino", "Cappuccino")
create_coffee_choice("Latte", "Latte")
create_coffee_choice("Espresso", "Espresso")

# Coffee image (right)
coffee_img_label = tk.Label(coffee_image_box, image=cappuccino_img, bg="white")
coffee_img_label.pack(side=tk.RIGHT, padx=10, pady=5)

# ---------------------------- OPTIONS BOX ---------------------------- #
options_box = tk.Frame(root, bg="white", bd=2, relief="ridge", padx=5, pady=5)
options_box.pack(fill="x", pady=5, padx=10)

tk.Label(options_box, text="Options:", bg="white", fg="saddlebrown", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0,3))

def create_option(text, var, onvalue, offvalue):
    frame = tk.Frame(options_box, bg="white", bd=1, relief="solid", padx=3, pady=3)
    tk.Checkbutton(frame, text=text, variable=var, bg="white", fg="saddlebrown", font=("Arial", 12), onvalue=onvalue, offvalue=offvalue).pack(anchor="w")
    frame.pack(fill="x", pady=3)
    return frame

create_option("Sugar (1 tsp)", sugar_var, 1, 0)
create_option("Milk (50 ml)", milk_var, 50, 0)

# ---------------------------- MONEY BOX ---------------------------- #
money_box = tk.Frame(root, bg="white", bd=2, relief="ridge", padx=5, pady=5)
money_box.pack(fill="x", pady=5, padx=10)

tk.Label(money_box, text="Insert Money ($):", bg="white", fg="saddlebrown", font=("Arial", 12, "bold")).pack(anchor="w")
tk.Entry(money_box, textvariable=money_var, width=8, font=("Arial", 12)).pack(anchor="w", pady=3)

# ---------------------------- PLACE ORDER BOX ---------------------------- #
order_box = tk.Frame(root, bg="white", bd=2, relief="ridge", padx=5, pady=5)
order_box.pack(fill="x", pady=5, padx=10)

tk.Button(order_box, text="Place Order", bg="saddlebrown", fg="white", font=("Arial", 12, "bold"), command=show_order).pack(pady=3)

# ---------------------------- INIT IMAGE ---------------------------- #
update_image()

root.mainloop()
