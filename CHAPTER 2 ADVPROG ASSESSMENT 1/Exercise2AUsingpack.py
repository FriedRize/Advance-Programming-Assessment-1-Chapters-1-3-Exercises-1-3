import tkinter as tk

# Create main window
window = tk.Tk()
window.title("GUI Pack Example")
window.geometry("400x200")
window.configure(bg="lightgray")

# Label A (Top - fills horizontally)
labelA = tk.Label(window, text="A", bg="red", fg="black", bd=5, relief="raised")
labelA.pack(fill=tk.X)

# Frame to hold C and D side-by-side
frame_middle = tk.Frame(window, bg="lightgray")
frame_middle.pack(fill=tk.X)

# Label C (Left side)
labelC = tk.Label(frame_middle, text="C", bg="blue", fg="white", bd=5, relief="sunken", width=10)
labelC.pack(side=tk.LEFT)

# Label D (Right side)
labelD = tk.Label(frame_middle, text="D", bg="white", fg="black", bd=5, relief="ridge", width=10)
labelD.pack(side=tk.RIGHT)

# Label B (Bottom - centered)
labelB = tk.Label(window, text="B", bg="yellow", fg="black", bd=5, relief="groove", width=10)
labelB.pack(pady=5)

# Run the GUI loop
window.mainloop()