# ==============================================
# 🍔 ZENIE'S BURGER SHACK - Ordering System
# ==============================================

def display_menu(title, options):
    """Displays a numbered menu and returns the user's choice"""
    print(f"\n--- {title} ---")
    for i, item in enumerate(options, start=1):
        print(f"{i}. {item}")
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")


def choose_multiple(title, options):
    """Allows user to choose multiple items from a list"""
    print(f"\n--- {title} (choose any, separated by commas, or 0 for none) ---")
    for i, item in enumerate(options, start=1):
        print(f"{i}. {item}")
    choice = input("Enter your choices (e.g. 1,3): ").strip()
    if choice == "0" or choice == "":
        return []
    selected = []
    for c in choice.split(","):
        try:
            idx = int(c)
            if 1 <= idx <= len(options):
                selected.append(options[idx - 1])
        except ValueError:
            continue
    return selected


def calculate_total(burger, toppings, condiments, sides):
    """Calculates total cost"""
    prices = {
        "Beef Burger": 20.0,
        "Chicken Burger": 18.0,
        "Vegetarian Burger": 16.0,
        "Cheese": 2.0,
        "Peanut Butter": 3.0,
        "Avocado": 4.0,
        "Ketchup": 0.5,
        "Mayonnaise": 0.5,
        "BBQ Sauce": 1.0,
        "Fries": 6.0,
        "Drink": 4.0,
        "Onion Rings": 7.0
    }
    total = 0
    total += prices.get(burger, 0)
    for t in toppings + condiments + sides:
        total += prices.get(t, 0)
    return total


def handle_payment(total):
    """Handles payment and returns change"""
    print(f"\nYour total is AED {total:.2f}")
    while True:
        try:
            paid = float(input("Enter payment amount (AED): "))
            if paid < total:
                print("Not enough payment. Please enter a higher amount.")
            else:
                change = paid - total
                print(f"Change: AED {change:.2f}")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("==============================================")
    print("🍔  WELCOME TO ZENIE'S BURGER SHACK - RAK 🍟")
    print("==============================================")

    burgers = ["Beef Burger", "Chicken Burger", "Vegetarian Burger"]
    toppings = ["Cheese", "Peanut Butter", "Avocado"]
    condiments = ["Ketchup", "Mayonnaise", "BBQ Sauce"]
    sides = ["Fries", "Drink", "Onion Rings"]

    burger_choice = display_menu("Choose your burger", burgers)
    topping_choice = choose_multiple("Choose toppings", toppings)
    condiment_choice = choose_multiple("Choose condiments", condiments)
    side_choice = choose_multiple("Choose sides", sides)

    print("\n--- ORDER SUMMARY ---")
    print(f"Burger: {burger_choice}")
    print(f"Toppings: {', '.join(topping_choice) if topping_choice else 'None'}")
    print(f"Condiments: {', '.join(condiment_choice) if condiment_choice else 'None'}")
    print(f"Sides: {', '.join(side_choice) if side_choice else 'None'}")

    total = calculate_total(burger_choice, topping_choice, condiment_choice, side_choice)
    handle_payment(total)

    print("\n✅ Thank you for dining at ZENIE'S BURGER SHACK! Enjoy your meal! 🍔")


if __name__ == "__main__":
    main()
