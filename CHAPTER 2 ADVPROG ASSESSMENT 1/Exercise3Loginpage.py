import tkinter as tk
from tkinter import messagebox

# Function for login button
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create main window
window = tk.Tk()
window.title("Login Page")
window.geometry("350x200")
window.resizable(False, False)
window.configure(bg="#E8E8E8")

# Create and place widgets using grid()
# Title label
label_title = tk.Label(window, text="User Login", font=("Helvetica", 16, "bold"), bg="#E8E8E8")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Username label and entry
label_username = tk.Label(window, text="Username:", bg="#E8E8E8", font=("Arial", 12))
label_username.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_username = tk.Entry(window, width=25)
entry_username.grid(row=1, column=1, padx=10, pady=5)

# Password label and entry
label_password = tk.Label(window, text="Password:", bg="#E8E8E8", font=("Arial", 12))
label_password.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(window, width=25, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=5)

# Login button
btn_login = tk.Button(window, text="Login", bg="blue", fg="white", width=10, command=login)
btn_login.grid(row=3, column=0, columnspan=2, pady=15)

# Run the Tkinter event loop
window.mainloop()